# URL Shortener with Flask and QR Code | ตัวย่อลิงก์ด้วย Flask พร้อม QR Code

## Overview | ภาพรวม
This project is a simple URL shortener built with Flask. It allows users to enter a long URL and generate a shortened URL, along with a QR code for easy access.

โปรเจกต์นี้เป็นตัวย่อลิงก์ที่พัฒนาด้วย Flask ช่วยให้ผู้ใช้สามารถป้อน URL ยาว ๆ แล้วสร้างลิงก์ย่อพร้อม QR Code เพื่อให้เข้าถึงได้ง่ายขึ้น

## Features | คุณสมบัติ
- Shorten long URLs into unique short codes
- Store URLs in an SQLite database
- Generate QR codes for shortened URLs
- Redirect users to the original URL when they visit the shortened link
- Web interface using Bootstrap

- ย่อลิงก์ให้เป็นรหัสสั้น ๆ ที่ไม่ซ้ำกัน
- บันทึก URL ไว้ในฐานข้อมูล SQLite
- สร้าง QR Code สำหรับลิงก์ที่ถูกย่อ
- เมื่อลิงก์สั้นถูกเข้าถึง ระบบจะเปลี่ยนเส้นทางไปยัง URL ต้นฉบับ
- มีอินเทอร์เฟซแบบเว็บที่ใช้ Bootstrap

## Requirements | ความต้องการของระบบ
Make sure you have the following installed:
ตรวจสอบให้แน่ใจว่าคุณติดตั้งสิ่งต่อไปนี้แล้ว:
- Python 3
- Flask
- SQLite
- qrcode
- Pillow (for QR code image generation) | Pillow (ใช้สำหรับสร้าง QR Code เป็นภาพ)

## Installation | การติดตั้ง
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/url-shortener.git
   cd url-shortener
   ```

   โคลนโปรเจกต์:
   ```bash
   git clone https://github.com/your-repo/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   สร้าง Virtual Environment (แนะนำให้ใช้):
   ```bash
   python -m venv venv
   source venv/bin/activate  # บน Windows ใช้ `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install flask qrcode[pil]
   ```

   ติดตั้งไลบรารีที่จำเป็น:
   ```bash
   pip install flask qrcode[pil]
   ```

4. Run the application:
   ```bash
   python url_ShortenerApp.py
   ```

   รันแอปพลิเคชัน:
   ```bash
   python url_ShortenerApp.py
   ```

5. Open your browser and go to:
   ```
   http://localhost:5000
   ```

   เปิดเบราว์เซอร์และไปที่:
   ```
   http://localhost:5000
   ```

## Usage | วิธีการใช้งาน
1. Enter a URL into the input field and click the "Shorten URL" button.
2. The shortened URL will be displayed along with a QR code.
3. Click the shortened URL or scan the QR code to access the original URL.
4. To visit the original URL, enter `http://localhost:5000/<short_code>` in your browser.

1. ป้อน URL ที่ต้องการย่อในช่องป้อนข้อมูล แล้วกดปุ่ม "ย่อ URL"
2. ระบบจะแสดงลิงก์ที่ถูกย่อและ QR Code
3. สามารถคลิกลิงก์หรือสแกน QR Code เพื่อเข้าถึง URL ต้นฉบับได้
4. หากต้องการเข้าถึง URL ต้นฉบับผ่านเบราว์เซอร์ ให้ใช้ `http://localhost:5000/<short_code>`

## Project Structure | โครงสร้างโปรเจกต์
```
url-shortener/
│── url_ShortenerApp.py  # Main Flask application | โค้ดหลักของแอปพลิเคชัน Flask
│── urls.db               # SQLite database (auto-created) | ฐานข้อมูล SQLite (สร้างอัตโนมัติ)
│── README.md             # Project documentation | เอกสารคู่มือโปรเจกต์
│── requirements.txt      # List of dependencies | รายชื่อไลบรารีที่จำเป็น
```

## Notes | หมายเหตุ
- If you encounter `ModuleNotFoundError: No module named 'qrcode'`, install it using:
  ```bash
  pip install qrcode[pil]
  ```

  หากพบข้อผิดพลาด `ModuleNotFoundError: No module named 'qrcode'` ให้ติดตั้งด้วยคำสั่ง:
  ```bash
  pip install qrcode[pil]
  ```

- You can modify the database name in the `DATABASE` variable inside `url_ShortenerApp.py`.

  สามารถเปลี่ยนชื่อฐานข้อมูลได้ในตัวแปร `DATABASE` ในไฟล์ `url_ShortenerApp.py`

## License | ลิขสิทธิ์
This project is open-source. Feel free to modify and use it for personal or commercial projects.

โปรเจกต์นี้เป็นโอเพนซอร์ส สามารถแก้ไขและนำไปใช้ได้ทั้งในเชิงส่วนตัวและเชิงพาณิชย์

