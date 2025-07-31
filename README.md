# 📜 Chatbot Lịch Sử Việt Nam (GROQ API)

Chatbot tương tác với các nhân vật lịch sử Việt Nam nổi tiếng! Trò chuyện với Hồ Chí Minh, Lý Thường Kiệt, Trần Hưng Đạo và nhiều hơn nữa. Sử dụng mô hình ngôn ngữ từ GROQ (LLaMA 3) và giao diện Streamlit.

## 🎭 Nhân vật có sẵn

- 🌟 **Hồ Chí Minh**: Chủ tịch Hồ Chí Minh, lãnh tụ cách mạng
- 🏛️ **Lý Thường Kiệt**: Danh tướng triều Lý, tác giả "Nam quốc sơn hà"  
- ⚔️ **Trần Hưng Đạo**: Đại tướng chống quân Mông Nguyên
- 📚 **Học giả Lịch sử**: Nhà nghiên cứu khách quan

---

## 🚀 Cách chạy local

### 1. Giải nén & chuyển vào thư mục

```bash
unzip chatbot_lich_su_groq.zip
cd chatbot_lich_su_groq
```

### 2. (Tuỳ chọn) Tạo môi trường ảo

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Cài thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 4. Thêm API key GROQ

Tạo file `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "gsk_live_your_real_groq_api_key_here"
```

Lấy key tại: https://console.groq.com/keys

### 5. Chạy app

```bash
streamlit run app.py
```

Sau đó truy cập: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Mô hình sử dụng

- `llama3-8b-8192` từ GROQ
- Trả lời ngắn gọn, thân thiện, dễ hiểu

---

## 📝 Tùy chỉnh

- Câu hỏi mẫu trong `data.json`
- API key trong `.streamlit/secrets.toml`
- Giao diện chính trong `app.py`

---

## 📦 Yêu cầu

- Python 3.8+
- Internet để truy cập API của GROQ

---

## 📬 Liên hệ


