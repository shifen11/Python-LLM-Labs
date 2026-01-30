"""
lab-14-vector-databases: 向量数据库（FAISS / ChromaDB）

运行时会展示：FAISS 内存索引 L2 最近邻、ChromaDB 持久化 collection 的 add/query，以及「何时用哪种」。
"""
import numpy as np

print("=== 1. FAISS（内存向量索引）===\n")
print("  >>> [说明] IndexFlatL2(dim) 为暴力 L2 最近邻；.add(向量)、.search(查询向量, k)")


def demo_faiss():
    try:
        import faiss
    except ImportError:
        print("  faiss-cpu 未安装，跳过 FAISS demo")
        return
    dim = 4
    index = faiss.IndexFlatL2(dim)
    xs = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0.9, 0.1, 0, 0]], dtype=np.float32)
    index.add(xs)
    q = np.array([[1, 0, 0, 0]], dtype=np.float32)
    D, I = index.search(q, 2)
    print(f"  >>> [触发] 查询向量 [1,0,0,0] 的 top2 索引: {I[0].tolist()}, L2 距离: {D[0].tolist()}")
    print("  >>> [小结] FAISS 适合纯内存、大规模向量检索\n")


demo_faiss()

print("=== 2. ChromaDB（持久化 + 可选文档存储）===\n")
print("  >>> [说明] PersistentClient(path) 持久化；get_or_create_collection；add(ids, embeddings, documents)")


def demo_chromadb():
    try:
        import chromadb
    except ImportError:
        print("  chromadb 未安装，跳过 ChromaDB demo")
        return
    client = chromadb.PersistentClient(path="./chroma_data")
    coll = client.get_or_create_collection("lab14", metadata={"hnsw:space": "cosine"})
    coll.add(
        ids=["a", "b", "c"],
        embeddings=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        documents=["first doc", "second doc", "third doc"],
    )
    out = coll.query(query_embeddings=[[1, 0, 0]], n_results=2)
    print(f"  >>> [触发] 查询 [1,0,0] 的 top2 ids: {out['ids'][0]}, docs: {out['documents'][0]}")
    print("  >>> [小结] ChromaDB 带持久化与文档，适合 RAG 等场景\n")


demo_chromadb()
