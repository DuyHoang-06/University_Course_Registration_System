# UniCourse – Online Course Registration System

Bài tập lớn môn **Software Requirements**. Repository này cung cấp backend/API, mô hình dữ liệu, logic nghiệp vụ, kiểm thử tự động và hồ sơ truy vết yêu cầu cho hệ thống đăng ký học phần UniCourse.

## 1. Phạm vi

Hệ thống được tổ chức theo 8 module trong workbook:

1. **MOD-01 – Authentication & Account Management:** đăng ký tài khoản sinh viên, đăng nhập, đăng xuất, quản lý phiên.
2. **MOD-02 – Course Catalogue & Class Information:** truy vấn lớp học phần mở theo chương trình đào tạo và xem thông tin lớp.
3. **MOD-03 – Registration & Validation:** đăng ký học phần và kiểm tra trùng, sĩ số, trạng thái lớp, chương trình đào tạo, xung đột lịch.
4. **MOD-04 – Student Self-Service:** hồ sơ sinh viên, danh sách đăng ký và hủy đăng ký của chính sinh viên.
5. **MOD-05 – Lecturer Workspace:** xem các lớp được phân công cho giảng viên đang đăng nhập.
6. **MOD-06 – Administration & Class Management:** thống kê, tạo, chỉnh sửa và hủy lớp học phần.
7. **MOD-07 – Notification Management:** tạo thông báo sau đăng ký/hủy lớp và xem thông báo theo người nhận.
8. **MOD-08 – Security & Data Integrity:** phân quyền theo vai trò, bảo vệ endpoint, giới hạn dữ liệu theo chủ sở hữu và giao dịch dữ liệu.

**Lưu ý phạm vi:** Đây là gói triển khai backend/API. Không bao gồm website frontend hoặc giao diện người dùng hoàn chỉnh. API có thể được kiểm tra qua Swagger tại `/docs` khi chạy cục bộ.

## 2. Công nghệ

- Python 3.10+
- FastAPI
- SQLAlchemy 2.x
- Pydantic
- Pytest + HTTPX
- SQLite in-memory dùng trong kiểm thử; DBMS production được cấu hình qua `DATABASE_URL` và không mặc định là SQLite.

## 3. Cài đặt và chạy

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

python -m pip install -r requirements-test.txt
cp .env.example .env
python -m backend.seed
uvicorn backend.main:app --reload
```

Các địa chỉ kiểm tra:
- Swagger API: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

Tài khoản demo:
| Vai trò | Email | Mật khẩu |
|---|---|---|
| Student | student@example.com | Student123! |
| Lecturer | lecturer@example.com | Lecturer123! |
| Administrator | admin@example.com | Admin123! |

Chỉ dùng tài khoản demo cho môi trường học tập cục bộ. Thay `SECRET_KEY`, mật khẩu và cấu hình cookie/HTTPS trước khi triển khai.

## 4. Chạy kiểm thử

```bash
python -m pytest -v
python scripts/run_tests.py
```

Log và JUnit XML được lưu tại `output/test_logs/`. Kiểm thử tự động tập trung vào xác thực, phân quyền, các quy tắc đăng ký, xung đột lịch, sức chứa, hủy đăng ký, dữ liệu được lưu và API theo vai trò.

Các NFR như 500 người dùng đồng thời, độ sẵn sàng 99% và thời gian phản hồi p95 ≤ 2 giây chưa được xác nhận bằng kiểm thử tải/giám sát triển khai. Không xem kết quả unit/API test là bằng chứng đạt các chỉ tiêu này.

## 5. Cấu trúc repository

```text
UniCourse_Source_Package/
├── backend/
│   ├── routers/             # API theo vai trò/chức năng
│   ├── services/            # Nghiệp vụ đăng ký và quản lý lớp
│   ├── main.py              # FastAPI application
│   ├── models.py            # SQLAlchemy entities
│   ├── schemas.py           # Request/response validation
│   ├── security.py          # Password hashing, session, role guards
│   └── database.py
├── src/                     # Bản đồ phạm vi 8 module theo workbook
├── tests/                   # Pytest unit/integration/API tests
├── datasets/                # Dữ liệu yêu cầu, module, test và dữ liệu mẫu
├── diagrams/                # Sơ đồ kiến trúc, DFD, use case, trạng thái
├── docs/                    # Phạm vi, API, test strategy, mapping repo mẫu
├── output/test_logs/        # Kết quả kiểm thử đã chạy
├── scripts/                 # Test runner
├── workbooks/               # Workbook gốc do người dùng cung cấp
├── TestCase.csv
├── Traceability_matrix.csv
├── requirements.txt
└── requirements-test.txt
```

## 6. Các quy tắc nghiệp vụ trọng tâm

- Chỉ sinh viên đã xác thực mới được đăng ký lớp.
- Lớp phải ở trạng thái mở và còn chỗ.
- Không cho phép đăng ký trùng cùng lớp.
- Chương trình đào tạo của lớp phải phù hợp với sinh viên.
- Không cho phép hai lớp đã xác nhận bị trùng lịch; hai khoảng thời gian tiếp giáp được chấp nhận.
- Khi đăng ký thành công, bản ghi đăng ký, số lượng đã ghi danh và thông báo xác nhận được xử lý trong cùng transaction.
- Sinh viên chỉ xem/hủy đăng ký của chính mình.
- Giảng viên chỉ xem các lớp được phân công.
- Các thao tác quản trị yêu cầu vai trò administrator.
- Hủy lớp tạo thông báo cho sinh viên đã đăng ký.

## 7. Giới hạn cần lưu ý

- Đây là backend/API, không phải sản phẩm website hoàn chỉnh.
- Kiểm thử SQLite in-memory không thay thế kiểm thử transaction/locking trên DBMS triển khai thật.
- Cấu hình session hiện phục vụ demo cục bộ; production cần HTTPS, secure cookie, CSRF protection, quản lý secret và chính sách session phù hợp.
- Audit logging NFR-010 được mô tả trong workbook nhưng chưa triển khai đầy đủ.
- NFR tải, độ sẵn sàng và khả năng bảo trì cần kiểm thử/đánh giá riêng trước khi tuyên bố đạt.
- Không tích hợp hệ thống SIS, email/SMS gateway hoặc hạ tầng production.

## 8. Tài liệu tham chiếu

- `workbooks/course_registration_system.xlsx`: workbook yêu cầu gốc.
- `datasets/requirements.csv`, `datasets/modules.csv`, `datasets/use_cases.csv`: dữ liệu trích xuất từ workbook.
- `TestCase.csv`: danh mục test case.
- `Traceability_matrix.csv`: liên kết requirement – use case – test case.
- `src/MOD-01` đến `src/MOD-08`: mapping 8 module sang mã nguồn/API/test.
- `docs/implementation_status.md`: phân biệt trạng thái workbook gốc và phần triển khai trong ZIP.
