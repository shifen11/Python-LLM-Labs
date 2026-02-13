"""
lab-15 练习题：RAG 检索
运行: python exercises.py
需安装: pip install chromadb numpy
"""


# ========== 练习 1 ==========
# 写一个函数 simple_split(text, chunk_size=20)：把字符串按 chunk_size 长度切分成列表（最后一块可不足）。对 "Python is great for ML." 测试，打印切分结果
# 期望输出: 如 ['Python is great for ', 'ML.']（或按你 chunk_size 的切分）
def exercise_1():
    pass


# ========== 练习 2 ==========
# 用 ChromaDB：创建 PersistentClient，get_or_create_collection("ex_rag")；add 两条：ids=["1","2"]，embeddings=[[1,0,0],[0,1,0]]，documents=["Python is a language.","ML needs data."]；query query_embeddings=[[1,0,0]] n_results=1，打印返回的 documents[0]
# 期望输出: ['Python is a language.']（与 [1,0,0] 最近）
def exercise_2():
    pass


# ========== 练习 3（可选，需 langchain）==========
# 若已安装 langchain：用 Document、RecursiveCharacterTextSplitter 把一段长文本切分，打印每块 page_content 长度；否则打印「未安装 langchain，跳过」
# 期望输出: 若干块的长度 或 未安装 langchain，跳过
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 若干子串的列表")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] Python is a language.")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 每块长度 或 未安装 langchain，跳过")
