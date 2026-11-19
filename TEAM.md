# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Tiramisu
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Tiramisu-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5 — CFO: mỗi ticket qua trợ lý đang đắt hơn làm tay

## Thành viên

| STT | Họ và tên | MSSV | GitHub | Vai | Trưởng nhóm |
| --: | --------- | ---- | ------ | --- | :---------: |
|   1 | Hồ Nguyễn Minh Sang | 2A202603905 | Ama2352 | Kỹ sư cổng 1; chủ CP1, CP3 | Có |
|   2 | Nguyễn Thị Khánh Linh | 2A202603845 | xrkhanhlinh | Kỹ sư cổng 2; chủ CP4 | |
|   3 | Vũ Ngọc Quỳnh Anh | 2A202603875 | qavu2407-lang | Sản phẩm và kinh doanh; chủ CP2, CP5 (quyết định v2) | |
|   4 | Nguyễn Thảo Quyên | 2A202603895 | carwyn100678 | Vận hành và pháp lý; chủ CP5 (gom bài) | |

## Cá nhân

### Phân công rà soát và trình bày CP1–CP5

Các thành viên đã xác nhận phân công, đóng góp và sử dụng AI; đã rà soát nội dung và hai ticket hiểm B7.3. Mỗi người cần bổ sung exit ticket trước khi nộp.

| Thành viên | CP1–CP2 | CP3 | CP4 | CP5 |
|---|---|---|---|---|
| Hồ Nguyễn Minh Sang | Setup, kiểm tra Git/test, soát tiêu chí kỹ thuật, ký và push sau khi nhóm chốt | Baseline, cổng code, checkpoint và report prepared; B0, B1, B7.1 | Đọc report trước sửa, sửa cổng và chạy đánh giá/regression; C0, C1, C7 phần code | Kiểm integrity, gom bài, kiểm manifest và push; demo ba mốc |
| Nguyễn Thị Khánh Linh | Metric offline A2; giải thích pass_rate, pass^k, pass@k | Trace, phân loại lỗi, tránh rò rỉ dữ liệu và behavioral test; B2, B7.2, B7.3 | Trace hai kiểu lỗi, chỉ số mới và kiểm report; C2, C8 | Chuẩn bị ticket hiểm, bảng so sánh và bằng chứng kỹ thuật |
| Vũ Ngọc Quỳnh Anh | Mục tiêu hệ thống, ngưỡng và decision_rule; A1 câu 1.1, A4 | Bản đồ dữ liệu, drift, config business; B3, B7.4, bằng chứng kinh doanh B8 | Specification, sửa business, phân biệt giảm/ngăn tác hại; C5, C7 phần business | Chủ trì C12 và quyết định v2 dựa trên report; trình bày chi phí/ROI |
| Nguyễn Thảo Quyên | Mục tiêu kế toán/người duyệt, telemetry; A1 câu 1.2, A2 production | HAZOP, checklist PIC, config operations/legal, runbook; B4, B5, B7.5, B7.6 | Phần riêng thẻ, HAZOP, giả định, risk register và runbook; C3, C4, C5, C9–C11 | Soát submission.json, đủ tài liệu và thông tin thành viên; trình bày vận hành |

Cả bàn cùng chốt A3, pre-mortem B6, quyết định v1 B8, fault tree C6, quyết định v2 C12 và phản biện demo. Mỗi thành viên tự viết mục cá nhân và tự nộp link trên LMS.

### Tình trạng tài liệu và báo cáo

| Hạng mục | Đã có | Còn thiếu hoặc cần xác nhận |
|---|---|---|
| CP1 | Bảng 4 thành viên, phân vai, danh tính Git, 13 test setup đạt | Public/fork/Collaborators chưa xác minh trực tuyến được từ môi trường AI |
| CP2 | A1–A5, tiêu chí ký commit `6118576`, hash còn nguyên; đã push trước baseline | Nhóm tự giải thích được các ngưỡng khi demo; không sửa file đã ký |
| CP3 | B0–B8, ba cổng, config vận hành, snapshot `141ff4be`, commit `5823095`; 13 test và regression đạt; đã rà soát hai ticket hiểm | Cần thực hiện demo |
| Report vòng 1 | 4 report trong runs/ và journal; CP4 có grade-report cùng ba mốc S5 | runs/ là thư mục làm việc bị gitignore; bộ nộp dùng submission/runs/ do collect gom, phải collect lại khi code/config/report thay đổi |
| CP4 | S5 đã nhận đúng4 file; grade trước sửa được lưu; C0–C11, guards/monitors/config đã sửa. Grade R-S5-grade-20261119-165008-9a016e PASS-VISIBLE, integrity/visible/regression/monitor✅ | Test ẩn chưa có; chưa xác minh dữ liệu, concurrency, công suất và chi phí thực tế |
| CP5 | C12 và submission.json có v2 Thu hẹp,3 dòng; chi phí toàn luồng đã tính cả12 ca sỉ/ngày làm tay; lệnh7 in ĐỦ THÀNH PHẦN | Cần hoàn tất demo, exit ticket và nộp LMS; test ẩn chưa chạy |

## HoNguyenMinhSang-2A202603905

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng 1: setup CP1, ký tiêu chí CP2; tiếp nhận cổng và các lệnh đánh giá/chốt/gom bài CP3–CP5 theo phân công phía trên.

### Đóng góp cụ thể

Setup Git/test, duyệt và ký tiêu chí, quản lý commit/push; dùng AI hỗ trợ cổng code, config, Phiếu A–C, eval/checkpoint/grade và gom bài. Đã rà soát kết quả và quyết định v2 Thu hẹp.

### Bằng chứng

