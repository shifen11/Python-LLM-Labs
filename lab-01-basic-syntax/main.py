"""
lab-01-basic-syntax: 变量类型、切片、列表推导式
"""


def demo_types():
    """动态类型：无需声明，同一变量可指向不同类型"""
    x = 42
    print(f"x = {x}, type = {type(x).__name__}")
    x = "hello"
    print(f"x = {x}, type = {type(x).__name__}")


def demo_slicing():
    """切片 [start:stop:step]"""
    s = "Python"
    print(f"'Python'[1:4]   = {s[1:4]!r}")   # yth
    print(f"'Python'[::2]   = {s[::2]!r}")   # Pto
    print(f"'Python'[::-1]  = {s[::-1]!r}")  # nohtyP
    lst = [0, 1, 2, 3, 4, 5]
    print(f"lst[-2:] = {lst[-2:]}")
    print(f"lst[:4]  = {lst[:4]}")


def demo_list_comprehension():
    """列表推导式"""
    squares = [x ** 2 for x in range(1, 6)]
    print(f"[x**2 for x in range(1,6)] = {squares}")
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"evens = {evens}")
    matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
    print(f"3x3 matrix = {matrix}")


def demo_dict_and_set_comprehension():
    """字典推导式、集合推导式"""
    d = {k: k ** 2 for k in range(1, 5)}
    print(f"dict comp = {d}")
    uniq = {c.lower() for c in "Hello"}
    print(f"set comp = {uniq}")


if __name__ == "__main__":
    print("=== 变量类型 ===")
    demo_types()
    print("\n=== 切片 ===")
    demo_slicing()
    print("\n=== 列表推导式 ===")
    demo_list_comprehension()
    print("\n=== 字典/集合推导式 ===")
    demo_dict_and_set_comprehension()
