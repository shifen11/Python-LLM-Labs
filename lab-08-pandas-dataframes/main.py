"""
lab-08-pandas-dataframes: DataFrame 创建、筛选、聚合
"""
import pandas as pd


def demo_dataframe():
    """创建与基本操作"""
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "age": [25, 30, 28],
        "score": [85, 90, 88],
    })
    print("DataFrame:")
    print(df)
    print("\ndf.describe():")
    print(df.describe())
    print("\ndf[df.age >= 28]:")
    print(df[df["age"] >= 28])


def demo_groupby():
    """分组聚合"""
    df = pd.DataFrame({
        "dept": ["A", "A", "B", "B"],
        "amount": [10, 20, 15, 25],
    })
    g = df.groupby("dept")["amount"].sum()
    print("groupby dept, sum(amount):")
    print(g)


if __name__ == "__main__":
    print("=== DataFrame 基础 ===")
    demo_dataframe()
    print("\n=== groupby ===")
    demo_groupby()
