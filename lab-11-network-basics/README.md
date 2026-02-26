# lab-11-network-basics - 网络编程基础

## 简介

本实验室介绍 Python 中的网络编程基础概念，包括 TCP/UDP 协议、Socket 编程、以及阻塞与非阻塞的概念。这些知识是理解 HTTP 协议（lab-13）、API 调用（lab-14）和异步网络编程（lab-12）的重要基础。

## 学习目标

- 理解 TCP 和 UDP 协议的基本区别
- 掌握 Socket 的基本概念
- 能够使用 Python 创建简单的 Socket 客户端
- 理解网络编程中的阻塞与非阻塞概念
- 了解网络通信的基本流程

## 运行方法

### 交互式演示

```bash
python main.py
```

### 练习题

```bash
python exercises.py
```

## 核心概念

### TCP vs UDP

| 特性 | TCP | UDP |
|-----|-----|-----|
| 连接性 | 面向连接 | 无连接 |
| 可靠性 | 可靠传输，保证数据完整 | 不可靠，可能丢包 |
| 速度 | 较慢（需三次握手） | 快速 |
| 用途 | HTTP、FTP、邮件 | 视频、游戏实时数据 |

### Socket

Socket 是网络编程的基础 API，用于不同主机间的进程通信。

```python
# 创建 TCP Socket
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 阻塞与非阻塞

- **阻塞模式**：函数调用会等待操作完成才返回
- **非阻塞模式**：函数调用立即返回，操作在后台进行

```python
# 设置非阻塞模式
sock.setblocking(False)
```

## 内容概览

### main.py 演示内容

1. **TCP/UDP 协议基础**
   - 协议对比
   - 适用场景

2. **Socket 基础**
   - 创建 Socket
   - TCP 客户端示例
   - UDP 客户端示例

3. **阻塞 vs 非阻塞**
   - 阻塞式网络操作
   - 非阻塞模式演示

4. **网络通信流程**
   - 客户端-服务器模型
   - 请求-响应模式

### exercises.py 练习题

1. 创建简单的 TCP 客户端
2. 创建简单的 UDP 客户端
3. 使用 socket 模块的基本操作

## 前置知识

- Python 基础语法
- 文件操作（lab-00-07）
- 函数式编程（lab-00-10）

## 后续关联

- **lab-12-asyncio-concurrency**：异步网络编程
- **lab-13-http-protocol**：HTTP 协议（基于 TCP）
- **lab-14-api-integration**：调用外部 API
- **lab-17-fastapi-service**：Web 服务开发

## 注意事项

- 某些演示需要网络连接
- Socket 编程涉及系统底层 API，跨平台时需注意
- 实际开发中通常使用高级库（如 httpx）而非直接使用 socket
