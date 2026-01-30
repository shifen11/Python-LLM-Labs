"""
lab-02-functions-advanced: 解构赋值、*args、**kwargs

运行时会展示：解构怎么拆包、*args 如何收成元组、**kwargs 如何收成字典，以及组合时的顺序。
"""


def demo_unpacking():
    """解构赋值：把序列或可迭代对象「拆开」赋给多个变量"""
    print("  >>> [说明] 等号右边可以是元组、列表、甚至 range，左边用变量按位置接收")
    a, b = 1, 2
    print(f"  a, b = 1, 2  -> a={a}, b={b}")

    print("  >>> [说明] 用 *变量 可以「收尾」，中间多出来的全部放进这个列表")
    first, *rest, last = [1, 2, 3, 4, 5]
    print(f"  first, *rest, last = [1,2,3,4,5]  -> first={first}, rest={rest}, last={last}")

    print("  >>> [说明] 字典可以 .values() / .items() 解构")
    d = {"x": 10, "y": 20}
    x, y = d.values()
    print(f"  x, y = d.values()  -> x={x}, y={y}\n")


def greet(*names):
    """*args：在形参里写 *名字，多出来的「位置参数」会打包成元组"""
    print(f"  >>> [触发 *args] 收到 names = {names}，类型 = {type(names).__name__}")
    for n in names:
        print(f"    Hello, {n}!")
    print()


def config(**kwargs):
    """**kwargs：多出来的「关键字参数」会打包成字典"""
    print(f"  >>> [触发 **kwargs] 收到 kwargs = {kwargs}，类型 = {type(kwargs).__name__}")
    for k, v in kwargs.items():
        print(f"    {k} = {v}")
    print()


def mixed(a, b, *args, **kwargs):
    """组合顺序：固定参数 -> *args（多余位置）-> **kwargs（多余关键字）"""
    print("  >>> [触发 组合] 固定参数先占位，其余按顺序分配")
    print(f"    a = {a}, b = {b}")
    print(f"    *args  -> args = {args}")
    print(f"    **kwargs -> kwargs = {kwargs}\n")


if __name__ == "__main__":
    print("=== 1. 解构赋值 ===\n")
    demo_unpacking()

    print("=== 2. *args（不定长位置参数）===\n")
    print("  调用: greet('Alice', 'Bob')")
    greet("Alice", "Bob")

    print("=== 3. **kwargs（不定长关键字参数）===\n")
    print("  调用: config(host='localhost', port=8080, debug=True)")
    config(host="localhost", port=8080, debug=True)

    print("=== 4. 组合：固定参数 + *args + **kwargs ===\n")
    print("  调用: mixed(1, 2, 3, 4, foo='bar', baz=99)")
    mixed(1, 2, 3, 4, foo="bar", baz=99)
