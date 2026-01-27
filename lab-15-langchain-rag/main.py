"""
lab-15-langchain-rag: 简单 RAG 检索流程
支持 LangChain 完整链，或仅 ChromaDB 的降级 demo。
"""


def _split_simple(texts: list[str], chunk_size: int = 50):
    """简单按长度切分，无 LangChain 时用"""
    out = []
    for i, t in enumerate(texts):
        for j in range(0, len(t), chunk_size):
            out.append((t[j : j + chunk_size], f"doc{i}"))
    return out


def demo_rag_chromadb_only():
    """仅 ChromaDB：文档切分 -> 存入 -> 检索（无 LangChain）"""
    try:
        import chromadb
        import numpy as np
    except ImportError as e:
        print("Install: chromadb numpy →", e)
        return

    raw = [
        "Python is a programming language. It is used for ML and AI.",
        "FastAPI is a web framework for building APIs with Python.",
        "Vector databases store embeddings for similarity search.",
    ]
    chunks = _split_simple(raw)
    texts = [c[0] for c in chunks]
    # 用简单确定性向量代替 embed（仅 demo）
    dim = 8
    np.random.seed(42)
    embs = np.random.randn(len(texts), dim).astype(np.float32).tolist()
    ids = [f"c{i}" for i in range(len(texts))]

    client = chromadb.PersistentClient(path="./chroma_rag_simple")
    coll = client.get_or_create_collection("rag", metadata={"hnsw:space": "cosine"})
    coll.add(ids=ids, embeddings=embs, documents=texts)

    q_emb = np.random.randn(1, dim).astype(np.float32).tolist()
    out = coll.query(query_embeddings=q_emb, n_results=2)
    print("RAG retrieve (ChromaDB-only, top 2):")
    for i, doc in enumerate(out["documents"][0]):
        print(f"  [{i+1}] {doc[:60]}...")
    print("(Use LangChain + OpenAI for full RAG with LLM.)")


def demo_rag_langchain():
    """LangChain：Document + TextSplitter + Chroma + 检索"""
    try:
        from langchain_core.documents import Document
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from langchain_chroma import Chroma
        from langchain_openai import OpenAIEmbeddings
    except ImportError as e:
        print("LangChain not available:", e)
        return

    raw = [
        "Python is a programming language. It is used for ML and AI.",
        "FastAPI is a web framework for building APIs with Python.",
        "Vector databases store embeddings for similarity search.",
    ]
    docs = [Document(page_content=t, metadata={"source": f"doc{i}"}) for i, t in enumerate(raw)]
    splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
    splits = splitter.split_documents(docs)

    try:
        emb = OpenAIEmbeddings()
        persist_dir = "./chroma_rag"
    except Exception:
        import numpy as np
        from langchain_core.embeddings import Embeddings

        class RandomEmbeddings(Embeddings):
            def embed_documents(self, texts):
                return [np.random.randn(8).tolist() for _ in texts]

            def embed_query(self, text):
                return np.random.randn(8).tolist()

        emb = RandomEmbeddings()
        persist_dir = "./chroma_rag_mock"

    vs = Chroma.from_documents(splits, emb, persist_directory=persist_dir)
    ret = vs.similarity_search("What is FastAPI?", k=2)
    print("RAG retrieve (LangChain + Chroma, top 2):")
    for i, d in enumerate(ret):
        print(f"  [{i+1}] {d.page_content[:60]}...")
    print("(Use RetrievalQA chain for full RAG with LLM.)")


if __name__ == "__main__":
    print("=== ChromaDB-only RAG 检索 ===")
    demo_rag_chromadb_only()
    print("\n=== LangChain RAG 检索（若已安装）===")
    demo_rag_langchain()
