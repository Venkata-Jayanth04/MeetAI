from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer(
    'sentence-transformers/all-MiniLM-L6-v2'
)

documents = []

index = faiss.IndexFlatL2(384)

def add_documents(text_chunks):

    global documents

    embeddings = model.encode(text_chunks)

    index.add(np.array(embeddings).astype("float32"))

    documents.extend(text_chunks)

def search(query):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype("float32"),
        k=3
    )

    results = [documents[i] for i in I[0]]

    return results