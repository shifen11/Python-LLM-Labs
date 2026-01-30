"""
lab-02 练习题：解构赋值、*args、**kwargs
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 用解构：first, *rest, last = [1, 2, 3, 4, 5]，打印 first、rest、last
# 期望输出: first=1, rest=[2, 3, 4], last=5
def exercise_1():
    pass


# ========== 练习 2 ==========
# 定义函数 greet(*names)，遍历 names 并打印 "Hello, 名字!"。调用 greet("A", "B")
# 期望输出: Hello, A! 和 Hello, B!
def exercise_2():
    pass


# ========== 练习 3 ==========
# 定义函数 print_config(**kwargs)，遍历 kwargs 并打印 "key = value"。调用 print_config(a=1, b=2)
# 期望输出: a = 1 和 b = 2
def exercise_3():
    pass


# ========== 练习 4 ==========
# 定义函数 f(a, b, *args, **kwargs)，打印 a, b, args, kwargs。调用 f(1, 2, 3, 4, x=10, y=20)
# 期望输出: a=1, b=2, args=(3, 4), kwargs={'x': 10, 'y': 20}
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] first=1, rest=[2,3,4], last=5")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] Hello, A! 和 Hello, B!")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] a = 1 和 b = 2")
    print("\n=== 练习 4 ===")
    exercise_4()
    print("  [期望] a=1, b=2, args=(3,4), kwargs={'x':10,'y':20}")
