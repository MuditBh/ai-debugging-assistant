import faiss
import numpy as np

# embedding size (MiniLM = 384)
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Store metadata separately
metadata_store = []


def store_error(id, embedding, metadata):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    metadata_store.append(metadata)


def search_error(query_embedding):
    query = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query, k=3)

    print("DEBUG -> indices:", indices)
    print("DEBUG -> metadata_store length:", len(metadata_store))

    results = []

    for i in indices[0]:
        if i >= 0 and i < len(metadata_store):
            results.append({"metadata": metadata_store[i]})

    # fallback
    if len(results) == 0:
        results.append({
            "metadata": {
                "error": "No exact match found",
                "solution": "Try rephrasing your error or check logs manually."
            }
        })

    return results