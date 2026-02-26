#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-00-10-functional-basics - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
"""

# ========== 练习 1: 使用 lambda 和 map ==========

print("=" * 50)
print("练习 1: 使用 lambda 和 map")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

# TODO: 使用 lambda 和 map 将列表中的每个数加 10
# 提示：result = list(map(lambda x: ..., numbers))
result = list(map(lambda x: x + 10, numbers))

print(f"原列表: {numbers}")
print(f"每个数加 10: {result}")

# 预期输出:
# 原列表: [1, 2, 3, 4, 5]
# 每个数加 10: [11, 12, 13, 14, 15]

# 验证
assert result == [11, 12, 13, 14, 15], "结果不正确"
print("✓ 练习 1 通过!\n")


# ========== 练习 2: 使用 filter 筛选数据 ==========

print("=" * 50)
print("练习 2: 使用 filter 筛选数据")
print("=" * 50)

words = ["apple", "banana", "pear", "grapefruit", "kiwi", "watermelon"]

# TODO: 使用 filter 和 lambda 筛选出长度小于 6 的单词
# 提示：short_words = list(filter(lambda w: ..., words))
short_words = list(filter(lambda w: len(w) < 6, words))

print(f"所有单词: {words}")
print(f"长度 < 6 的单词: {short_words}")

# 预期输出:
# 所有单词: ['apple', 'banana', 'pear', 'grapefruit', 'kiwi', 'watermelon']
# 长度 < 6 的单词: ['apple', 'pear', 'kiwi']

# 验证
assert short_words == ['apple', 'pear', 'kiwi'], "筛选结果不正确"
print("✓ 练习 2 通过!\n")


# ========== 练习 3: 使用 reduce 计算阶乘 ==========

print("=" * 50)
print("练习 3: 使用 reduce 计算阶乘")
print("=" * 50)

from functools import reduce

# TODO: 使用 reduce 计算 5 的阶乘（5! = 5 × 4 × 3 × 2 × 1）
# 提示：factorial_5 = reduce(lambda a, b: ..., range(1, 6))
factorial_5 = reduce(lambda a, b: a * b, range(1, 6))

print(f"5! = {factorial_5}")

# 预期输出:
# 5! = 120

# 验证
assert factorial_5 == 120, "阶乘计算不正确"
print("✓ 练习 3 通过!\n")


# ========== 练习 4: 创建闭包函数 ==========

print("=" * 50)
print("练习 4: 创建闭包函数")
print("=" * 50)

# TODO: 创建一个 make_adder 函数，它返回一个可以给数字加上固定值的函数
# 提示：
# def make_adder(n):
#     def adder(x):
#         return ...
#     return adder

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_5 = make_adder(5)
add_10 = make_adder(10)

print(f"add_5(3) = {add_5(3)}")
print(f"add_10(3) = {add_10(3)}")

# 预期输出:
# add_5(3) = 8
# add_10(3) = 13

# 验证
assert add_5(3) == 8, "add_5 函数不正确"
assert add_10(3) == 13, "add_10 函数不正确"
print("✓ 练习 4 通过!\n")


# ========== 练习 5: 函数组合 ==========

print("=" * 50)
print("练习 5: 函数组合")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: 使用 map 和 filter 的组合完成以下操作：
# 1. 筛选出奇数
# 2. 将每个奇数乘以 3
# 3. 将结果按升序排序
# 提示：使用 map 和 filter 组合，最后用 sorted()
result = sorted(map(lambda x: x * 3, filter(lambda x: x % 2 != 0, numbers)))

print(f"原列表: {numbers}")
print(f"奇数乘以 3 并排序: {result}")

# 预期输出:
# 原列表: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 奇数乘以 3 并排序: [3, 9, 15, 21, 27]

# 验证
assert result == [3, 9, 15, 21, 27], "组合操作结果不正确"
print("✓ 练习 5 通过!\n")


# ========== 练习 6: 使用 lambda 排序 ==========

print("=" * 50)
print("练习 6: 使用 lambda 排序")
print("=" * 50)

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95),
]

# TODO: 使用 sorted 和 lambda 按成绩降序（从高到低）排序
# 提示：sorted(students, key=lambda x: ..., reverse=...)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("按成绩降序排序:")
for name, score in sorted_students:
    print(f"  {name}: {score}")

# 预期输出:
# 按成绩降序排序:
#   Diana: 95
#   Bob: 92
#   Alice: 85
#   Charlie: 78

# 验证
expected = [("Diana", 95), ("Bob", 92), ("Alice", 85), ("Charlie", 78)]
assert sorted_students == expected, "排序结果不正确"
print("✓ 练习 6 通过!\n")


print("=" * 50)
print("所有练习完成！")
print("=" * 50)
