"""
lab-00-08 练习题：异常处理
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 用 try/except：尝试将 "abc" 转为 int，捕获 ValueError 并打印「转换失败」
# 期望输出: 转换失败
def exercise_1():
    pass


# ========== 练习 2 ==========
# 定义函数 safe_divide(a, b)，在 try 中返回 a/b；除零时 except ZeroDivisionError 返回 None
# 期望输出: 5.0、None、None（对应 10/2、10/0、10/'a'）
def exercise_2():
    pass


# ========== 练习 3 ==========
# 用 try/except Exception as e：尝试访问 [1,2,3][10]，捕获后打印异常类型名和 e
# 期望输出: IndexError 和 list index out of range
def exercise_3():
    pass


# ========== 练习 4 ==========
# 定义函数 check_positive(n)，若 n<=0 则 raise ValueError("n 必须为正数")，否则返回 n。调用 check_positive(-1) 并用 try/except 打印错误信息
# 期望输出: 捕获到错误信息（如 n 必须为正数）
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 转换失败")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 5.0 / None / None")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] IndexError: list index out of range")
    print("\n=== 练习 4 ===")
    exercise_4()
    print("  [期望] 错误信息（n 必须为正数）")
