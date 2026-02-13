"""
lab-09 练习题：Pydantic 类型校验
运行: python exercises.py
需安装: pip install pydantic
"""

from pydantic import BaseModel, Field


# ========== 练习 1 ==========
# 定义 Pydantic 模型 Product：name(str)、price(float, 且 ge=0)、stock(int, 默认 0)。创建实例并打印 model_dump()
# 期望输出: {'name': '...', 'price': ..., 'stock': 0}
def exercise_1():
    pass


# ========== 练习 2 ==========
# 给 Product 加可选字段 description: str | None = None。创建带 description 和不带的两个实例，打印
# 期望输出: 一个无 description（None），一个有 description 值
def exercise_2():
    pass


# ========== 练习 3 ==========
# 尝试用 Product(name="x", price=-1) 创建，用 try/except 捕获 ValidationError 并打印「校验失败」
# 期望输出: 校验失败（或 ValidationError 信息）
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] dict 含 name, price, stock")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 两个实例的 model_dump()")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 校验失败")
