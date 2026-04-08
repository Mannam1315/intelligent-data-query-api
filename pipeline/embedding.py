from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from pipeline.preprocess import load_and_clean_data

def build_vector_store(file_path: str, save_path: str = "vector_store"):
    df = load_and_clean_data(file_path)

    documents = []
    for _, row in df.iterrows():
        content = ", ".join([f"{col}: {row[col]}" for col in df.columns])
        documents.append(Document(page_content=content))

    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(save_path)

    return f"Vector store saved to {save_path}"
