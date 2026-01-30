"""
lab-08-pandas-dataframes: 表格化数据清洗与分析

运行时会展示：DataFrame 的创建、列访问、describe、布尔筛选、以及 groupby 聚合。
"""
import pandas as pd

print("=== 1. 创建 DataFrame ===\n")
print("  >>> [说明] pd.DataFrame(dict)：键为列名，值为该列数据（列表/数组）")
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "age": [25, 30, 28],
    "score": [85, 90, 88],
})
print("  df =")
print(df)
print(f"\n  >>> [说明] df.dtypes 查看每列类型；df.index 为行索引")
print(f"  dtypes:\n{df.dtypes}\n")

print("=== 2. 基本统计 describe() ===\n")
print("  >>> [说明] 数值列会自动统计 count/mean/std/min/25%/50%/75%/max")
print(df.describe())
print()

print("=== 3. 布尔筛选（类似 SQL WHERE）===\n")
print("  >>> [说明] df[df['列名'] 条件] 得到满足条件的行")
print("  df[df['age'] >= 28] ->")
print(df[df["age"] >= 28])
print("  >>> [小结] 条件返回布尔 Series，True 的行被保留\n")

print("=== 4. groupby 分组聚合 ===\n")
print("  >>> [说明] df.groupby('列名')['另一列'].sum() 按列分组后对另一列聚合")
df2 = pd.DataFrame({
    "dept": ["A", "A", "B", "B"],
    "amount": [10, 20, 15, 25],
})
print("  原表:")
print(df2)
g = df2.groupby("dept")["amount"].sum()
print("  groupby('dept')['amount'].sum():")
print(g)
print("  >>> [小结] 结果是一个 Series，索引为分组键")
