"""
lab-13 练习题：流式输出与 Token
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 写一个函数 rough_token_count(text)：英文按约 4 字符/token，中文按约 1.5 字符/token 估算 token 数，返回整数。对 "Hello world" 和 "你好世界" 分别打印
# 期望输出: 约 3 和 约 4（或你实现的公式结果）
def exercise_1():
    pass


# ========== 练习 2 ==========
# 模拟流式：列表 chunks = ["Hi", ", ", "this ", "is ", "stream."]，用 for 循环逐块 print(..., end="", flush=True)，最后打印一行「token 约 x」
# 期望输出: Hi, this is stream. 和 一行 token 约 x
def exercise_2():
    pass


# ========== 练习 3（可选，需 OPENAI_API_KEY）==========
# 若有 API Key，用 openai 客户端发一条非流式 chat completion，打印返回的 content；否则打印「跳过（需 KEY）」
# 期望输出: 一段文本 或 跳过（需 KEY）
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 两个整数（token 估算）")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] Hi, this is stream. 和 token 约 x")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 文本内容 或 跳过（需 KEY）")
