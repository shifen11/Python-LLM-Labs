"""
lab-00-07-file-operations: 文件操作

运行时会展示：with 打开文件、'r'/'w'/'a' 模式、read/readlines、write、以及 os 路径与清理。
"""

import os

print("=== 1. 写入文件（'w' 模式，会覆盖）===\n")
print("  >>> [说明] with open(..., 'w') as f: 退出 with 时自动关闭文件")
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
print("  >>> [触发] 已写入 demo.txt，with 块结束即关闭文件\n")

print("=== 2. 读取整个文件（'r' 模式）===\n")
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("  文件内容：")
print(content)

print("=== 3. 逐行读取（文件对象可迭代）===\n")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  行: {line.strip()}")

print("\n=== 4. 读取所有行到列表 readlines() ===\n")
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"  readlines() -> {lines}\n")

print("=== 5. 追加内容（'a' 模式）===\n")
print("  >>> [说明] 'a' 在文件末尾追加，不覆盖")
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的内容\n")
with open("demo.txt", "r", encoding="utf-8") as f:
    print("  追加后的内容：")
    print(f.read())

print("=== 6. 文件路径（os）===\n")
print(f"  >>> [说明] os.getcwd() 当前目录；os.path.exists() 是否存在；os.path.getsize() 大小")
print(f"  当前目录: {os.getcwd()}")
print(f"  demo.txt 存在: {os.path.exists('demo.txt')}")
if os.path.exists("demo.txt"):
    print(f"  文件大小: {os.path.getsize('demo.txt')} 字节\n")

print("=== 7. 清理测试文件 ===\n")
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("  >>> [触发] 已删除 demo.txt")
