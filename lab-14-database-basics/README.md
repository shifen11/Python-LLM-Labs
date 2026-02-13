# lab-14-database-basics - 数据库操作

## 简介

本实验室介绍使用 SQLAlchemy ORM 进行数据库操作的基本方法。SQLAlchemy 是 Python 生态中最流行的 ORM（对象关系映射）库之一。

## 学习目标

- 理解 ORM 的基本概念
- 掌握 SQLAlchemy DeclarativeBase 的使用
- 学会定义数据模型
- 掌握基本的 CRUD 操作
- 理解查询过滤和排序

## 运行方法

### 交互式演示

```bash
python main.py
```

### 练习题

```bash
python exercises.py
```

## 安装依赖

```bash
pip install sqlalchemy
```

## 核心概念

### ORM（对象关系映射）

ORM 将数据库表映射为 Python 类，将表的行映射为对象，使我们可以使用面向对象的方式操作数据库。

### 模型定义

```python
from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)
```

### CRUD 操作

- **Create**: 创建新记录
- **Read**: 查询记录
- **Update**: 更新记录
- **Delete**: 删除记录

## 内容概览

### main.py 演示内容

1. **SQLAlchemy 简介**
   - 引擎（Engine）的概念
   - 会话（Session）的使用

2. **定义模型**
   - 使用 DeclarativeBase
   - 映射列和类型

3. **CRUD 操作**
   - 添加记录
   - 查询记录
   - 更新记录
   - 删除记录

4. **查询过滤和排序**
   - 使用 filter 过滤
   - 使用 order_by 排序
   - 使用 limit 限制结果

### exercises.py 练习题

1. 定义一个简单的模型
2. 实现完整的 CRUD 操作
3. 复杂查询（过滤、排序、连接）

## 使用 SQLite

本实验室使用 SQLite 内存数据库进行演示，不需要安装额外的数据库软件。SQLite 轻量级、零配置，非常适合学习和开发。
