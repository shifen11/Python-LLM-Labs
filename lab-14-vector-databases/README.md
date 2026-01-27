# lab-14-vector-databases

**向量数据库：FAISS / ChromaDB 增删改查**

## 知识点

- 向量存储、相似度检索（本 demo 用随机向量演示）
- ChromaDB：持久化、collection、`add` / `query`
- FAISS：`IndexFlatL2`、`add`、`search`

## 运行

```bash
pip install chromadb faiss-cpu numpy
python main.py
```

ChromaDB 数据会写入 `./chroma_data`（可在 `.gitignore` 中排除）。
