"""
lab-00-08-exception-handling: 异常处理

运行时会展示：try/except 捕获特定异常、as e 获取异常信息、finally、以及 raise 主动抛出。
"""

print("=== 1. 基本 try / except ===\n")
print("  >>> [说明] 把可能出错的代码放 try 里，except 异常类型: 捕获该类型")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  >>> [触发] 捕获到 ZeroDivisionError：不能除以 0！\n")

print("=== 2. 捕获多种异常 ===\n")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  >>> [触发] 除数不能为 0")
        return None
    except TypeError:
        print("  >>> [触发] 参数类型不正确")
        return None


print("  divide(10, 2) ->", divide(10, 2))
print("  divide(10, 0) ->", divide(10, 0))
print("  divide(10, 'a') ->", divide(10, "a"))
print()

print("=== 3. 获取异常信息（except ... as e）===\n")
print("  >>> [说明] as e 可拿到异常实例，type(e).__name__ 为类型名，str(e) 为信息")
try:
    num = int("abc")
except ValueError as e:
    print(f"  >>> [触发] 异常类型: {type(e).__name__}, 信息: {e}\n")

print("=== 4. 捕获所有异常（Exception）===\n")
try:
    data = [1, 2, 3]
    print(data[10])
except Exception as e:
    print(f"  >>> [触发] 发生错误: {type(e).__name__}: {e}\n")

print("=== 5. finally：无论是否异常都会执行 ===\n")
print("  >>> [说明] 常用于释放资源（关文件、关连接）")


def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("  文件读取成功")
            return content
    except FileNotFoundError:
        print(f"  >>> [触发] 文件 '{filename}' 不存在")
        return None
    finally:
        print("  >>> [触发 finally] 无论成功或失败都会执行这里")


read_file_safe("不存在的文件.txt")
print()

print("=== 6. 主动抛出异常 raise ===\n")
print("  >>> [说明] raise ValueError('消息') 可主动抛异常，由上层 try/except 处理")


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return f"年龄有效：{age}"


try:
    print("  check_age(25) ->", check_age(25))
    print("  check_age(-5) ->", check_age(-5))
except ValueError as e:
    print(f"  >>> [触发] 捕获到错误: {e}\n")

print("=== 7. 常见异常类型速览 ===\n")
print("  >>> [说明] ValueError/TypeError/IndexError/KeyError 等，按需捕获")
for exc_name, code, msg in [
    ("ValueError", "int('abc')", "值转换失败"),
    ("TypeError", "'hello' + 123", "类型不匹配"),
    ("IndexError", "lst[10]", "索引越界"),
    ("KeyError", "d['age']", "字典中不存在该键"),
]:
    try:
        if "int(" in code:
            int("abc")
        elif "+" in code:
            "hello" + 123
        elif "lst" in code:
            lst = [1, 2, 3]
            _ = lst[10]
        else:
            d = {"name": "Alice"}
            _ = d["age"]
    except Exception as e:
        print(f"  {exc_name}: {msg}")
