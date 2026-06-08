from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

documents = []

index = faiss.IndexFlatL2(384)


def reset_vector_db():

    global index
    global documents

    index = faiss.IndexFlatL2(384)
    documents = []


def add_to_vector_db(chunks):

    embeddings = embedding_model.encode(chunks)

    embeddings = np.array(
        embeddings
    ).astype("float32")

    index.add(embeddings)

    documents.extend(chunks)


def search_query(query, k=3):

    if len(documents) == 0:
        return []

    query_embedding = embedding_model.encode([query])

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        min(k, len(documents))
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):
            results.append(documents[idx])

    return results