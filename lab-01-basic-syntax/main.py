"""
lab-01-basic-syntax: 变量类型、切片、列表推导式

运行时会逐步展示：动态类型、切片规则、推导式写法，以及「何时触发」什么行为。
"""


def demo_types():
    """动态类型：无需声明类型，同一变量可以先后指向不同类型（与 Java 不同）"""
    print("  >>> [说明] Python 变量是「名字绑定到对象」，不写 int x; 这种声明")
    x = 42
    print(f"  x = 42        -> x = {x}, type(x) = {type(x).__name__}")
    x = "hello"
    print(f"  x = 'hello'   -> x = {x}, type(x) = {type(x).__name__}")
    print("  >>> [小结] 变量 x 先指向 int，再指向 str，不会报错\n")


def demo_slicing():
    """切片 [start:stop:step]：对字符串、列表、元组都适用"""
    s = "Python"
    lst = [0, 1, 2, 3, 4, 5]
    print("  >>> [公式] 切片写法: 序列[start:stop:step]，左闭右开，step 为步长")
    print(f"  原序列: s = {s!r}, lst = {lst}")
    print(f"  s[1:4]    -> 从索引1到3: {s[1:4]!r}")
    print(f"  s[::2]    -> 从头到尾步长2: {s[::2]!r}")
    print(f"  s[::-1]   -> step=-1 即反转: {s[::-1]!r}")
    print(f"  lst[-2:]  -> 倒数两个元素: {lst[-2:]}")
    print(f"  lst[:4]   -> 前四个元素: {lst[:4]}")
    print("  >>> [小结] 负数索引表示从右往左数，-1 是最后一个\n")


def demo_list_comprehension():
    """列表推导式：一行写出「对可迭代对象做变换/过滤」的新列表"""
    print("  >>> [公式] [ 表达式 for 变量 in 可迭代对象 if 条件 ]")
    squares = [x ** 2 for x in range(1, 6)]
    print(f"  [x**2 for x in range(1,6)]  -> {squares}")
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"  [x for x in range(10) if x%2==0]  -> {evens}")
    matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
    print(f"  二维列表（3x3 矩阵）: {matrix}")
    print("  >>> [小结] 外层 for 对应行，内层 for 对应列\n")


def demo_dict_and_set_comprehension():
    """字典推导式、集合推导式：同样思路，得到 dict 或 set"""
    print("  >>> [字典推导] { key表达式: value表达式 for ... in ... }")
    d = {k: k ** 2 for k in range(1, 5)}
    print("  {k: k**2 for k in range(1,5)}  ->", d)
    print("  >>> [集合推导] { 表达式 for ... in ... }，自动去重")
    uniq = {c.lower() for c in "Hello"}
    print(f"  {{c.lower() for c in 'Hello'}}  -> {uniq}")
    print("  >>> [小结] 集合无序且不重复，适合去重、成员检测\n")


if __name__ == "__main__":
    print("=== 1. 变量类型（动态类型）===\n")
    demo_types()

    print("=== 2. 切片 Slicing ===\n")
    demo_slicing()

    print("=== 3. 列表推导式 ===\n")
    demo_list_comprehension()

    print("=== 4. 字典/集合推导式 ===\n")
    demo_dict_and_set_comprehension()
