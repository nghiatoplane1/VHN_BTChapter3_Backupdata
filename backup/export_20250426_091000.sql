-- Thêm dữ liệu vào bảng ThucDon01
INSERT INTO ThucDon (MaMonAn, TenMonAn, GiaTien, MoTa, HinhAnh, SoLuongTon, MaNguoiDung)
VALUES
    ('M001', 'Cơm gà', 50000, 'Cơm trắng kèm với gà chiên giòn', 'https://example.com/com-ga.jpg', 20, 'U003'),
    ('M002', 'Bún chả', 60000, 'Bún kèm với thịt nướng và nước chấm', 'https://example.com/bun-cha.jpg', 15, 'U003'),
    ('M003', 'Phở bò', 70000, 'Phở với thịt bò và rau gia vị', 'https://example.com/pho-bo.jpg', 25, 'U003'),
    ('M004', 'Bánh mì', 20000, 'Bánh mì kẹp với thịt, pate và rau', 'https://example.com/banh-mi.jpg', 30, 'U003');

-- Thêm dữ liệu vào bảng DonHang01
INSERT INTO DonHang (MaDonHang, MaNguoiDung, MaBan, NgayDat, NgaySuDung, TongTien, TrangThai)
VALUES
    ('D001', 'U001', 'B001', '2023-04-15', '2023-04-15 01:00:00', 100000, 'Đang xử lý'),
    ('D002', 'U004', 'B004', '2023-04-16', '2023-04-16 01:00:00', 180000, 'Đã thanh toán'),
    ('D003', 'U001', 'B001', '2023-04-17', '2023-04-20 00:00:00', 120000, 'Đang xử lý'),
    ('D004', 'U002', 'B002', '2023-04-18', '2023-04-18 01:00:00', 150000, 'Đã thanh toán');

-- Thêm dữ liệu vào bảng ChiTietDonHang01
INSERT INTO ChiTietDonHang (MaChiTiet, MaDonHang, MaMonAn, SoLuong, DonGia)
VALUES
    ('CT001', 'D001', 'M001', 2, 50000),
    ('CT002', 'D001', 'M002', 1, 60000),
    ('CT003', 'D002', 'M003', 2, 70000),
    ('CT004', 'D002', 'M004', 3, 20000),
    ('CT005', 'D003', 'M001', 1, 50000),
    ('CT006', 'D003', 'M002', 2, 60000),
    ('CT007', 'D004', 'M003', 1, 70000),
    ('CT008', 'D004', 'M004', 2, 20000);