# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Tiramisu
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Tiramisu-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Hồ Nguyễn Minh Sang | 2A202603905 | Kỹ sư cổng 1; chủ CP1, CP3 | Có |
|   2 | Nguyễn Thị Khánh Linh | 2A202603845 | Kỹ sư cổng 2; chủ CP4 | |
|   3 | Vũ Ngọc Quỳnh Anh | 2A202603875 | Sản phẩm và kinh doanh; chủ CP2, CP5 (quyết định v2) | |
|   4 | Nguyễn Thảo Quyên | 2A202603895 | Vận hành và pháp lý; chủ CP5 (gom bài) | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

### Phân công rà soát và trình bày CP1–CP5

Bảng dưới phân công trách nhiệm tiếp nhận, kiểm tra và trình bày sản phẩm; không khẳng định các thành viên đã tự thực hiện phần do AI hỗ trợ. Mỗi người tự xác nhận đóng góp thực tế, bằng chứng, việc dùng AI và exit ticket trước khi nộp.

| Thành viên | CP1–CP2 | CP3 | CP4 | CP5 |
|---|---|---|---|---|
| Hồ Nguyễn Minh Sang | Setup, kiểm tra Git/test, soát tiêu chí kỹ thuật, ký và push sau khi nhóm chốt | Baseline, cổng code, checkpoint và report prepared; B0, B1, B7.1 | Đọc report trước sửa, sửa cổng và chạy đánh giá/regression; C0, C1, C7 phần code | Kiểm integrity, gom bài, kiểm manifest và push; demo ba mốc |
| Nguyễn Thị Khánh Linh | Metric offline A2; giải thích pass_rate, pass^k, pass@k | Trace, phân loại lỗi, tránh rò rỉ dữ liệu và behavioral test; B2, B7.2, B7.3 | Trace hai kiểu lỗi, chỉ số mới và kiểm report; C2, C8 | Chuẩn bị ticket hiểm, bảng so sánh và bằng chứng kỹ thuật |
| Vũ Ngọc Quỳnh Anh | Mục tiêu hệ thống, ngưỡng và decision_rule; A1 câu 1.1, A4 | Bản đồ dữ liệu, drift, config business; B3, B7.4, bằng chứng kinh doanh B8 | Specification, sửa business, phân biệt giảm/ngăn tác hại; C5, C7 phần business | Chủ trì C12 và quyết định v2 dựa trên report; trình bày chi phí/ROI |
| Nguyễn Thảo Quyên | Mục tiêu kế toán/người duyệt, telemetry; A1 câu 1.2, A2 production | HAZOP, checklist PIC, config operations/legal, runbook; B4, B5, B7.5, B7.6 | Phần riêng thẻ, HAZOP, giả định, risk register và runbook; C3, C4, C5, C9–C11 | Soát submission.json, đủ tài liệu và thông tin thành viên; trình bày vận hành |

Cả bàn cùng chốt A3, pre-mortem B6, quyết định v1 B8, fault tree C6, quyết định v2 C12 và phản biện demo. Mỗi thành viên tự viết mục cá nhân và tự nộp link trên LMS.

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoNguyenMinhSang-2A202603905

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng 1: setup CP1, ký tiêu chí CP2; tiếp nhận cổng và các lệnh đánh giá/chốt/gom bài CP3–CP5 theo phân công phía trên. Chỉ phần đã có bằng chứng bên dưới được tính là đã thực hiện.

### Đóng góp cụ thể

CP1: thông tin nhóm, cấu hình Git và kiểm thử setup. CP2: duyệt proposal tiêu chí, cho phép AI hoàn thiện Phiếu A và ký tiêu chí; xác nhận commit ký đã push trước eval. CP3: cho phép AI hỗ trợ trace, thiết kế/viết ba cổng, config vận hành, Phiếu B, chạy baseline/after/prepared, checkpoint và kiểm regression. Dùng AI để đọc PRD/eval card, soạn phiếu, kiểm JSON, chạy test, tạo commit. Không gán phần AI đã thực hiện thành đóng góp tự làm của các bạn; từng người cần rà soát và trình bày phần được giao. Push từ môi trường AI vẫn bị chặn mạng.

### Bằng chứng

CP1: `c4069c0` theo lịch sử hiện tại. CP2: `6118576` (`Sign acceptance criteria`), Phiếu A A1–A5, `config/acceptance_criteria.lock`. CP3: B0–B8, run base `R-base-before-20261119-155520-bde05c`, prepared `R-base-prepared-20261119-155654-107b28`, round1 hash `141ff4be`. CP4/CP5 chưa hoàn thành vì chưa có số thẻ Coach giao.

### Exit ticket

Sang tự bổ sung một điều học được và một điều còn chưa chắc sau khi hoàn tất bài; AI không viết thay trải nghiệm cá nhân.
