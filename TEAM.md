# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Tiramisu
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Tiramisu-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | GitHub | Vai | Trưởng nhóm |
| --: | --------- | ---- | ------ | --- | :---------: |
|   1 | Hồ Nguyễn Minh Sang | 2A202603905 | Ama2352 | Kỹ sư cổng 1; chủ CP1, CP3 | Có |
|   2 | Nguyễn Thị Khánh Linh | 2A202603845 | xrkhanhlinh | Kỹ sư cổng 2; chủ CP4 | |
|   3 | Vũ Ngọc Quỳnh Anh | 2A202603875 | qavu2407-lang | Sản phẩm và kinh doanh; chủ CP2, CP5 (quyết định v2) | |
|   4 | Nguyễn Thảo Quyên | 2A202603895 | carwyn100678 | Vận hành và pháp lý; chủ CP5 (gom bài) | |

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

### Tình trạng tài liệu và báo cáo

| Hạng mục | Đã có | Còn thiếu hoặc cần xác nhận |
|---|---|---|
| CP1 | Bảng 4 thành viên, phân vai, danh tính Git, 13 test setup đạt | Public/fork/Collaborators chưa xác minh trực tuyến được từ môi trường AI |
| CP2 | A1–A5, tiêu chí ký commit `6118576`, hash còn nguyên; Sang xác nhận đã push trước baseline | Nhóm tự giải thích được các ngưỡng khi demo; không sửa file đã ký |
| CP3 | B0–B8, ba cổng, config vận hành, snapshot `141ff4be`, commit `5823095`; 13 test và regression đạt | Thành viên rà lại phần được giao; một người không viết code đọc hai ticket hiểm |
| Report vòng 1 | 4 report trong `runs/`: base, hai lần after, prepared; `runs/journal.jsonl` ghi đủ lần chạy | `runs/` bị gitignore; chưa được gom vào `submission/runs/`, chưa phải bộ report nộp cuối |
| CP4 | Phân công đã rõ; snapshot prepared được giữ nguyên | Số thẻ Coach giao, đúng gói thẻ, grade trước sửa, C0–C11, sửa theo bằng chứng, monitor mới, report thẻ và regression sau sửa |
| CP5 | submission.json có tên nhóm, 4 members đúng MSSV và quyết định v1 | C12/quyết định v2/ba dòng, grade-report ba mốc, collect/manifest đạt, demo, exit ticket và mỗi người tự nộp LMS |

Các mục cá nhân dưới đây là bản mô tả theo phân công do AI hỗ trợ soạn. Bằng chứng trỏ tới sản phẩm của nhóm, không chứng minh mỗi người đã tự viết hoặc trực tiếp chạy lệnh. Từng người cần bổ sung đóng góp thực tế và tự viết exit ticket trước khi nộp.

## HoNguyenMinhSang-2A202603905

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng 1: setup CP1, ký tiêu chí CP2; tiếp nhận cổng và các lệnh đánh giá/chốt/gom bài CP3–CP5 theo phân công phía trên. Chỉ phần đã có bằng chứng bên dưới được tính là đã thực hiện.

### Đóng góp cụ thể

CP1: thông tin nhóm, cấu hình Git và kiểm thử setup. CP2: duyệt proposal tiêu chí, cho phép AI hoàn thiện Phiếu A và ký tiêu chí; xác nhận commit ký đã push trước eval. CP3: cho phép AI hỗ trợ trace, thiết kế/viết ba cổng, config vận hành, Phiếu B, chạy baseline/after/prepared, checkpoint và kiểm regression. Dùng AI để đọc PRD/eval card, soạn phiếu, kiểm JSON, chạy test, tạo commit. Không gán phần AI đã thực hiện thành đóng góp tự làm của các bạn; từng người cần rà soát và trình bày phần được giao. Push từ môi trường AI vẫn bị chặn mạng.

### Bằng chứng

CP1: `c4069c0` theo lịch sử hiện tại. CP2: `6118576` (`Sign acceptance criteria`), Phiếu A A1–A5, `config/acceptance_criteria.lock`. CP3: B0–B8, run base `R-base-before-20261119-155520-bde05c`, prepared `R-base-prepared-20261119-155654-107b28`, round1 hash `141ff4be`. CP4/CP5 chưa hoàn thành vì chưa có số thẻ Coach giao.

### Exit ticket

Sang tự bổ sung một điều học được và một điều còn chưa chắc sau khi hoàn tất bài; AI không viết thay trải nghiệm cá nhân.

