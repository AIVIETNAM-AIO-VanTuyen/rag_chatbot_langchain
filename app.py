import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs: 
        pdf_reader = PdfReader(pdf)
        print(pdf_reader)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len,
    )
    chunks = text_splitter.split_text(text)
    return chunks
    
def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vectorstore = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    # Khởi tạo mô hình ngôn ngữ lớn (Gemini 1.5 Flash)
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.3)
    
    # Khởi tạo bộ nhớ lưu trữ lịch sử hội thoại
    memory = ConversationBufferMemory(
        memory_key='chat_history', 
        return_messages=True
    )
    
    # Tạo chuỗi hội thoại truy vấn dữ liệu từ Vector store
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Vui lòng tải lên tài liệu PDF và nhấn 'Process' trước khi hỏi!")
        return

    # Gọi chuỗi hội thoại truy vấn thông tin
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

def main():
    load_dotenv()
    
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    
    # Khởi tạo session state để lưu trữ hội thoại và lịch sử qua các lượt chạy
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    
    # Hiển thị lịch sử chat trước (nằm phía trên)
    if st.session_state.chat_history:
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                with st.chat_message("user"):
                    st.write(message.content)
            else:
                with st.chat_message("assistant"):
                    st.write(message.content)

    # Nhận câu hỏi từ người dùng bằng ô nhập chat cố định ở cuối trang
    user_question = st.chat_input("Ask a question about your documents...")
    if user_question:
        handle_userinput(user_question)
        st.rerun()
    
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True) 
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                # get the text
                text_chunks = get_text_chunks(raw_text)
                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain và lưu vào session_state
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("Documents processed successfully!")
                
    