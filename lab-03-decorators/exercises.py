"""
lab-03 练习题：装饰器
运行: python exercises.py
"""

import functools


# ========== 练习 1 ==========
# 写一个装饰器 repeat_twice：被装饰的函数执行两次（不要求保留返回值），并打印「第1次」「第2次」
# 期望输出: 第1次 / Hi / 第2次 / Hi
def exercise_1():
    def repeat_twice(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # 你的代码：调用 f 两次
            pass
        return wrapper

    @repeat_twice
    def say_hi():
        print("Hi")

    say_hi()


# ========== 练习 2 ==========
# 写一个装饰器 log_name：在调用被装饰函数前后各打印一行「调用 函数名」「返回」
# 期望输出: 调用 xxx / 返回
def exercise_2():
    # 你的装饰器 + 一个示例函数
    pass


# ========== 练习 3 ==========
# 用 @ 语法给一个函数 add(a, b) 加上 log_name 装饰器，调用 add(1, 2) 并打印返回值
# 期望输出: 调用 add / 返回，以及 3
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 第1次 / Hi / 第2次 / Hi")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 调用 函数名 / 返回")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 调用 add / 返回，以及 3")
