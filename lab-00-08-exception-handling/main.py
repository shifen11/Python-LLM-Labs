"""
lab-00-08-exception-handling: 异常处理
"""

# ========== 基本异常处理 ==========
print("=== 基本异常处理 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误：不能除以0！")

# ========== 捕获多个异常 ==========
print("\n=== 捕获多个异常 ===")
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为0")
        return None
    except TypeError:
        print("错误：参数类型不正确")
        return None

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / 'a' = {divide(10, 'a')}")

# ========== 获取异常信息 ==========
print("\n=== 获取异常信息 ===")
try:
    num = int("abc")
except ValueError as e:
    print(f"捕获到异常：{type(e).__name__}")
    print(f"错误信息：{e}")

# ========== 捕获所有异常 ==========
print("\n=== 捕获所有异常 ===")
try:
    # 可能出错的代码
    data = [1, 2, 3]
    print(data[10])  # 索引越界
except Exception as e:
    print(f"发生错误：{type(e).__name__}: {e}")

# ========== else 和 finally ==========
print("\n=== else 和 finally ===")
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("文件读取成功")
            return content
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        return None
    except Exception as e:
        print(f"发生其他错误：{e}")
        return None
    finally:
        print("无论成功或失败，都会执行这里")

# 测试
read_file_safe("不存在的文件.txt")

# ========== 主动抛出异常 ==========
print("\n=== 主动抛出异常 ===")
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return f"年龄有效：{age}"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print(f"捕获到错误：{e}")

# ========== 常见异常类型 ==========
print("\n=== 常见异常类型 ===")
# ValueError：值错误
try:
    int("abc")
except ValueError:
    print("ValueError: 值转换失败")

# TypeError：类型错误
try:
    "hello" + 123
except TypeError:
    print("TypeError: 类型不匹配")

# IndexError：索引错误
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("IndexError: 索引越界")

# KeyError：键错误
try:
    d = {"name": "Alice"}
    print(d["age"])
except KeyError:
    print("KeyError: 字典中不存在该键")