### Sử dụng AI

Đã dùng AI trong phiên làm việc với Sang để đọc tài liệu, soạn/soát Phiếu A–B, đề xuất tiêu chí rồi chỉnh theo phê duyệt, viết cổng và config, chạy test/eval/checkpoint, rà soát độc lập và cập nhật bằng chứng. Chưa dùng AI để tuyên bố có kết quả thẻ, demo hoặc nộp LMS khi chưa thực hiện.

## NguyenThiKhanhLinh-2A202603845

### Phần việc phụ trách

Kỹ sư cổng 2; phụ trách rà soát metric offline A2 (câu 1.3), giải thích pass_rate/pass^k/pass@k, trace và phân loại lỗi B2 (2.2), hai bước tránh rò rỉ đánh giá B7.2 (2.7), behavioral test B7.3 (2.8). Chủ CP4: phân tích hai kiểu lỗi ở C2 (3.1), triển khai chỉ số mới trong `lab10/monitors.py` và C8 (3.6), kiểm regression, chuẩn bị ticket hiểm cho demo. Cùng nhóm tham gia A3, B6, B8, C1, C6 và C12.

### Đóng góp cụ thể

Sản phẩm nhóm đã có thuộc phần Linh cần tiếp nhận: metric chọn policy hiệu lực ở A2; bảng soát lỗi `T-002@55` ở B2; quy trình giữ test ẩn độc lập ở B7.2; hai ticket thử về lời khai độ trễ và PII ở B7.3. AI đã hỗ trợ soạn/chạy các phần này trong phiên với Sang; Linh cần đọc lại trace, công thức và kết luận trước khi xác nhận đóng góp cá nhân.

Phần còn làm: khi có đúng thẻ, chọn ít nhất hai ticket hỏng khác kiểu, tìm nguồn lỗi và lỗi chìm; thiết kế chỉ số có thước đo/dữ liệu/cách tính, không đọc nhãn, đăng ký MONITORS và xác nhận monitor/regression trong report. Hiện chưa thay `monitors.py`, chưa có bằng chứng CP4.

### Bằng chứng

Commit sản phẩm nhóm `b647310` (A2) và `5823095` (B2, B7.2, B7.3). Trace `T-002@55`: tracking 2 ngày, model_override 5 ngày, hoàn sai 20000 và ghi lỗi VNX; baseline `R-base-before-20261119-155520-bde05c`. Sau sửa: prepared `R-base-prepared-20261119-155654-107b28`, không ca mới hỏng. Hai trace adhoc seed11 ở B7.3 là hai lệnh riêng, không có mã eval riêng. Bằng chứng cá nhân và CP4 chờ Linh bổ sung.

### Exit ticket

Linh tự viết một điều học được và một điều còn chưa chắc sau khi thực hiện/rà soát; chưa ghi thay trải nghiệm cá nhân.

### Sử dụng AI

Các nội dung nêu trên do AI hỗ trợ trong phiên với Sang. Linh cần tự xác nhận phần đã dùng AI trực tiếp, phần đã kiểm lại và đóng góp thêm; chưa có xác nhận Linh đã trực tiếp chạy các lệnh.

## VuNgocQuynhAnh-2A202603875

### Phần việc phụ trách

Sản phẩm và kinh doanh; chủ CP2 và phần quyết định CP5. Phụ trách mục tiêu hệ thống A1 (1.1), tiêu chí/hành động/ngày xem lại A4 (1.6), bản đồ dữ liệu và drift B3 (2.3), config `business` và lý do con số B7.4 (2.9), bằng chứng kinh doanh B8. CP4: specification kiểm được ở C5 (3.2), sửa business và phân biệt giảm/ngăn ở C7 (3.5). CP5: chủ trì C12, giải thích chi phí/ROI và so v2 với v1. Cùng nhóm tham gia A3, B6, C6, các quyết định và demo.

### Đóng góp cụ thể

Sản phẩm nhóm đã có thuộc phần Anh cần tiếp nhận: A1 nối PRD/eval card Lab9; A4 gồm sàn 0,85/0,80, ba ngưỡng an toàn0, ngân sách toàn phần8000, ROI0,20 và không ùn; B3 có drift policy ngày2026-12-01; B7.4 đặt trần Finance2000000 và trần LLM1500; B8 giải thích v1 bằng report. Sang đã duyệt tiêu chí, AI hỗ trợ soạn; Anh cần rà soát và giải thích được lựa chọn trước demo, chưa ghi nhận Anh đã tự chọn hoặc tự viết các nội dung này.

