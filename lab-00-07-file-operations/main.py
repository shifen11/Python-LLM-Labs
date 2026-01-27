"""
lab-00-07-file-operations: 文件操作
"""

# ========== 写入文件 ==========
print("=== 写入文件 ===")
# 使用 with 语句，文件会自动关闭
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
print("文件已写入")

# ========== 读取文件 ==========
print("\n=== 读取整个文件 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容：")
    print(content)

print("\n=== 逐行读取 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"行：{line.strip()}")  # strip() 去除换行符

print("\n=== 读取所有行到列表 ===")
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"所有行：{lines}")

# ========== 追加内容 ==========
print("\n=== 追加内容 ===")
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的内容\n")
print("已追加内容")

# 验证追加结果
with open("demo.txt", "r", encoding="utf-8") as f:
    print("追加后的内容：")
    print(f.read())

# ========== 文件路径 ==========
print("\n=== 文件路径 ===")
import os

# 当前目录
current_dir = os.getcwd()
print(f"当前目录：{current_dir}")

# 检查文件是否存在
if os.path.exists("demo.txt"):
    print("demo.txt 存在")
    # 获取文件大小
    size = os.path.getsize("demo.txt")
    print(f"文件大小：{size} 字节")

# ========== 清理：删除测试文件 ==========
print("\n=== 清理测试文件 ===")
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("已删除 demo.txt")
