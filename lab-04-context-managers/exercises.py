"""
lab-04 练习题：with 与上下文管理器
运行: python exercises.py
"""

from contextlib import contextmanager


# ========== 练习 1 ==========
# 用 with open("exercises.py", "r", encoding="utf-8") as f: 读取前 3 行（可用 readline 或 readlines），打印
# 期望输出: 本文件的前 3 行内容
def exercise_1():
    pass


# ========== 练习 2 ==========
# 用 @contextmanager 写一个 managed_counter()：进入时打印「开始」，yield 一个列表 [0]，退出时打印「结束」和列表长度
# 期望输出: 开始 / 结束 len=1（若在 with 块内 lst[0]+=1 则 len 仍为 1）
def exercise_2():
    # 在 with 块内可以 lst[0] += 1
    pass


# ========== 练习 3 ==========
# 写一个类 Timer，实现 __enter__（打印「开始计时」并记录时间）和 __exit__（打印「结束」和耗时秒数）。with Timer(): pass 运行一下
# 期望输出: 开始计时 / 结束 耗时约 0.xxx 秒
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 本文件前 3 行")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 开始 / 结束 len=...")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 开始计时 / 结束 耗时 x.xx 秒")
