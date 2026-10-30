# Ghi chú đối chiếu repository tham khảo

Repository tham khảo do người dùng cung cấp dưới dạng ZIP:
`BTL_Warehouse_Management_-_Reorder_Sytem_Group2_YCPM-main.zip`

Đã kiểm tra cấu trúc repository tham khảo. Gói bài nộp có:
- mã nguồn chia theo `src/Module1` đến `src/Module4`,
- thư mục `datasets/`, `diagrams/`, `output/`, `workbooks/`,
- `TestCase.csv` và `Traceability_matrix.csv`,
- test tự động, test runner, dependency files, README và log kiểm thử.

UniCourse sử dụng cách tổ chức hồ sơ và bằng chứng tương tự: workbook nguồn, CSV dữ liệu, sơ đồ, test case, traceability matrix, mã nguồn, test runner và log. Do workbook UniCourse mô tả 8 module, thư mục `src/MOD-01` đến `src/MOD-08` cung cấp bản đồ phạm vi và liên kết đến phần mã nguồn/test thực thi trong `backend/` và `tests/`.

**Chỉ mượn cách tổ chức gói bài nộp.** Không sao chép nghiệp vụ kho hàng, tồn kho, nhà cung cấp, đặt hàng hoặc logic đặc thù của repository tham khảo. UniCourse được triển khai theo mô hình dữ liệu và yêu cầu trong workbook riêng.

Gói này không bao gồm frontend website. Mã nguồn hiện tại là backend/API theo công nghệ được nêu trong workbook và phần test code: FastAPI, SQLAlchemy, pytest; SQLite in-memory chỉ dùng cho kiểm thử.
