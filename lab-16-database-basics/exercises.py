#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-14-database-basics - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
"""

from sqlalchemy import create_engine, String, Integer, Float, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# ========== 练习 1: 定义模型 ==========

print("=" * 50)
print("练习 1: 定义模型")
print("=" * 50)

# TODO: 定义一个 Book（书籍）模型，包含以下字段：
# - id: int，主键
# - title: str，标题（最大长度 100）
# - author: str，作者（最大长度 50）
# - price: float，价格
# - stock: int，库存数量

class Base(DeclarativeBase):
    """所有模型类的基类"""
    pass


# 在这里完成练习 1 的代码
class Book(Base):
    """书籍模型"""
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    author: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', price={self.price}, stock={self.stock})"


# 创建数据库和表
engine = create_engine("sqlite:///:memory:", echo=False)
Base.metadata.create_all(engine)

print("Book 模型已定义并创建表")
print(f"Book 类的属性: id, title, author, price, stock")


# ========== 练习 2: 实现完整的 CRUD 操作 ==========

print("\n" + "=" * 50)
print("练习 2: CRUD 操作")
print("=" * 50)

with Session(engine) as session:
    # TODO: 创建 3 本书并添加到数据库
    # 书籍 1: 《Python编程》 by "张三", 59.9, 10
    # 书籍 2: 《算法导论》 by "李四", 89.9, 5
    # 书籍 3: 《数据结构》 by "王五", 69.9, 8

    # 在这里完成练习 2 的代码
    books = [
        Book(title="Python编程", author="张三", price=59.9, stock=10),
        Book(title="算法导论", author="李四", price=89.9, stock=5),
        Book(title="数据结构", author="王五", price=69.9, stock=8),
    ]
    session.add_all(books)
    session.commit()

    print("已添加 3 本书")

    # TODO: 查询所有书籍并打印
    # 在这里完成练习 2 的代码
    stmt = select(Book)
    print("\n所有书籍：")
    for book in session.scalars(stmt):
        print(f"  {book}")

    # TODO: 查询价格大于 60 的书籍
    # 在这里完成练习 2 的代码
    stmt = select(Book).where(Book.price > 60)
    print("\n价格 > 60 的书籍：")
    for book in session.scalars(stmt):
        print(f"  {book}")

    # TODO: 更新《Python编程》的库存为 15
    # 在这里完成练习 2 的代码
    stmt = select(Book).where(Book.title == "Python编程")
    book = session.scalar(stmt)
    book.stock = 15
    session.commit()
    print(f"\n更新后《Python编程》: {book}")

    # TODO: 删除《算法导论》
    # 在这里完成练习 2 的代码
    stmt = select(Book).where(Book.title == "算法导论")
    book = session.scalar(stmt)
    session.delete(book)
    session.commit()

    print("\n删除《算法导论》后的书籍列表：")
    stmt = select(Book)
    for book in session.scalars(stmt):
        print(f"  {book}")


# ========== 练习 3: 复杂查询 ==========

print("\n" + "=" * 50)
print("练习 3: 复杂查询")
print("=" * 50)

# 重新添加数据用于复杂查询练习
with Session(engine) as session:
    books = [
        Book(title="Python编程", author="张三", price=59.9, stock=15),
        Book(title="算法导论", author="李四", price=89.9, stock=5),
        Book(title="数据结构", author="王五", price=69.9, stock=8),
        Book(title="机器学习", author="张三", price=99.9, stock=3),
        Book(title="深度学习", author="李四", price=79.9, stock=12),
    ]
    session.add_all(books)
    session.commit()

    # TODO: 查询张三写的所有书籍
    # 在这里完成练习 3 的代码
    stmt = select(Book).where(Book.author == "张三")
    print("张三写的书籍：")
    for book in session.scalars(stmt):
        print(f"  {book}")

    # TODO: 查询价格在 60-90 之间的书籍
    # 在这里完成练习 3 的代码
    stmt = select(Book).where(Book.price >= 60, Book.price <= 90)
    print("\n价格在 60-90 之间的书籍：")
    for book in session.scalars(stmt):
        print(f"  {book}")

    # TODO: 按价格降序排序，取前 3 本最贵的书
    # 在这里完成练习 3 的代码
    stmt = select(Book).order_by(Book.price.desc()).limit(3)
    print("\n最贵的 3 本书：")
    for book in session.scalars(stmt):
        print(f"  {book}")

    # TODO: 统计所有书籍的平均价格
    # 在这里完成练习 3 的代码
    stmt = select(func.avg(Book.price))
    avg_price = session.scalar(stmt)
    print(f"\n所有书籍的平均价格: {avg_price:.2f}")

    # TODO: 统计总库存
    # 在这里完成练习 3 的代码
    stmt = select(func.sum(Book.stock))
    total_stock = session.scalar(stmt)
    print(f"所有书籍的总库存: {total_stock}")

    # TODO: 统计张三写了几本书
    # 在这里完成练习 3 的代码
    stmt = select(func.count(Book.id)).where(Book.author == "张三")
    count = session.scalar(stmt)
    print(f"张三写了 {count} 本书")


print("\n" + "=" * 50)
print("所有练习完成！")
print("=" * 50)
