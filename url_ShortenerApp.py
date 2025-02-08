from flask import Flask, request, redirect, render_template_string, send_file
import sqlite3
import string, random
import os
import qrcode
from io import BytesIO

app = Flask(__name__)
DATABASE = 'urls.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    qr_code_url = ''
    short_url = ''
    if request.method == 'POST':
        original_url = request.form.get('original_url')
        if original_url:
            short_code = generate_short_code()
            conn = get_db_connection()
            exists = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,)).fetchone()
            while exists is not None:
                short_code = generate_short_code()
                exists = conn.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,)).fetchone()
            conn.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
            conn.commit()
            conn.close()
            
            short_url = f'http://localhost:5000/{short_code}'
            qr_code_url = f'/qr/{short_code}'
            message = f'<div class="text-center">URL ของคุณถูกย่อลงแล้ว: <a href="{short_url}" target="_blank">{short_url}</a></div>'
    
    return render_template_string('''
        <html>
        <head>
            <title>URL Shortener</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body class="bg-light">
            <div class="container mt-5">
                <div class="row justify-content-center">
                    <div class="col-md-6">
                        <div class="card shadow">
                            <div class="card-body text-center">
                                <h1 class="card-title">URL Shortener</h1>
                                <form method="POST">
                                    <div class="mb-3">
                                        <label for="original_url" class="form-label">กรอก URL ที่ต้องการย่อ:</label>
                                        <input type="text" class="form-control" id="original_url" name="original_url" placeholder="https://example.com" required>
                                    </div>
                                    <div class="d-grid">
                                        <button type="submit" class="btn btn-primary">ย่อ URL</button>
                                    </div>
                                </form>
                                {% if message %}
                                    <div class="alert alert-success mt-3" role="alert">
                                        {{ message|safe }}
                                        <div class="text-center mt-3">
                                            <img src="{{ qr_code_url }}" alt="QR Code" class="img-fluid">
                                        </div>
                                    </div>
                                {% endif %}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
    ''', message=message, qr_code_url=qr_code_url)

@app.route('/<short_code>')
def redirect_short_url(short_code):
    conn = get_db_connection()
    url_entry = conn.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,)).fetchone()
    conn.close()
    if url_entry:
        return redirect(url_entry['original_url'])
    else:
        return 'ไม่พบ URL ที่ต้องการย่อ', 404

@app.route('/qr/<short_code>')
def generate_qr(short_code):
    short_url = f'http://localhost:5000/{short_code}'
    qr = qrcode.make(short_url)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
