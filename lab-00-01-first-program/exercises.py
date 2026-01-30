"""
lab-00-01 练习题：第一个 Python 程序
在 lab 目录下运行: python exercises.py
完成下方任务，取消注释或填写代码后运行自测。
"""


# ========== 练习 1 ==========
# 用 print 输出一行：你好，[你的名字]！
# 期望输出: 你好，[你填的名字]！
def exercise_1():
    # 你的代码（可多行）
    print("hello")


# ========== 练习 2 ==========
# 用 f-string 定义变量 name="Python", version=3.12，然后打印：语言：Python，版本：3.12
# 期望输出: 语言：Python，版本：3.12
def exercise_2():
    # 你的代码
    name="python"
    version=3.12
    print(f"name={name},版本={version}")



# ========== 练习 3 ==========
# 写一个 if True: 块，块内打印两行：第一行、第二行；块外打印：块外
# 期望输出: 第一行\n第二行\n块外
def exercise_3():
    # 你的代码
    if True:
        print( )




if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 你好，[你的名字]！")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 语言：Python，版本：3.12")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 第一行 / 第二行 / 块外")
