#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-00-10-functional-basics - 函数式编程基础

本脚本演示 Python 函数式编程的核心概念。
"""

# >>> [说明] 函数式编程是一种编程范式，强调使用纯函数、避免可变状态
# 函数式编程的核心思想：函数是一等公民（First-class citizen）


# ========== 1. Lambda 表达式 ==========

print("=" * 50)
print("1. Lambda 表达式（匿名函数）")
print("=" * 50)

# >>> [说明] lambda 是匿名函数的简写，语法：lambda 参数: 表达式
# >>> [说明] lambda 只能包含一个表达式，不能包含语句（如 if, for 等）

# 传统函数定义
def square(x):
    """计算平方"""
    return x * x

# >>> [说明] lambda 表达式定义相同功能
square_lambda = lambda x: x * x

print(f"square(5) = {square(5)}")
# >>> [预期输出] square(5) = 25

print(f"square_lambda(5) = {square_lambda(5)}")
# >>> [预期输出] square_lambda(5) = 25

# >>> [说明] lambda 可以有多个参数
add = lambda x, y: x + y
multiply = lambda x, y: x * y

print(f"add(3, 4) = {add(3, 4)}")
# >>> [预期输出] add(3, 4) = 7

print(f"multiply(3, 4) = {multiply(3, 4)}")
# >>> [预期输出] multiply(3, 4) = 12

# >>> [说明] lambda 的典型使用场景：作为参数传递给高阶函数
numbers = [1, 2, 3, 4, 5]

# 使用 lambda 和 sorted 进行自定义排序
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (5, 'five'), (4, 'four')]

# >>> [触发] 按第二个元素（字符串）排序
sorted_by_second = sorted(pairs, key=lambda x: x[1])
print(f"按第二个元素排序: {sorted_by_second}")
# >>> [预期输出] 按第二个元素排序: [(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# >>> [触发] 按第一个元素的绝对值排序
negative_pairs = [(-3, 'a'), (1, 'b'), (-1, 'c'), (2, 'd')]
sorted_by_abs = sorted(negative_pairs, key=lambda x: abs(x[0]))
print(f"按绝对值排序: {sorted_by_abs}")
# >>> [预期输出] 按绝对值排序: [(1, 'b'), (-1, 'c'), (2, 'd'), (-3, 'a')]


# ========== 2. 高阶函数 - map() ==========

print("\n" + "=" * 50)
print("2. 高阶函数 - map()")
print("=" * 50)

# >>> [说明] map(function, iterable) 对可迭代对象的每个元素应用函数
# >>> [说明] map 返回一个迭代器，需要用 list() 转换

numbers = [1, 2, 3, 4, 5]

# 使用 lambda 和 map
squared = list(map(lambda x: x * x, numbers))
print(f"原列表: {numbers}")
# >>> [预期输出] 原列表: [1, 2, 3, 4, 5]

print(f"平方后: {squared}")
# >>> [预期输出] 平方后: [1, 4, 9, 16, 25]

# 使用命名函数（更清晰）
def power_of_three(x):
    return x ** 3

cubed = list(map(power_of_three, numbers))
print(f"立方后: {cubed}")
# >>> [预期输出] 立方后: [1, 8, 27, 64, 125]

# map 可以接受多个可迭代对象
list1 = [1, 2, 3]
list2 = [10, 20, 30]
added = list(map(lambda x, y: x + y, list1, list2))
print(f"逐元素相加: {added}")
# >>> [预期输出] 逐元素相加: [11, 22, 33]

# 对字符串应用 map
words = ["hello", "world", "python"]
capitalized = list(map(str.upper, words))
print(f"大写: {capitalized}")
# >>> [预期输出] 大写: ['HELLO', 'WORLD', 'PYTHON']


# ========== 3. 高阶函数 - filter() ==========

print("\n" + "=" * 50)
print("3. 高阶函数 - filter()")
print("=" * 50)

# >>> [说明] filter(function, iterable) 筛选满足条件的元素
# >>> [说明] function 返回 True 时保留元素

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {evens}")
# >>> [预期输出] 偶数: [2, 4, 6, 8, 10]

# 筛选大于 5 的数
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(f"大于 5 的数: {greater_than_five}")
# >>> [预期输出] 大于 5 的数: [6, 7, 8, 9, 10]

# 筛选字符串长度大于 5 的单词
words = ["hi", "hello", "python", "functional", "test"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(f"长度 > 5 的单词: {long_words}")
# >>> [预期输出] 长度 > 5 的单词: ['hello', 'python', 'functional']


# ========== 4. 高阶函数 - reduce() ==========

print("\n" + "=" * 50)
print("4. 高阶函数 - reduce()")
print("=" * 50)

# >>> [说明] reduce(function, iterable) 将函数累积应用到序列的元素
# >>> [说明] reduce 在 Python 3 中需要从 functools 导入

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 计算和（sum 的实现）
total = reduce(lambda a, b: a + b, numbers)
print(f"总和: {total}")
# >>> [预期输出] 总和: 15

# 计算乘积
product = reduce(lambda a, b: a * b, numbers)
print(f"乘积: {product}")
# >>> [预期输出] 乘积: 120

# 找最大值（max 的实现）
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"最大值: {maximum}")
# >>> [预期输出] 最大值: 5

# 使用初始值
total_with_init = reduce(lambda a, b: a + b, numbers, 10)
print(f"带初始值的和 (10 + ...): {total_with_init}")
# >>> [预期输出] 带初始值的和 (10 + ...): 25

# 字符串拼接
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda a, b: a + b, words)
print(f"拼接结果: {sentence}")
# >>> [预期输出] 拼接结果: Hello World!


# ========== 5. 闭包（Closure）==========

print("\n" + "=" * 50)
print("5. 闭包（Closure）")
print("=" * 50)

# >>> [说明] 闭包：函数能够记住并访问其词法作用域
# >>> [说明] 即使函数在其定义的作用域之外执行

def make_multiplier(factor):
    """创建一个乘法器函数"""
    def multiplier(x):
        # multiplier 可以访问 make_multiplier 的参数 factor
        return x * factor
    return multiplier  # 返回内部函数

# 创建不同的乘法器
double = make_multiplier(2)  # double 记住了 factor=2
triple = make_multiplier(3)  # triple 记住了 factor=3

# 每个闭包有自己独立的状态
print(f"double(5) = {double(5)}")
# >>> [预期输出] double(5) = 10

print(f"triple(5) = {triple(5)}")
# >>> [预期输出] triple(5) = 15

# >>> [说明] 闭包可以用来创建计数器
def make_counter():
    """创建一个计数器"""
    count = 0  # 私有变量

    def increment():
        nonlocal count  # 声明使用外层作用域的变量
        count += 1
        return count

    def get_count():
        return count

    return increment, get_count

counter1_inc, counter1_get = make_counter()
counter2_inc, counter2_get = make_counter()

# 两个计数器是独立的
print(f"Counter 1: {counter1_inc()}, {counter1_inc()}, {counter1_get()}")
# >>> [预期输出] Counter 1: 1, 2, 2

print(f"Counter 2: {counter2_inc()}, {counter2_get()}")
# >>> [预期输出] Counter 2: 1, 1


# ========== 6. 作用域规则（LEGB）==========

print("\n" + "=" * 50)
print("6. 作用域规则（LEGB）")
print("=" * 50)

# >>> [说明] Python 使用 LEGB 规则查找变量名：
# L (Local) → E (Enclosing) → G (Global) → B (Built-in)

x_global = "全局"

def outer():
    x_enclosing = "外层函数"

    def inner():
        x_local = "内层函数"

        # >>> [触发] 展示不同作用域的变量
        print(f"Local: {x_local}")
        print(f"Enclosing: {x_enclosing}")
        print(f"Global: {x_global}")

    inner()

outer()
# >>> [预期输出]
# Local: 内层函数
# Enclosing: 外层函数
# Global: 全局


# ========== 7. 函数式编程思维 ==========

print("\n" + "=" * 50)
print("7. 函数式编程思维")
print("=" * 50)

# >>> [说明] 函数式编程强调：
# 1. 纯函数：相同的输入永远得到相同的输出，无副作用
# 2. 不可变数据：不修改原始数据
# 3. 函数组合：将简单函数组合成复杂功能

# 命令式风格（修改原数据）
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] *= 2
print(f"命令式（修改原数据）: {numbers}")
# >>> [预期输出] 命令式（修改原数据）: [2, 4, 6, 8, 10]

# 函数式风格（创建新数据）
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"函数式（创建新数据）: 原数据={numbers}, 新数据={doubled}")
# >>> [预期输出] 函数式（创建新数据）: 原数据=[1, 2, 3, 4, 5], 新数据=[2, 4, 6, 8, 10]

# 函数组合：将简单函数串联
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 复杂操作：筛选偶数 → 平方 → 找大于20的
result = list(filter(lambda x: x > 20, map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))))
print(f"偶数的平方中大于20的: {result}")
# >>> [预期输出] 偶数的平方中大于20的: [36, 64, 100]


print("\n" + "=" * 50)
print("实验室演示完成！")
print("=" * 50)
