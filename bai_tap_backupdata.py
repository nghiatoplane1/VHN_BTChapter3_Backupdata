import os
import shutil
import smtplib
import schedule
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from security.env import app_password, sender_email, receiver_email

# Gửi email
def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print(f"Gửi email thành công đến {receiver}")
    except Exception as e:
        print(f"Gửi email thất bại: {e}")

# Thực hiện backup và gửi mail
def backup_and_notify():
    src_dir = './chapter3'
    backup_dir = './chapter3/backup' 

    # Tạo thư mục backup nếu chưa tồn tại
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    success_files = []
    failed_files = []

    print(f"Kiểm tra các file trong thư mục: {os.getcwd()}")
    print(f"Các file hiện có: {os.listdir(src_dir)}")

    for file in os.listdir(src_dir):
        if file.endswith('.sql') or file.endswith('.sqlite3'):
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_name = f"{os.path.splitext(file)[0]}_{timestamp}{os.path.splitext(file)[1]}"
                src_path = os.path.join(src_dir, file)
                dst_path = os.path.join(backup_dir, new_name)
                print(f"Đang sao chép từ {src_path} đến {dst_path}")
                shutil.copy2(src_path, dst_path)
                success_files.append(file)
                print(f"Backup thành công: {file}")
            except Exception as e:
                failed_files.append((file, str(e)))
                print(f"Backup thất bại: {file} - Lỗi: {e}")

    # Tạo nội dung email
    if success_files:
        body = "Backup thành công các file:\n" + "\n".join(success_files)
    else:
        body = "Không có file nào được backup."

    if failed_files:
        body += "\n\nMột số file backup thất bại:\n"
        for file, err in failed_files:
            body += f"- {file}: {err}\n"

    send_email(sender_email, receiver_email, "Báo cáo backup lúc 00:00", body, app_password)

# Lên lịch chạy lúc 00:00 mỗi ngày
schedule.every().day.at("00:00").do(backup_and_notify)

print("Đang chờ đến giờ để thực hiện backup tự động...")

while True:
    schedule.run_pending()
    time.sleep(1)