# Multiple PDF Chat Application

Đây là một ứng dụng web xây dựng bằng **Streamlit** và **LangChain**, cho phép bạn tải lên nhiều tài liệu PDF cùng một lúc và trò chuyện (hỏi - đáp) trực tiếp với nội dung của các file PDF đó thông qua mô hình ngôn ngữ lớn (LLM) của OpenAI.

---

## 🚀 Tính năng nổi bật

- **Tải lên nhiều PDF cùng lúc:** Trích xuất nội dung từ nhiều tài liệu để phân tích đồng thời.
- **Xử lý ngôn ngữ tự nhiên:** Sử dụng OpenAI Embeddings và mô hình ngôn ngữ lớn để trả lời các câu hỏi dựa trên nội dung tài liệu.
- **Bộ nhớ hội thoại (Conversational Memory):** Ghi nhớ ngữ cảnh hội thoại trước đó để trả lời thông minh và logic hơn.
- **Vector Database (FAISS):** Lưu trữ vector nhúng cục bộ giúp tìm kiếm tương đồng cực kỳ nhanh chóng.

---

## 🛠️ Yêu cầu hệ thống & Cài đặt

Dự án này chạy tốt nhất trên **Python 3.12** hoặc **3.13**.

### 1. Thiết lập môi trường ảo

Kích hoạt môi trường ảo `venv` trong thư mục dự án:

```bash
# Trên macOS/Linux
source venv/bin/activate

# Trên Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 2. Cài đặt các thư viện phụ thuộc

Ứng dụng sử dụng các thư viện chính sau:

- `streamlit`: Xây dựng giao diện Web.
- `pypdf2`: Đọc và trích xuất text từ file PDF.
- `langchain`: Khung kết nối và xây dựng chuỗi xử lý AI.
- `faiss-cpu`: Cơ sở dữ liệu Vector lưu trữ dữ liệu nhúng cục bộ.
- `openai`: Kết nối API của OpenAI.
- `python-dotenv`: Quản lý biến môi trường.

Chạy lệnh sau để cài đặt (nếu chưa cài):

```bash
pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai huggingface_hub
```

### 3. Cấu hình khóa API (API Key)

Tạo một file `.env` ở thư mục gốc của dự án và thêm khóa API của bạn vào:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🏃 Hướng dẫn khởi chạy ứng dụng

Sau khi cài đặt xong thư viện và cấu hình API Key, bạn chạy lệnh sau trên terminal để khởi động ứng dụng Streamlit:

```bash
streamlit run app.py
```

Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ mặc định: `http://localhost:8501`.

---

## 📁 Cấu trúc dự án tham khảo

```text
multiple-pdf-chat/
├── app.py              # File chạy ứng dụng chính (Streamlit UI + Logic)
├── venv/               # Môi trường ảo Python
├── .env                # Lưu trữ API Key (Không đẩy lên Git)
└── README.md           # Hướng dẫn sử dụng này
```
