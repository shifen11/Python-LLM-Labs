"""
lab-05-magic-methods: __init__, __call__, __str__, __repr__, __len__, __getitem__
"""


class Greeter:
    def __init__(self, name):
        # 类似 Java 构造函数
        print(f"  >>> [触发 __init__]: 正在为 {name} 创建实例")
        self.name = name

    def __str__(self):
        # 类似 Java 的 toString()，面向用户
        print("  >>> [触发 __str__]: print 或 str() 调用了我")
        return f"Greeter({self.name})"

    def __repr__(self):
        # 面向开发者，!r 会调用 self.name 的 repr()
        print("  >>> [触发 __repr__]: repr() 调用了我")
        return f"Greeter(name={self.name!r})"

    def __call__(self, msg="Hello"):
        # 让实例像函数一样可以被 () 调用
        print(f"  >>> [触发 __call__]: 有人像调用函数一样调用了实例")
        return f"{msg}, {self.name}!"

class SimpleSeq:
    def __init__(self, data):
        print("[Init] 正在初始化数据...")
        self._data = list(data)

    def __len__(self):
        print("[Len] 被调用了，用于确定容器大小")
        return len(self._data)

    def __getitem__(self, key):
        print(f"[GetItem] 正在获取索引为 {key} 的元素")
        return self._data[key]

    def __iter__(self):
        """正统迭代协议：返回一个迭代器"""
        print("[Iter] 开启正统迭代模式！")
        # 直接利用 list 原生的迭代器
        return iter(self._data)


if __name__ == "__main__":
    print("=== 1. 初始化 ===")
    g = Greeter("World")

    print("\n=== 2. 打印与字符串转换 ===")
    # 这里 print(g) 也会触发 __str__
    print(f"str(g) 的结果是: {str(g)}")
    print(f"repr(g) 的结果是: {repr(g)}")

    print("\n=== 3. 实例调用 ===")
    # 像函数一样直接在变量名后加 ()
    print(f"调用 g(): {g()}")
    print(f"调用 g('Hi'): {g('Hi')}")

    s = SimpleSeq([10, 20])

    print("\n--- 执行 list(s) ---")
    result = list(s)

    print("\n--- 执行 s[0] ---")
    _ = s[0]
