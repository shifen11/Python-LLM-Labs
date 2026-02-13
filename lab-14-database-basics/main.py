#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-14-database-basics - 数据库操作

本脚本演示使用 SQLAlchemy ORM 进行数据库操作。
"""

from sqlalchemy import create_engine, String, Integer, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# ========== 1. SQLAlchemy 简介 ==========

print("=" * 60)
print("lab-14-database-basics - 数据库操作")
print("=" * 60)

print("\n1. SQLAlchemy 简介")
print("-" * 60)

print("""
SQLAlchemy 是 Python 生态中最流行的 ORM（对象关系映射）库。

ORM 的好处：
  - 不需要手写 SQL 语句
  - 使用面向对象的方式操作数据库
  - 数据库无关，可以轻松切换数据库
  - 类型安全，减少错误

核心概念：
  - Engine：数据库连接引擎
  - Session：数据库会话，管理数据库操作
  - Model：数据模型类，映射到数据库表
  - Base：所有模型类的基类
""")

# >>> [说明] 创建 SQLite 内存数据库引擎
# SQLite 是轻量级数据库，不需要额外安装，适合学习
engine = create_engine("sqlite:///:memory:", echo=False)

print("\n使用 SQLite 内存数据库进行演示")


# ========== 2. 定义模型 ==========

print("\n\n2. 定义模型")
print("-" * 60)

# >>> [说明] 定义基类
class Base(DeclarativeBase):
    """所有模型类的基类"""
    pass


# >>> [说明] 定义 User 模型
class User(Base):
    """用户模型"""
    __tablename__ = "users"

    # >>> [说明] 映射列定义
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')"


# >>> [说明] 定义 Product 模型
class Product(Base):
    """产品模型"""
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"


print("\n定义了两个模型类：")
print("  - User: 用户信息（id, name, age, email）")
print("  - Product: 产品信息（id, name, price, stock）")

# >>> [说明] 创建表结构
Base.metadata.create_all(engine)
print("\n表结构已创建")


# ========== 3. 创建数据（Create）==========

print("\n\n3. 创建数据（Create）")
print("-" * 60)

# >>> [说明] 创建会话
with Session(engine) as session:
    # >>> [说明] 创建并添加用户
    user1 = User(name="张三", age=20, email="zhangsan@example.com")
    user2 = User(name="李四", age=25, email="lisi@example.com")
    user3 = User(name="王五", age=18, email="wangwu@example.com")

    # >>> [说明] 添加到会话
    session.add(user1)
    session.add(user2)
    session.add(user3)

    # >>> [说明] 提交到数据库
    session.commit()

    print(f"已添加 3 个用户：{user1}, {user2}, {user3}")

    # >>> [说明] 批量添加产品
    products = [
        Product(name="笔记本电脑", price=5999.0, stock=10),
        Product(name="手机", price=3999.0, stock=20),
        Product(name="耳机", price=299.0, stock=50),
    ]
    session.add_all(products)
    session.commit()

    print(f"已添加 {len(products)} 个产品")


# ========== 4. 查询数据（Read）==========

print("\n\n4. 查询数据（Read）")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 查询所有用户
    print("\n--- 查询所有用户 ---")
    stmt = select(User)
    for user in session.scalars(stmt):
        print(f"  {user}")

    # >>> [说明] 查询单个用户（通过 id）
    print("\n--- 查询单个用户（id=1）---")
    user = session.get(User, 1)
    print(f"  {user}")

    # >>> [说明] 查询单个用户（通过条件）
    print("\n--- 查询名为 '李四' 的用户 ---")
    stmt = select(User).where(User.name == "李四")
    user = session.scalar(stmt)
    print(f"  {user}")


# ========== 5. 更新数据（Update）==========

print("\n\n5. 更新数据（Update）")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 先查询，再修改
    stmt = select(User).where(User.name == "张三")
    user = session.scalar(stmt)

    print(f"更新前：{user}")

    # >>> [说明] 修改属性
    user.age = 21
    user.email = "zhangsan_new@example.com"

    # >>> [说明] 提交更改
    session.commit()

    # >>> [说明] 重新查询验证
    user = session.scalar(stmt)
    print(f"更新后：{user}")


# ========== 6. 删除数据（Delete）==========

print("\n\n6. 删除数据（Delete）")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 先查询要删除的用户
    stmt = select(User).where(User.name == "王五")
    user = session.scalar(stmt)

    print(f"准备删除：{user}")

    # >>> [说明] 删除用户
    session.delete(user)
    session.commit()

    # >>> [说明] 验证删除
    print("\n删除后的用户列表：")
    stmt = select(User)
    for user in session.scalars(stmt):
        print(f"  {user}")


# ========== 7. 查询过滤和排序 ==========

print("\n\n7. 查询过滤和排序")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 过滤：年龄大于等于 20 的用户
    print("\n--- 年龄 >= 20 的用户 ---")
    stmt = select(User).where(User.age >= 20)
    for user in session.scalars(stmt):
        print(f"  {user}")

    # >>> [说明] 排序：按年龄升序
    print("\n--- 按年龄升序排序 ---")
    stmt = select(User).order_by(User.age)
    for user in session.scalars(stmt):
        print(f"  {user}")

    # >>> [说明] 排序：按年龄降序
    print("\n--- 按年龄降序排序 ---")
    stmt = select(User).order_by(User.age.desc())
    for user in session.scalars(stmt):
        print(f"  {user}")

    # >>> [说明] 限制：只返回前 2 个用户
    print("\n--- 前 2 个用户 ---")
    stmt = select(User).limit(2)
    for user in session.scalars(stmt):
        print(f"  {user}")


# ========== 8. 复杂查询 ==========

print("\n\n8. 复杂查询")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 多条件过滤：价格大于 1000 且库存大于 15 的产品
    print("\n--- 价格 > 1000 且库存 > 15 的产品 ---")
    stmt = select(Product).where(Product.price > 1000, Product.stock > 15)
    for product in session.scalars(stmt):
        print(f"  {product}")

    # >>> [说明] 价格范围：价格在 500 到 6000 之间的产品
    print("\n--- 价格在 500-6000 之间的产品 ---")
    stmt = select(Product).where(Product.price >= 500, Product.price <= 6000)
    for product in session.scalars(stmt):
        print(f"  {product}")

    # >>> [说明] 价格排序后取前 2 个最贵的
    print("\n--- 最贵的 2 个产品 ---")
    stmt = select(Product).order_by(Product.price.desc()).limit(2)
    for product in session.scalars(stmt):
        print(f"  {product}")


# ========== 9. 统计查询 ==========

print("\n\n9. 统计查询")
print("-" * 60)

with Session(engine) as session:
    # >>> [说明] 计数：用户总数
    from sqlalchemy import func

    stmt = select(func.count(User.id))
    user_count = session.scalar(stmt)
    print(f"用户总数：{user_count}")

    # >>> [说明] 计数：产品总数
    stmt = select(func.count(Product.id))
    product_count = session.scalar(stmt)
    print(f"产品总数：{product_count}")

    # >>> [说明] 平均值：平均价格
    stmt = select(func.avg(Product.price))
    avg_price = session.scalar(stmt)
    print(f"产品平均价格：{avg_price:.2f}")

    # >>> [说明] 求和：总库存
    stmt = select(func.sum(Product.stock))
    total_stock = session.scalar(stmt)
    print(f"产品总库存：{total_stock}")


print("\n\n" + "=" * 60)
print("实验室演示完成！")
print("=" * 60)

print("\n总结：")
print("  - 定义模型：继承 DeclarativeBase，使用 mapped_column 定义列")
print("  - 创建记录：session.add() 或 session.add_all()")
print("  - 查询记录：select() 配合 where()、order_by()、limit()")
print("  - 更新记录：查询后修改属性，session.commit()")
print("  - 删除记录：session.delete()")
print("  - 提交更改：session.commit()")
