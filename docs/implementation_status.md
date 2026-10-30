# Implementation status and baseline differences

Tài liệu này phân biệt **trạng thái ghi trong workbook gốc** với **phần mã nguồn được cung cấp trong ZIP**. Workbook được giữ nguyên trong `workbooks/`; các ghi chú dưới đây không sửa ngược dữ liệu gốc.

## Các chức năng được bổ sung so với trạng thái baseline

| Requirement | Trạng thái trong workbook | Phần hiện có trong gói mã nguồn |
|---|---|---|
| REQ-008 – Cancel Registration | Not Implemented | Có API hủy đăng ký của chính sinh viên; cập nhật trạng thái và trả chỗ về lớp. |
| REQ-009 – Create Class | Not Implemented | Có API quản trị tạo lớp học phần. |
| REQ-010 – Edit Class Information | Not Implemented | Có API quản trị cập nhật thông tin lớp; không cho giảm sức chứa xuống thấp hơn số lượng đã ghi danh. |
| REQ-011 – Cancel Class | Not Implemented | Có API quản trị hủy lớp và chặn đăng ký mới. |
| REQ-012 – Notify Students of Class Cancellation | Not Implemented | Khi hủy lớp, tạo thông báo cho các sinh viên đang có đăng ký xác nhận. |
| REQ-014 – View Notifications | Not Implemented | Có API lấy danh sách thông báo theo người dùng đã xác thực. |
| REQ-019 – View Student Dashboard | Implemented | Có API dashboard trả thông tin sinh viên và các đăng ký đã xác nhận của chính sinh viên. |

## Phần còn một phần / giới hạn

- **REQ-013 – User Role Management:** workbook đánh dấu Partial. Gói này thực thi kiểm soát quyền Student, Lecturer và Administrator ở các API tương ứng, nhưng chưa triển khai đầy đủ chức năng quản trị vòng đời tài khoản/vai trò.
- **NFR-001 đến NFR-003:** chưa có bằng chứng kiểm thử tải, 500 người dùng đồng thời, p95 ≤ 2 giây hoặc availability ≥ 99%.
- **NFR-010:** audit logging được workbook ghi là khuyến nghị khi bật; gói chưa triển khai đầy đủ bảng/log kiểm toán và chính sách lưu trữ.
- **Production database:** workbook nêu DBMS production phụ thuộc triển khai; SQLite in-memory chỉ là cấu hình test.

## Phạm vi kiểm thử hiện có

Bộ test tự động bao phủ các luồng nghiệp vụ và API được liệt kê trong `tests/`. Kết quả test cục bộ không đồng nghĩa tất cả NFR hoặc quy trình triển khai production đã được nghiệm thu.
