"""
lab-07-numpy-basics: 多维数组与矩阵运算
"""
import numpy as np


def demo_creation():
    """创建数组"""
    a = np.array([1, 2, 3, 4, 5])
    z = np.zeros((2, 3))
    o = np.ones((2, 2))
    r = np.arange(0, 10, 2)
    lin = np.linspace(0, 1, 5)
    print("arange(0,10,2):", r)
    print("linspace(0,1,5):", lin)
    print("zeros(2,3):\n", z)


def demo_shape_broadcast():
    """shape 与广播"""
    a = np.array([[1, 2], [3, 4]])
    print("shape:", a.shape)
    b = np.array([10, 20])
    print("a + b (broadcast):\n", a + b)


def demo_ops():
    """矩阵与逐元素运算"""
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[0, 1], [1, 0]])
    print("a * b (element-wise):\n", a * b)
    print("a @ b (matrix mult):\n", a @ b)
    print("a.dot(b):\n", a.dot(b))


if __name__ == "__main__":
    print("=== 创建 ===")
    demo_creation()
    print("\n=== shape / 广播 ===")
    demo_shape_broadcast()
    print("\n=== 运算 ===")
    demo_ops()
