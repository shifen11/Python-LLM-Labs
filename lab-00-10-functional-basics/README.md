# lab-00-10-functional-basics - 函数式编程基础

## 简介

本实验室介绍 Python 中的函数式编程基础概念，包括 lambda 表达式、高阶函数、闭包等。这些概念是理解装饰器（lab-03）和异步编程（后续 lab）的重要基础。

## 学习目标

- 掌握 lambda 表达式的基本语法和使用场景
- 理解高阶函数：`map()`, `filter()`, `reduce()`
- 理解闭包的概念和作用域规则
- 了解函数式编程的思维模式
- 掌握简单的函数组合技巧

## 运行方法

### 交互式演示

```bash
python main.py
```

### 练习题

```bash
python exercises.py
```

## 核心概念

### Lambda 表达式

Lambda 是匿名函数的简写形式，适用于简单的单行函数。

```python
# 普通函数
def square(x):
    return x * x

# Lambda 表达式
square = lambda x: x * x
```

### 高阶函数

高阶函数是接收函数作为参数或返回函数的函数。

```python
# map: 对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))  # [1, 4, 9, 16, 25]

# filter: 筛选满足条件的元素
even = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# reduce: 累积计算
from functools import reduce
total = reduce(lambda a, b: a + b, numbers)  # 15
```

### 闭包

闭包是指函数能够记住并访问其词法作用域，即使函数在其定义的作用域之外执行。

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier  # 返回内部函数

double = make_multiplier(2)  # double 闭包捕获了 factor=2
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## 内容概览

### main.py 演示内容

1. **Lambda 表达式**
   - 基本语法
   - 与普通函数的对比
   - 常见使用场景（sort, filter 等）

2. **高阶函数**
   - `map()` - 映射转换
   - `filter()` - 过滤筛选
   - `reduce()` - 累积计算
   - `sorted()` 与 `key` 参数

3. **闭包**
   - 闭包的定义和特性
   - 作用域规则（LEGB 规则）
   - 实用闭包示例

4. **函数式编程思维**
   - 不可变数据
   - 纯函数
   - 函数组合

### exercises.py 练习题

1. 使用 lambda 和 map 转换列表
2. 使用 filter 筛选数据
3. 使用 reduce 计算累积值
4. 创建一个闭包函数
5. 实现简单的函数组合

## 前置知识

- Python 函数基础（lab-00-04）
- 列表等数据结构（lab-00-05）
- 面向对象基础（lab-00-09）

## 后续关联

- **lab-03-decorators**：装饰器本质上是高阶函数+闭包的组合
- **lab-11-asyncio-concurrency**：异步编程大量使用 lambda 和高阶函数
- **lab-12-api-integration**：回调函数常使用 lambda
