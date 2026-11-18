# incidents/ · Gói sự cố (chưa có gì ở đây cho tới phút 125)

Thư mục này cố ý để trống lúc đầu buổi. Đây là chỗ **gói sự cố của bàn** sẽ xuất hiện.

**Phút 125**, sau giờ nghỉ, Lab Coach báo **số thẻ của bàn** (S1–S8) và mời tài khoản GitHub của các thành viên vào repo thẻ riêng tư (quyền Read). Ai chưa ở trong org GitHub của khoá thì mở email hoặc https://github.com/notifications và bấm chấp nhận lời mời.

1. Từ thư mục gốc repo của bàn (nhánh `main`, đã commit hết), chạy lệnh sau. Thay `Sx` bằng số thẻ của bàn (cả ba chỗ):

   ```bash
   git fetch https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_cards.git main && git checkout FETCH_HEAD -- incidents/Sx && git commit -m "Nhận thẻ Sx"
   ```

   `git fetch` tải repo thẻ về (chưa đổi gì trong bài); `git checkout FETCH_HEAD -- incidents/Sx` chép **đúng thư mục thẻ của bàn**; `git commit` lưu lại. Lệnh không gộp lịch sử git, không đụng bài của bàn. Rồi `git push -u origin main` để các bạn khác trong bàn `git pull` về.

   Báo `Repository not found` / `Authentication failed`: tài khoản GitHub trên máy chưa được mời hoặc chưa chấp nhận lời mời, báo Lab Coach. Nếu máy báo `Please tell me who you are`, làm bước 2b ở mục 2 của `README.md` rồi chạy lại.

   **Dự phòng:** nếu Lab Coach báo phát thẻ qua **repo mẫu**, chạy `git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main` (nếu báo `'upstream' does not appear to be a git repository`, gắn repo mẫu theo bước 2a ở mục 2 của `README.md`). Cách này tải cả 8 thẻ và file `incident-cards.md`; bàn vẫn chỉ làm thẻ của mình.

2. Bạn sẽ thấy thư mục mới `incidents/Sx/`.
3. Bàn **chỉ làm đúng thẻ của bàn**. Mở `incidents/Sx/card.md` và đọc mặt trước.
4. Ghi số thẻ vào dòng `Thẻ đã bốc:` ở đầu Phiếu C (`templates/form-c-incident.md`).
5. Chạy ngay `python3 -m lab10.grade --incident Sx`, khi chưa sửa gì, để xem cổng bàn dựng ở vòng 1 đỡ được bao nhiêu. Lấy thẻ đúng thì report có `1 integrity | ✅`.

Mỗi thư mục `incidents/Sx/` có:

| File | Nó là gì |
|---|---|
| `card.md` | Thẻ sự cố: mặt trước là tin nhắn báo sự cố, mặt sau là nhiệm vụ và luật |
| `tickets.jsonl` | Các ticket của sự cố, kèm kết quả đúng |
| `world_patch.json` | Dữ liệu bổ sung của sự cố (đơn hàng, phê duyệt, sổ cái có sẵn…) |
| `card.json` | Hai lệnh chạy và tự kiểm tra của thẻ |

Không sửa các file này: chúng bị khoá, lệnh tự kiểm tra sẽ phát hiện.

Nếu chạy lệnh tự kiểm tra (`python3 -m lab10.grade`) trước khi nhận thẻ, bạn sẽ thấy dòng `TỪ CHỐI KIỂM TRA: chưa có gói sự cố …`. Đó là đúng thiết kế, không phải lỗi máy.
