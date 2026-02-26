#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-11-network-basics - 练习题

请完成以下练习题，完成后运行本文件验证你的答案。
注意：某些练习需要网络连接。
"""

import socket

# ========== 练习 1: 创建 TCP Socket ==========

print("=" * 50)
print("练习 1: 创建 TCP Socket")
print("=" * 50)

# TODO: 创建一个 TCP Socket
# 提示：使用 socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"创建的 Socket 类型: {tcp_socket.type}")
print(f"是否为阻塞模式: {tcp_socket.getblocking()}")

# 验证
assert tcp_socket.type == socket.SOCK_STREAM, "未正确创建 TCP Socket"
tcp_socket.close()
print("✓ 练习 1 通过!\n")


# ========== 练习 2: 创建 UDP Socket ==========

print("=" * 50)
print("练习 2: 创建 UDP Socket")
print("=" * 50)

# TODO: 创建一个 UDP Socket
# 提示：使用 socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"创建的 Socket 类型: {udp_socket.type}")

# 验证
assert udp_socket.type == socket.SOCK_DGRAM, "未正确创建 UDP Socket"
udp_socket.close()
print("✓ 练习 2 通过!\n")


# ========== 练习 3: 设置非阻塞模式 ==========

print("=" * 50)
print("练习 3: 设置非阻塞模式")
print("=" * 50)

# TODO: 创建一个 Socket 并设置为非阻塞模式
# 提示：使用 setblocking(False)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(False)

is_blocking = sock.getblocking()

print(f"Socket 是否为阻塞模式: {is_blocking}")
print(f"预期结果: False（非阻塞）")

# 验证
assert is_blocking == False, "未正确设置非阻塞模式"
sock.close()
print("✓ 练习 3 通过!\n")


# ========== 练习 4: 检查端口开放状态 ==========

print("=" * 50)
print("练习 4: 检查端口开放状态")
print("=" * 50)

def check_port_open(host, port, timeout=2):
    """
    检查指定主机的端口是否开放

    参数:
        host: 主机地址（如 "127.0.0.1"）
        port: 端口号（整数）
        timeout: 超时时间（秒）

    返回:
        bool: True 表示端口开放，False 表示端口关闭
    """
    # TODO: 完成函数实现
    # 提示：
    # 1. 创建 socket
    # 2. 设置超时
    # 3. 使用 connect_ex 尝试连接
    # 4. 连接成功返回 True，失败返回 False
    # 5. 记得关闭 socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# 测试函数（测试一个通常不开放的高端口）
is_open = check_port_open("127.0.0.1", 65000)
print(f"端口 65000 是否开放: {is_open}")
print(f"预期结果: False（通常高端口是关闭的）")

# 验证函数逻辑正确（检查是否返回布尔值）
assert isinstance(is_open, bool), "函数应返回布尔值"
print("✓ 练习 4 通过!\n")


# ========== 练习 5: DNS 解析 ==========

print("=" * 50)
print("练习 5: DNS 解析")
print("=" * 50)

# TODO: 使用 socket.gethostbyname 解析域名
# 提示：socket.gethostbyname("www.baidu.com")
try:
    ip = socket.gethostbyname("www.baidu.com")
    print(f"www.baidu.com 的 IP 地址: {ip}")

    # 验证是否是有效的 IP 地址格式
    parts = ip.split('.')
    assert len(parts) == 4, "IP 地址格式不正确"
    for part in parts:
        assert 0 <= int(part) <= 255, "IP 地址范围不正确"

    print("✓ 练习 5 通过!\n")
except socket.gaierror:
    print("DNS 解析失败（可能网络不可用），跳过验证\n")


# ========== 练习 6: Socket 地址元组 ==========

print("=" * 50)
print("练习 6: Socket 地址元组")
print("=" * 50)

# TODO: 创建一个 Socket 地址元组，表示 127.0.0.1:8080
# 提示：address = (host, port)
address = ("127.0.0.1", 8080)

print(f"地址元组: {address}")
print(f"主机: {address[0]}")
print(f"端口: {address[1]}")

# 验证
assert isinstance(address, tuple), "地址应为元组"
assert len(address) == 2, "地址元组应包含两个元素"
assert address[0] == "127.0.0.1", "主机地址不正确"
assert address[1] == 8080, "端口号不正确"
print("✓ 练习 6 通过!\n")


# ========== 练习 7: TCP 客户端基本流程 ==========

print("=" * 50)
print("练习 7: TCP 客户端基本流程")
print("=" * 50)

# TODO: 填写 TCP 客户端的基本步骤（用中文）
tcp_client_steps = [
    "创建 Socket",
    "连接到服务器 (connect)",
    "发送数据 (send)",
    "接收数据 (recv)",
    "关闭连接 (close)",
]

print("TCP 客户端的基本步骤:")
for i, step in enumerate(tcp_client_steps, 1):
    print(f"  {i}. {step}")

# 验证
assert len(tcp_client_steps) == 5, "应包含 5 个步骤"
print("✓ 练习 7 通过!\n")


print("=" * 50)
print("所有练习完成！")
print("=" * 50)
