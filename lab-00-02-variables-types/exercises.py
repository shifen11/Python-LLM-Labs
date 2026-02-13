"""
lab-00-02 练习题：变量与基本数据类型
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 定义变量 a=10, b=3.14, c="hello", d=True，并依次打印它们的类型（用 type(...).__name__）
# 期望输出: int / float / str / bool（顺序对应 a,b,c,d）
def exercise_1():
    a=10
    b=3.14
    c="hello"
    d=True


    atype= {type(a).__name__}
    btype= {type(b).__name__}
    ctype= {type(c).__name__}
    dtype= {type(d).__name__}
    print(f"a的数据类型是{atype}")
    print(f"b的数据类型是{btype}")
    print(f"c的数据类型是{ctype}")
    print(f"d的数据类型是{dtype}")
# ========== 练习 2 ==========
# 将字符串 "42" 转成整数，将整数 100 转成字符串，打印转换后的结果
# 期望输出: 42 和 '100'（或 "100"）
def exercise_2():
    a=42



# ========== 练习 3 ==========
# 写出 bool(0)、bool("")、bool(1)、bool("x") 的值并打印，验证「空为 False」
# 期望输出: False False True True
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] int, float, str, bool")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 42 和 '100'")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] False False True True")
