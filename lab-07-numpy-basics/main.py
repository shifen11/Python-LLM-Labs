"""
lab-07-numpy-basics: 多维数组与矩阵运算

运行时会展示：创建数组（array/zeros/ones/arange/linspace）、shape、广播、以及逐元素与矩阵乘法。
"""
import numpy as np

print("=== 1. 创建数组 ===\n")
print("  >>> [说明] np.array(列表) 从 Python 列表创建；dtype 可指定类型")
a = np.array([1, 2, 3, 4, 5])
print(f"  np.array([1,2,3,4,5]) -> {a}, shape = {a.shape}")

print("  >>> [说明] np.zeros(shape) / np.ones(shape) 全 0 或全 1")
z = np.zeros((2, 3))
print(f"  np.zeros((2,3)):\n{z}")
o = np.ones((2, 2))
print(f"  np.ones((2,2)):\n{o}")

print("  >>> [说明] np.arange(start, stop, step) 类似 range；np.linspace 等分")
r = np.arange(0, 10, 2)
lin = np.linspace(0, 1, 5)
print(f"  np.arange(0,10,2) -> {r}")
print(f"  np.linspace(0,1,5) -> {lin}\n")

print("=== 2. shape 与广播 ===\n")
print("  >>> [说明] .shape 为各维长度；广播：形状不同时，小数组会「扩展」以匹配大数组")
a = np.array([[1, 2], [3, 4]])
print(f"  a.shape = {a.shape}")
b = np.array([10, 20])
print(f"  b = {b}, shape = {b.shape}")
print("  >>> [触发] a + b 时 b 被广播为 [[10,20],[10,20]]")
print(f"  a + b:\n{a + b}\n")

print("=== 3. 逐元素运算 vs 矩阵乘法 ===\n")
print("  >>> [说明] * 为逐元素乘；@ 或 .dot() 为矩阵乘法（行×列）")
a = np.array([[1, 2], [3, 4]])
b = np.array([[0, 1], [1, 0]])
print("  a * b（逐元素）:")
print(a * b)
print("  a @ b（矩阵乘法）:")
print(a @ b)
print("  a.dot(b) 同上:")
print(a.dot(b))
