"""
lab-08 练习题：Pandas DataFrame
运行: python exercises.py
需安装: pip install pandas
"""


# ========== 练习 1 ==========
# 用 pd.DataFrame 创建表：列 name=["A","B","C"]，列 score=[85,90,88]。打印 df 和 df.describe()
# 期望输出: 3 行 2 列表格；describe 有 count/mean/std/min/25%/50%/75%/max
def exercise_1():
    pass


# ========== 练习 2 ==========
# 对上述 df，筛选 score >= 88 的行，打印
# 期望输出: 2 行（B 和 C）
def exercise_2():
    pass


# ========== 练习 3 ==========
# 创建 df：列 dept=["A","A","B","B"]，列 amount=[10,20,15,25]。用 groupby("dept")["amount"].sum() 得到各部门总和，打印
# 期望输出: A 30, B 40
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 3 行 2 列；describe 统计表")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 2 行（score>=88）")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] A 30, B 40")
