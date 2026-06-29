# Multiple PDF Chat Application

Đây là một ứng dụng web xây dựng bằng **Streamlit** và **LangChain**, cho phép bạn tải lên nhiều tài liệu PDF cùng một lúc và trò chuyện (hỏi - đáp) trực tiếp với nội dung của các file PDF đó thông qua mô hình ngôn ngữ lớn (LLM) của Google Gemini.

---

## 🚀 Tính năng nổi bật

- **Tải lên nhiều PDF cùng lúc:** Trích xuất nội dung từ nhiều tài liệu để phân tích đồng thời.
- **Xử lý ngôn ngữ tự nhiên:** Sử dụng Google Gemini Embeddings và mô hình ngôn ngữ lớn để trả lời các câu hỏi dựa trên nội dung tài liệu.
- **Bộ nhớ hội thoại (Conversational Memory):** Ghi nhớ ngữ cảnh hội thoại trước đó để trả lời thông minh và logic hơn.
- **Vector Database (FAISS):** Lưu trữ vector nhúng cục bộ giúp tìm kiếm tương đồng cực kỳ nhanh chóng.

---

## 🛠️ Yêu cầu hệ thống & Cài đặt

Dự án này chạy tốt nhất trên **Python 3.12** hoặc **3.13**.

### 1. Thiết lập môi trường ảo

**Tạo môi trường ảo `venv`:**
```bash
python -m venv venv
```

**Kích hoạt môi trường ảo `venv`:**

Chọn lệnh phù hợp với hệ điều hành và Terminal bạn đang sử dụng:

* **Trên macOS / Linux (hoặc Git Bash trên Windows):**
  ```bash
  source venv/bin/activate
  ```

* **Trên Windows (Sử dụng Command Prompt - CMD):**
  ```cmd
  venv\Scripts\activate
  ```

* **Trên Windows (Sử dụng PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

### 2. Cài đặt các thư viện phụ thuộc

Chạy lệnh sau để cài đặt tất cả các thư viện cần thiết từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Cấu hình khóa API (API Key)

Tạo một file `.env` ở thư mục gốc của dự án và thêm khóa API của bạn vào:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🏃 Hướng dẫn khởi chạy ứng dụng

Sau khi cài đặt xong thư viện và cấu hình API Key, bạn chạy lệnh sau trên terminal để khởi động ứng dụng Streamlit:

```bash
streamlit run main.py
```

Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ mặc định: `http://localhost:8501`.

---

## 📁 Cấu trúc dự án tham khảo

```text
multiple-pdf-chat/
├── app.py              # File chứa logic và giao diện ứng dụng (Streamlit UI + Logic)
├── main.py             # File khởi chạy ứng dụng chính
├── venv/               # Môi trường ảo Python
├── .env                # Lưu trữ API Key (Không đẩy lên Git)
└── README.md           # Hướng dẫn sử dụng này
```
