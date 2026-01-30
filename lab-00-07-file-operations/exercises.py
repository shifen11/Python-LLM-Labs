"""
lab-00-07 练习题：文件操作
运行: python exercises.py
会在当前目录创建/读取/删除 exercise_out.txt，注意当前工作目录
"""

import os


# ========== 练习 1 ==========
# 用 with open("exercise_out.txt", "w", encoding="utf-8") 写入两行：第一行、第二行
# 期望输出: 无（文件被创建）
def exercise_1():
    pass


# ========== 练习 2 ==========
# 用 with open("exercise_out.txt", "r", encoding="utf-8") 读取全部内容并打印（若文件不存在则先做练习 1）
# 期望输出: 第一行\n第二行（或两行内容）
def exercise_2():
    pass


# ========== 练习 3 ==========
# 用 os.path.exists 判断 "exercise_out.txt" 是否存在，打印 True/False；若存在再用 os.path.getsize 打印文件大小
# 期望输出: True 和一个正整数（字节数）
def exercise_3():
    pass


# ========== 练习 4（清理）==========
# 若 exercise_out.txt 存在，用 os.remove 删除，并打印「已删除」
# 期望输出: 已删除
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 无输出，文件被创建")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 第一行、第二行（两行内容）")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] True 和文件大小（字节）")
    print("\n=== 练习 4（清理）===")
    exercise_4()
    print("  [期望] 已删除")
