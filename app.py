import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

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
    


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents...")
    
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
                
                # In thông tin kiểm tra ra terminal
                print("\n=== FAISS VECTORSTORE INFO ===")
                print(f"Tong so vector (chunks) trong FAISS: {vectorstore.index.ntotal}")
                print("Mau 2 doan van ban dau tien trong docstore:")
                for doc_id, doc in list(vectorstore.docstore._dict.items())[:2]:
                    print(f"- ID: {doc_id}")
                    print(f"  Noi dung: {doc.page_content[:150]}...")
                print("==============================\n")
                
                # Hien thi thong tin len giao dien Streamlit
                st.subheader("Thông tin Vector DB (FAISS)")
                st.write(f"📊 **Tổng số lượng vector (đoạn văn):** {vectorstore.index.ntotal}")
                st.write("📝 **Xem mẫu nội dung các đoạn văn đã lưu trữ:**")
                for doc_id, doc in list(vectorstore.docstore._dict.items())[:3]:
                    with st.expander(f"Đoạn văn (ID: {doc_id[:8]}...)"):
                        st.write(doc.page_content)

    