"""
lab-00-04 练习题：函数基础
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 定义函数 add(a, b)，返回 a+b。调用 add(2, 3) 并打印结果
# 期望输出: 5
def exercise_1():
    # 先 def add(a, b): ...
    pass


# ========== 练习 2 ==========
# 定义函数 greet(name, greeting="Hello")，打印 greeting + ", " + name。分别用默认值和传入 "Hi" 调用
# 期望输出: Hello, 名字 和 Hi, 名字（两行）
def exercise_2():
    pass


# ========== 练习 3 ==========
# 定义函数 get_first_two(lst)，返回列表的前两个元素（用切片）。打印 get_first_two([10, 20, 30])
# 期望输出: [10, 20]
def exercise_3():
    pass


# ========== 练习 4 ==========
# 定义函数 min_max(a, b)，返回 (较小值, 较大值)。用解包接收并打印
# 期望输出: 较小值 较大值（例如 min_max(5,3) -> 3 5）
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 5")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] Hello, xxx 和 Hi, xxx")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] [10, 20]")
    print("\n=== 练习 4 ===")
    exercise_4()
    print("  [期望] 较小值 较大值")
