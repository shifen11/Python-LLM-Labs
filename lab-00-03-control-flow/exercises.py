"""
lab-00-03 练习题：控制流
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 用 if/elif/else：若变量 x=70，根据 x 打印「优秀」(>=90)、「良好」(>=80)、「及格」(>=60)、「不及格」
# 期望输出: 及格（x=70 在 >=60 分支）
def exercise_1():
    x = 70
    # 你的代码
    pass


# ========== 练习 2 ==========
# 用 for 和 range(1, 6) 打印 1 到 5 的平方（每行一个：1 的平方是 1 ...）
# 期望输出: 1 的平方是 1 / 2 的平方是 4 / ... / 5 的平方是 25
def exercise_2():
    pass


# ========== 练习 3 ==========
# 用 while 实现：count 从 0 开始，每次加 1，当 count 达到 5 时停止，并打印每次的 count
# 期望输出: count = 0 到 count = 4（共 5 行）
def exercise_3():
    pass


# ========== 练习 4 ==========
# 用 for 遍历列表 [3, 7, 2, 9]，遇到大于 5 的数就 break，打印「遇到 x，停止」
# 期望输出: 遇到 7，停止（7 是第一个 >5 的）
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 及格")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 1 的平方是 1 ... 5 的平方是 25")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] count = 0 ~ 4 共 5 行")
    print("\n=== 练习 4 ===")
    exercise_4()
    print("  [期望] 遇到 7，停止")
