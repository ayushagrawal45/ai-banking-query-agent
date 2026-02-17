from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_store(text):
    chunks = [line for line in text.split("\n") if line.strip()]
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)
    return index, chunks

def search(query, index, chunks, k=3):
    query_embedding = model.encode([query])
    _, results = index.search(query_embedding, k)
    return [chunks[i] for i in results[0]]
