from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def query_data(query: str, db_path: str = "vector_store") -> str:
    try:
        embeddings = HuggingFaceEmbeddings()
        db = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
        docs = db.similarity_search(query, k=2)

        if not docs:
            return "No relevant result found."

        return docs[0].page_content
    except Exception as e:
        return f"Error while querying data: {str(e)}"
