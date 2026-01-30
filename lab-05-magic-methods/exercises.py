"""
lab-05 练习题：魔术方法
运行: python exercises.py
"""


# ========== 练习 1 ==========
# 写一个类 Box，__init__(self, value) 存 self.value，__str__(self) 返回 f"Box({self.value})"。创建 Box(42) 并用 print 打印
# 期望输出: Box(42)
def exercise_1():
    pass


# ========== 练习 2 ==========
# 给 Box 实现 __call__(self, x)，返回 self.value + x。创建 b = Box(10)，打印 b(5) 的结果
# 期望输出: 15
def exercise_2():
    pass


# ========== 练习 3 ==========
# 写一个类 MyList，__init__(self, data) 存 self._data = list(data)，实现 __len__ 和 __getitem__，使 len(obj)、obj[0]、obj[1:3] 可用。创建 MyList([10,20,30,40]) 并测试
# 期望输出: len=4, obj[0]=10, obj[1:3]=[20, 30]
def exercise_3():
    pass


# ========== 练习 4 ==========
# 给 MyList 实现 __iter__，使 for x in obj 和 list(obj) 可用。对 MyList([1,2,3]) 执行 list(...) 并打印
# 期望输出: [1, 2, 3]
def exercise_4():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] Box(42)")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] 15")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] len=4, obj[0]=10, obj[1:3]=[20,30]")
    print("\n=== 练习 4 ===")
    exercise_4()
    print("  [期望] [1, 2, 3]")