Commit `6118576`, `5823095`, `f42bcb9`, `7cb7a16`; Phiếu A–C. Baseline `R-base-before-20261119-155520-bde05c`, prepared `R-base-prepared-20261119-155654-107b28`, grade S5 `R-S5-grade-20261119-165008-9a016e`. Bộ nền đạt 110/110; S5 đạt 90/90 với độ phủ 60%.

### Exit ticket

Cần bổ sung một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Dùng AI hỗ trợ đọc tài liệu, soạn phiếu, đề xuất tiêu chí, viết cổng/config, chạy kiểm tra và gom bài; đã rà soát nội dung phần phụ trách.

## NguyenThiKhanhLinh-2A202603845

### Phần việc phụ trách

Kỹ sư cổng 2; phụ trách rà soát metric offline A2 (câu 1.3), giải thích pass_rate/pass^k/pass@k, trace và phân loại lỗi B2 (2.2), hai bước tránh rò rỉ đánh giá B7.2 (2.7), behavioral test B7.3 (2.8). Chủ CP4: phân tích hai kiểu lỗi ở C2 (3.1), triển khai chỉ số mới trong `lab10/monitors.py` và C8 (3.6), kiểm regression, chuẩn bị ticket hiểm cho demo. Cùng nhóm tham gia A3, B6, B8, C1, C6 và C12.

### Đóng góp cụ thể

Đã rà soát metric A2, trace T-002@55, quy trình giữ test ẩn độc lập và hai ticket hiểm B7.3; AI hỗ trợ soạn và chạy kiểm tra.

CP4: rà soát C2/C8, các ca chi trùng, chi phí kho sỉ và hoàn thiếu; kiểm công thức 4 monitor trong monitors.py. AI hỗ trợ phân tích và triển khai. Monitor/regression: Đạt.

### Bằng chứng

Commit `b647310`, `5823095`, `7cb7a16`; A2, B2, B7.2–B7.3, C2/C8; grade `R-S5-grade-20261119-165008-9a016e`.

### Exit ticket

Cần bổ sung một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Dùng AI hỗ trợ metric, trace, behavioral test và monitor; đã rà soát nội dung phần phụ trách.

## VuNgocQuynhAnh-2A202603875

### Phần việc phụ trách

Sản phẩm và kinh doanh; chủ CP2 và phần quyết định CP5. Phụ trách mục tiêu hệ thống A1 (1.1), tiêu chí/hành động/ngày xem lại A4 (1.6), bản đồ dữ liệu và drift B3 (2.3), config `business` và lý do con số B7.4 (2.9), bằng chứng kinh doanh B8. CP4: specification kiểm được ở C5 (3.2), sửa business và phân biệt giảm/ngăn ở C7 (3.5). CP5: chủ trì C12, giải thích chi phí/ROI và so v2 với v1. Cùng nhóm tham gia A3, B6, C6, các quyết định và demo.

### Đóng góp cụ thể

Đã rà soát mục tiêu, tiêu chí A4, bản đồ dữ liệu/drift, cổng business và bằng chứng quyết định v1. AI hỗ trợ tổng hợp và soạn nội dung.

CP4: rà soát specification, phạm vi bán lẻ và quyết định v2 Thu hẹp: 18/30 ca/ngày trong scope, 12 ca sỉ/ngày làm tay. Chi phí trong scope 3.980 đồng/ticket, ROI 1,51; toàn luồng 6.388,10 đồng/ticket, ROI khoảng 0,57. AI hỗ trợ phân tích report và soạn C5/C7/C12.

### Bằng chứng

Commit `6118576`, `b647310`, `5823095`, `7cb7a16`; A1/A4, B3/B7.4/B8, C5/C7/C12; grade `R-S5-grade-20261119-165008-9a016e`.

### Exit ticket

Cần bổ sung một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Dùng AI hỗ trợ PRD/eval card, mục tiêu, tiêu chí, bản đồ dữ liệu và quyết định; đã rà soát nội dung phần phụ trách.

## NguyenThaoQuyen-2A202603895

### Phần việc phụ trách

Vận hành và pháp lý; chủ CP5 phần gom bài. Phụ trách mục tiêu Oanh/Hạnh A1 (1.2), telemetry A2 (1.4), HAZOP và checklist B4/B5 (2.4), config `operations`/`legal` cùng runbook B7.5–B7.6 (2.10). CP4: mục riêng theo thẻ C3 (miễn với S4), HAZOP C4, giả định môi trường C5 (3.3), sửa vận hành/pháp lý C7, fault tree sau sửa/risk register/checklist/runbook C9–C11 (3.7). CP5: submission.json, kiểm đầy đủ hồ sơ và giải thích người trực/runbook khi demo. Cùng nhóm tham gia pre-mortem, fault tree và quyết định.

### Đóng góp cụ thể

Đã rà soát mục tiêu đối soát/người duyệt, telemetry PII, HAZOP, checklist 9 nhóm, runbook và config operations/legal. AI hỗ trợ soạn nội dung và metadata bài nộp.

CP4: rà soát C3.5/C4/C5/C9–C11, nguồn lực 12 ca sỉ/ngày làm tay và submission.json. AI hỗ trợ soạn phiếu, runbook, risk register và metadata. Cần hoàn tất demo và nộp LMS.

### Bằng chứng

Commit `b647310`, `5823095`, `7cb7a16`; A1/A2, B4/B5/B7.5–B7.6, C3.5/C4/C9–C11, submission/manifest.json; grade `R-S5-grade-20261119-165008-9a016e`.

### Exit ticket

Cần bổ sung một điều học được và một điều còn chưa chắc.

### Sử dụng AI

Dùng AI hỗ trợ mục tiêu, telemetry, HAZOP, checklist, runbook, config và metadata; đã rà soát nội dung phần phụ trách.
