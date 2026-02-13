"""
lab-14 练习题：向量数据库（FAISS / ChromaDB）
运行: python exercises.py
需安装: pip install numpy faiss-cpu chromadb
"""


# ========== 练习 1（FAISS）==========
# 用 faiss.IndexFlatL2(2) 创建 2 维索引；add 三个向量 [[0,1],[1,0],[1,1]]；用 search([[0,1]], 2) 查询最近 2 个，打印索引和距离
# 期望输出: 最近的是 [0,1] 自己（距离 0），次近是 [1,1]（距离 1.0）
def exercise_1():
    pass


# ========== 练习 2（ChromaDB）==========
# 用 chromadb.PersistentClient(path="./ex_chroma")；get_or_create_collection("ex")；add(ids=["a","b"], embeddings=[[1,0],[0,1]], documents=["doc A","doc B"])；query(query_embeddings=[[1,0]], n_results=1)，打印返回的 ids 和 documents
# 期望输出: ids 含 'a'，documents 含 'doc A'
def exercise_2():
    pass


# ========== 练习 3 ==========
# 对上述 ChromaDB collection，再 add 一条 id="c", embedding=[0.9, 0.1], document="doc C"，再次 query [[1,0]] n_results=2，打印
# 期望输出: 2 条，含 a 和 c（与 [1,0] 最近）
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 索引 [0,1] 或 [0,2]，距离 0 和 1.0")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] ids 含 'a'，documents 含 'doc A'")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 2 条结果含 a 和 c")
