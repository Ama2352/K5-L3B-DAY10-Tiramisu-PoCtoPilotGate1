"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def warehouse_costs(trials):
    """Observed operating VND/ticket by warehouse, without labels or pass/fail.

    Unit review price and note discount are from ops_facts in the supplied
    mock: 10,000 VND/review and 0.4 units for a recheck with a decision note.
    Does not include standby or infer financial harm from unlabelled trials.
    """
    totals = {}
    for trial in trials:
        warehouse = trial.get("warehouse") or "?"
        row = totals.setdefault(warehouse, {"count": 0, "machine": 0, "human": 0})
        row["count"] += 1
        row["machine"] += trial.get("cost_vnd", 0)
        kind = trial.get("review_kind")
        has_note = any(e.get("type") == "decision_note" for e in trial.get("events", []))
        units = 0.4 if kind == "recheck" and has_note else (1.0 if kind else 0.0)
        row["human"] += units * 10000
    return {warehouse: {"machine": r["machine"] / r["count"],
                        "human": r["human"] / r["count"],
                        "operating": (r["machine"] + r["human"]) / r["count"]}
            for warehouse, r in totals.items()}


def worst_warehouse_operating_cost_vnd(trials):
    return max((r["operating"] for r in warehouse_costs(trials).values()), default=0)


def worst_warehouse_machine_cost_vnd(trials):
    return max((r["machine"] for r in warehouse_costs(trials).values()), default=0)


def worst_warehouse_human_cost_vnd(trials):
    return max((r["human"] for r in warehouse_costs(trials).values()), default=0)


def repeated_refund_write_vnd(trials):
    """Proxy for money at risk: subsequent refund writes within one ticket.

    Not total wrongful refunds: it cannot see the initial/manual ledger or
    cross-ticket entitlement. Finance reconciliation remains necessary.
    Average over seeds for the same per-day convention as the report.
    """
    seeds = {t.get("seed") for t in trials}
    return sum(sum(r["amount_vnd"] for r in t.get("ledger", [])[1:])
               for t in trials) / max(1, len(seeds))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "worst_warehouse_operating_cost_vnd": worst_warehouse_operating_cost_vnd,
    "worst_warehouse_machine_cost_vnd": worst_warehouse_machine_cost_vnd,
    "worst_warehouse_human_cost_vnd": worst_warehouse_human_cost_vnd,
    "repeated_refund_write_vnd": repeated_refund_write_vnd,
}
STARTER_MONITORS = ("escalation_rate",)