Phần còn làm: đọc report đúng thẻ, xác định điều kiện kinh doanh chưa đạt, đề xuất sửa có lý do; chốt specification; viết bằng chứng và ba dòng C12 dựa trên report sau sửa. Không chọn trước v2, không sửa acceptance_criteria sau ký.

### Bằng chứng

Commit `6118576` chứa tiêu chí đã ký; `b647310` chứa A1/A4; `5823095` chứa B3/B7.4/B8 và config business. Prepared `R-base-prepared-20261119-155654-107b28`: 4274 đồng/ticket, ROI1,34,0 ca ùn, coverage1. Nhóm kho `?` có chi phí10359 đồng/ticket được ghi riêng ở B8, không giấu bằng số trung bình. CP4/C12 và bằng chứng cá nhân chờ bổ sung.

### Exit ticket

Anh tự viết một điều học được và một điều còn chưa chắc sau khi thực hiện/rà soát; chưa ghi thay trải nghiệm cá nhân.

### Sử dụng AI

AI hỗ trợ tổng hợp PRD/eval card, draft mục tiêu/tiêu chí, bản đồ dữ liệu, phân tích report và câu chữ quyết định trong phiên với Sang. Anh tự xác nhận phần dùng AI trực tiếp, lý do các ngưỡng và phần đã kiểm lại.

## NguyenThaoQuyen-2A202603895

### Phần việc phụ trách

Vận hành và pháp lý; chủ CP5 phần gom bài. Phụ trách mục tiêu Oanh/Hạnh A1 (1.2), telemetry A2 (1.4), HAZOP và checklist B4/B5 (2.4), config `operations`/`legal` cùng runbook B7.5–B7.6 (2.10). CP4: mục riêng theo thẻ C3 (miễn với S4), HAZOP C4, giả định môi trường C5 (3.3), sửa vận hành/pháp lý C7, fault tree sau sửa/risk register/checklist/runbook C9–C11 (3.7). CP5: submission.json, kiểm đầy đủ hồ sơ và giải thích người trực/runbook khi demo. Cùng nhóm tham gia pre-mortem, fault tree và quyết định.

### Đóng góp cụ thể

Sản phẩm nhóm đã có thuộc phần Quyên cần tiếp nhận: mục tiêu đối soát/người duyệt; telemetry PII; HAZOP có nhánh ngoài kỹ thuật; checklist9 nhóm có PIC; runbook1–3 và giờ cao điểm khớp config. Một người duyệt6 ca/giờ, SLA60 phút, PIC Tùng, approver Hạnh, Oanh đối soát; không tự khai thêm người để qua report. submission.json đã có4 members và v1. Các phần này do AI hỗ trợ soạn trong phiên với Sang; Quyên cần kiểm lại tính khả thi và xác nhận đóng góp thực tế.

Phần còn làm: phân tích đúng thẻ; ghi HAZOP sự cố riêng, fault tree/risk register và runbook4–5; ghép incident/v2/three_lines đúng C12 vào submission.json; phối hợp Sang chạy collect đến ĐỦ THÀNH PHẦN và kiểm bộ nộp đúng code/config cuối. Không sửa bản sao submission/docs bằng tay vì collect sẽ ghi đè.

### Bằng chứng

Commit `b647310` chứa A1/A2 và `5823095` chứa B4/B5/B7.5/B7.6, config operations/legal và metadata submission. Prepared `R-base-prepared-20261119-155654-107b28`: chờ tối đa0 phút,0 ca ùn,1 người6 ca/giờ; snapshot round1 `141ff4be`. Kênh trực nội bộ và thời gian phản ứng5 phút là quy trình đề xuất, chưa có đo production hoặc kênh thật được tạo. CP4/risk register/manifest cuối và bằng chứng cá nhân chờ bổ sung.

### Exit ticket

Quyên tự viết một điều học được và một điều còn chưa chắc sau khi thực hiện/rà soát; chưa ghi thay trải nghiệm cá nhân.

### Sử dụng AI

AI hỗ trợ soạn mục tiêu, telemetry, HAZOP, checklist, runbook, config và metadata trong phiên với Sang. Quyên tự xác nhận phần dùng AI trực tiếp, phần đã kiểm lại và nội dung bổ sung; AI không xác nhận thay việc demo hoặc nộp LMS.
