#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-11-network-basics - 网络编程基础

本脚本演示 Python 网络编程的基础概念。
注意：某些演示需要网络连接。
"""

import socket
import time

# >>> [说明] 网络编程是现代应用开发的核心
# 从本地的文件操作跨越到网络上的数据交换


# ========== 1. TCP vs UDP 协议 ==========

print("=" * 50)
print("1. TCP vs UDP 协议")
print("=" * 50)

print("""
TCP (Transmission Control Protocol):
- 面向连接，需要三次握手建立连接
- 可靠传输，保证数据完整性和顺序
- 有流量控制和拥塞控制
- 适用于：HTTP、FTP、SMTP、SSH

UDP (User Datagram Protocol):
- 无连接，直接发送数据
- 不可靠，可能丢包、乱序
- 开销小，速度快
- 适用于：视频流、在线游戏、DNS查询

对比示例:
- 网页浏览：使用 TCP（需要确保所有数据都正确传输）
- 视频直播：使用 UDP（偶尔丢包不影响观看体验）
""")

# Python 中的协议类型常量
print("Python socket 模块中的协议类型:")
print(f"  TCP: {socket.SOCK_STREAM} (流式套接字)")
print(f"  UDP: {socket.SOCK_DGRAM} (数据报套接字)")


# ========== 2. Socket 基础 ==========

print("\n" + "=" * 50)
print("2. Socket 基础")
print("=" * 50)

# >>> [说明] Socket 是网络编程的基础 API
# >>> [说明] Socket 是一个端点，包含了 IP 地址和端口号

# Socket 地址族（Address Family）
print("Socket 地址族（Address Family）:")
print(f"  AF_INET (IPv4): {socket.AF_INET}")
print(f"  AF_INET6 (IPv6): {socket.AF_INET6}")
print(f"  AF_UNIX (本地): {socket.AF_UNIX}")

# Socket 类型
print("\nSocket 类型（Socket Type）:")
print(f"  SOCK_STREAM (TCP): {socket.SOCK_STREAM}")
print(f"  SOCK_DGRAM (UDP): {socket.SOCK_DGRAM}")

# 创建 Socket 的基本语法
print("\n创建 Socket:")
print("  # TCP Socket")
print("  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)")
print("  # UDP Socket")
print("  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)")


# ========== 3. TCP 客户端示例 ==========

print("\n" + "=" * 50)
print("3. TCP 客户端示例")
print("=" * 50)

# >>> [说明] TCP 客户端的基本流程：
# 1. 创建 socket
# 2. 连接到服务器 (connect)
# 3. 发送数据 (send)
# 4. 接收数据 (recv)
# 5. 关闭连接 (close)

def tcp_client_demo(host, port, request):
    """TCP 客户端演示"""
    try:
        # 1. 创建 TCP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. 设置超时（避免无限等待）
        sock.settimeout(5)

        # 3. 连接到服务器
        print(f"  >>> [触发] 连接到 {host}:{port}")
        sock.connect((host, port))

        # 4. 发送数据
        print(f"  >>> [触发] 发送请求: {request}")
        sock.sendall(request.encode('utf-8'))

        # 5. 接收数据
        response = sock.recv(4096)
        print(f"  >>> [触发] 收到响应（{len(response)} 字节）")
        print(f"  响应前 100 字符: {response[:100].decode('utf-8', errors='ignore')}")

        return response

    except socket.timeout:
        print(f"  [错误] 连接超时")
        return None
    except Exception as e:
        print(f"  [错误] {e}")
        return None
    finally:
        sock.close()

# 使用公共 HTTP 服务演示 TCP
print("使用 HTTP 协议演示 TCP 连接:")
# >>> [说明] HTTP 基于 TCP，我们通过 HTTP 来演示 TCP 连接
# 使用 httpbin.org 的公共 API
result = tcp_client_demo("httpbin.org", 80, "GET /get HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")


# ========== 4. UDP 客户端示例 ==========

print("\n" + "=" * 50)
print("4. UDP 客户端示例")
print("=" * 50)

def udp_client_demo(host, port, message):
    """UDP 客户端演示"""
    try:
        # 1. 创建 UDP Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 2. 设置超时
        sock.settimeout(5)

        # 3. UDP 不需要连接，直接发送数据
        print(f"  >>> [触发] 发送 UDP 数据到 {host}:{port}")
        sock.sendto(message.encode('utf-8'), (host, port))

        # 4. 接收数据
        try:
            data, addr = sock.recvfrom(4096)
            print(f"  >>> [触发] 收到来自 {addr} 的响应")
            return data
        except socket.timeout:
            print("  [说明] UDP 是无连接的，可能没有响应")
            return None

    except Exception as e:
        print(f"  [错误] {e}")
        return None
    finally:
        sock.close()

# UDP 演示：向 DNS 服务器发送查询
# 注意：这里使用的是简化的演示，实际 DNS 查询需要构造特定的数据包
print("UDP 协议演示:")
print("  >>> [说明] UDP 不需要建立连接，可以直接发送数据")
print("  >>> [说明] DNS 查询就是基于 UDP 的典型应用")

# >>> [说明] DNS 端口是 53，但演示需要构造正确的 DNS 查询包
# 这里只展示 UDP Socket 的创建和使用
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"  创建 UDP Socket 成功: {udp_sock}")
udp_sock.close()


# ========== 5. 阻塞 vs 非阻塞 ==========

print("\n" + "=" * 50)
print("5. 阻塞 vs 非阻塞")
print("=" * 50)

# >>> [说明] 阻塞模式：函数调用会等待操作完成才返回
# >>> [说明] 非阻塞模式：函数调用立即返回，操作在后台进行

print("""
阻塞模式（默认）:
  - recv() 会一直等待直到有数据到达
  - connect() 会等待直到连接建立
  - send() 可能会等待缓冲区有空间

