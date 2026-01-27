# lab-15-langchain-rag

**简单 RAG（检索增强生成）**

## 知识点

- 文档加载、切分、向量存储
- 检索 + 拼进 prompt，再调用 LLM 生成
- LangChain：`Document`、`RecursiveCharacterTextSplitter`、`Chroma`、`RetrievalQA`

## 运行

```bash
pip install chromadb numpy
# 完整 RAG 再安装：langchain langchain-openai langchain-text-splitters langchain-chroma
python main.py
```

- **ChromaDB-only**：仅需 `chromadb`、`numpy`，演示文档切分 → 向量存储 → 检索。
- **LangChain**：安装上述 LangChain 相关包后，会额外跑 LangChain + Chroma 检索流程。  
无 `OPENAI_API_KEY` 时用随机向量代替 embedding，不调用 LLM。
