"""
lab-14-vector-databases: ChromaDB / FAISS 增删改查
"""
import numpy as np


def demo_faiss():
    """FAISS：内存向量索引，L2 最近邻"""
    try:
        import faiss
    except ImportError:
        print("faiss-cpu not installed, skip FAISS demo")
        return
    dim = 4
    index = faiss.IndexFlatL2(dim)
    xs = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0.9, 0.1, 0, 0]], dtype=np.float32)
    index.add(xs)
    q = np.array([[1, 0, 0, 0]], dtype=np.float32)
    D, I = index.search(q, 2)
    print("FAISS: query [1,0,0,0] -> indices", I[0].tolist(), "L2 dists", D[0].tolist())


def demo_chromadb():
    """ChromaDB：持久化 collection，add / query"""
    try:
        import chromadb
    except ImportError:
        print("chromadb not installed, skip ChromaDB demo")
        return
    client = chromadb.PersistentClient(path="./chroma_data")
    coll = client.get_or_create_collection("lab14", metadata={"hnsw:space": "cosine"})
    coll.add(
        ids=["a", "b", "c"],
        embeddings=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        documents=["first doc", "second doc", "third doc"],
    )
    out = coll.query(query_embeddings=[[1, 0, 0]], n_results=2)
    print("ChromaDB: query [1,0,0] -> ids", out["ids"][0], "docs", out["documents"][0])


if __name__ == "__main__":
    print("=== FAISS ===")
    demo_faiss()
    print("\n=== ChromaDB ===")
    demo_chromadb()