非阻塞模式:
  - recv() 立即返回，如果没有数据则抛出异常
  - connect() 立即返回，连接在后台建立
  - send() 立即返回，实际发送由操作系统处理
""")

# 演示阻塞模式
print("演示阻塞模式:")
blocking_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"  默认阻塞状态: {blocking_sock.getblocking()}")

# 演示非阻塞模式
print("\n演示非阻塞模式:")
nonblocking_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nonblocking_sock.setblocking(False)
print(f"  设置非阻塞后: {nonblocking_sock.getblocking()}")

# 尝试在非阻塞模式下接收（会抛出异常）
print("  尝试在非阻塞模式下接收数据:")
try:
    # UDP socket 可以直接接收（即使未连接）
    # 使用 UDP socket 演示非阻塞
    nonblocking_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nonblocking_udp.setblocking(False)
    nonblocking_udp.recv(1024)
except BlockingIOError as e:
    print(f"  抛出 BlockingIOError（预期行为）")
except OSError as e:
    print(f"  抛出 OSError（预期行为）: 套接字未连接或无数据")
finally:
    nonblocking_sock.close()
    blocking_sock.close()


# ========== 6. 网络通信模型 ==========

print("\n" + "=" * 50)
print("6. 网络通信模型")
print("=" * 50)

print("""
客户端-服务器模型:
  1. 服务器:
     - 创建 Socket
     - 绑定地址和端口 (bind)
     - 监听连接 (listen)
     - 接受连接 (accept)
     - 处理请求

  2. 客户端:
     - 创建 Socket
     - 连接到服务器 (connect)
     - 发送请求
     - 接收响应

请求-响应模式:
  客户端           网络           服务器
    |               |               |
    |-- 请求 ------>|              |
    |               |------ 请求 ->|
    |               |              |
    |               |<----- 响应 --|
    |<-- 响应 ------|               |
""")

# 演示获取本机地址
print("获取本机网络信息:")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"  主机名: {hostname}")
print(f"  IP 地址: {ip_address}")

# 演示 DNS 解析
print("\n演示 DNS 解析:")
try:
    www_ip = socket.gethostbyname("www.baidu.com")
    print(f"  www.baidu.com -> {www_ip}")
except socket.gaierror as e:
    print(f"  DNS 解析失败: {e}")


# ========== 7. 网络编程中的常见概念 ==========

print("\n" + "=" * 50)
print("7. 网络编程中的常见概念")
print("=" * 50)

print("""
端口号（Port）:
  - 0-1023: 系统端口（需要管理员权限）
  - 1024-49151: 注册端口
  - 49152-65535: 动态/私有端口

  常见端口:
    - 21: FTP
    - 22: SSH
    - 80: HTTP
    - 443: HTTPS
    - 3306: MySQL
    - 5432: PostgreSQL

IP 地址:
  - IPv4: 如 192.168.1.1（32 位）
  - IPv6: 如 2001:db8::1（128 位）

套接字地址:
  - IPv4: (host, port) 元组
  - IPv6: (host, port, flowinfo, scopeid) 元组
""")

# 演示地址元组
tcp_address = ("127.0.0.1", 8080)
print(f"\nTCP 地址元组: {tcp_address}")
print(f"  主机: {tcp_address[0]}")
print(f"  端口: {tcp_address[1]}")


# ========== 8. 实用工具函数 ==========

print("\n" + "=" * 50)
print("8. 实用工具函数")
print("=" * 50)

def check_port_open(host, port, timeout=2):
    """检查端口是否开放"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# 检查常见的本地端口
ports_to_check = [80, 443, 8080, 3000]
print("检查常见端口是否开放（扫描 localhost）:")
for port in ports_to_check:
    is_open = check_port_open("127.0.0.1", port)
    status = "开放" if is_open else "关闭"
    print(f"  端口 {port}: {status}")


print("\n" + "=" * 50)
print("实验室演示完成！")
print("=" * 50)
print("""
重要提示:
  1. 实际开发中通常使用高级库（如 httpx、requests）
  2. Socket 编程涉及系统底层 API，跨平台需注意
  3. 后续学习:
     - lab-12: asyncio 异步网络编程
     - lab-13: HTTP 协议详解
     - lab-14: API 集成（使用 httpx）
     - lab-17: FastAPI 服务开发
""")
