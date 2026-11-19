"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Gate 1 (B6 technical): date-valid policy, never the cached active flag.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách hiệu lực")
    ctx.log("effective_policy", policy_id=policy["policy_id"])
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool in ("issue_refund", "file_carrier_fault"):
        order = ctx.tools.lookup_order(action.get("order_id"))
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not order or not policy or order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("thiếu nguồn sự thật hoặc sai chủ đơn")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)

    # Gate 2 (B4 WRONG/INVALID/PERTURBED): money movement must have evidence.
    if tool == "issue_refund":
        amount = action.get("amount_vnd")
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            return Verdict.deny("số tiền không hợp lệ")
        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        previous = ctx.tools.ledger_rows(order_id=order["order_id"])
        paid = sum(row["amount_vnd"] for row in previous)
        if amount + paid > entitlement:
            ctx.log("refund_evidence_mismatch", asked=amount, paid=paid, entitlement=entitlement)
            return Verdict.deny("số tiền hoặc khoản lặp vượt quyền lợi theo tracking/policy/sổ cái")
        if action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.escalate("chưa có căn cứ trừ tiền bên thứ ba")
        approval_id = action.get("approval_id")
        if approval_id:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id)
            valid = [a for a in approvals
                     if a.get("status") == "valid" and a.get("expires_at", "") >= ctx.as_of
                     and a.get("order_id") == order["order_id"]
                     and a.get("customer_id") == ctx.ticket.get("customer_id")
                     and a.get("ticket_id") == ctx.ticket.get("ticket_id")
                     and a.get("approver_id") == (ctx.gates.get("operations", {}).get("approver_id") or "NV-HANH")
                     and a.get("max_vnd", 0) >= amount
                     and not ctx.tools.ledger_rows(approval_id=approval_id)]
            if not valid:
                return Verdict.escalate("phê duyệt không đúng phạm vi/hiệu lực hoặc đã dùng")
        elif amount > policy["auto_limit_vnd"]:
            return Verdict.escalate("vượt hạn mức policy mà chưa có phê duyệt hợp lệ")

    # Gate 3 (B6 legal): evidence for strikes; minimise third-party disclosure.
    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking/policy không cho phép ghi lỗi hãng")
        return Verdict.modify("ghi lỗi đúng kiện và độ trễ DB", parcel_id=parcel["parcel_id"],
                              carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"),
                              delay_days=delay)
    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not policy:
            return Verdict.deny("thiếu chính sách chia sẻ dữ liệu")
        allowed = set(policy.get("carrier_notice_fields", [])) & {"order_id", "parcel_id", "district", "delay_days"}
        payload = {k: v for k, v in action.get("payload", {}).items() if k in allowed}
        if payload != action.get("payload"):
            return Verdict.modify("chỉ gửi trường được phép cho hãng", payload=payload)
    return Verdict.allow()
