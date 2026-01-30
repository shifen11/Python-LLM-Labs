"""
lab-10 练习题：async/await
运行: python exercises.py
"""

import asyncio


# ========== 练习 1 ==========
# 写一个 async def hello()：内部 await asyncio.sleep(0.1)，然后打印 "Hello"。用 asyncio.run(hello()) 运行
# 期望输出: Hello
def exercise_1():
    pass


# ========== 练习 2 ==========
# 写两个 async 函数 task_a、task_b，分别 sleep 0.2 秒后返回 "A" 和 "B"。用 asyncio.gather(task_a(), task_b()) 并发执行，打印结果列表
# 期望输出: ['A', 'B']（总耗时约 0.2s 而非 0.4s）
def exercise_2():
    pass


# ========== 练习 3 ==========
# 用 asyncio.create_task 创建两个任务，再 await 它们的结果，打印（等价于 gather 的效果）
# 期望输出: 两个返回值（如 'A', 'B'）
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] Hello")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] ['A', 'B']")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 两个返回值")
