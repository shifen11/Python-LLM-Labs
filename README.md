# Python-LLM-Labs

一个 **Python 学习仓库**，采用「lab + demo」形式，每个 lab 对应一个知识点的小示例，方便按主题练习与查阅。

结构参考 [SpringBoot-Labs](https://github.com/yudaocode/SpringBoot-Labs)：在一个项目中写下一个个 demo，归类每个知识点。

**适合人群：**
- 🟢 **0 基础学习者**：从第零阶段开始，循序渐进
- 🟡 **有 Java 背景的开发者**：可直接从第一阶段开始，学习 Pythonic 特性

---

## 第零阶段：Python 基础入门（0 基础必学）

目标：掌握 Python 最基础的语法和概念，为后续学习打下坚实基础。

| Lab | 主题 | 说明 |
|-----|------|------|
| [lab-00-01-first-program](./lab-00-01-first-program) | 第一个 Python 程序 | Hello World、print、注释、缩进 |
| [lab-00-02-variables-types](./lab-00-02-variables-types) | 变量与基本数据类型 | int、float、str、bool |
| [lab-00-03-control-flow](./lab-00-03-control-flow) | 控制流 | if/else、for、while、break、continue |
| [lab-00-04-functions-basic](./lab-00-04-functions-basic) | 函数基础 | 定义、调用、参数、返回值 |
| [lab-00-05-data-structures](./lab-00-05-data-structures) | 数据结构基础 | list、tuple、dict、set |
| [lab-00-06-string-operations](./lab-00-06-string-operations) | 字符串操作 | 格式化、常用方法 |
| [lab-00-07-file-operations](./lab-00-07-file-operations) | 文件操作 | 读写文本文件 |
| [lab-00-08-exception-handling](./lab-00-08-exception-handling) | 异常处理 | try/except/finally |
| [lab-00-09-oop-basics](./lab-00-09-oop-basics) | 面向对象基础 | 类、对象、继承、多态 |

---

## 第一阶段：Pythonic 基础（针对 Java 开发者）

目标：改掉「用 Java 写 Python」的习惯，理解 Python 的动态特性和语法糖。

| Lab | 主题 | 说明 |
|-----|------|------|
| [lab-01-basic-syntax](./lab-01-basic-syntax) | 变量类型、切片、列表推导式 | 基础语法与 Pythonic 写法 |
| [lab-06-typing-hints](./lab-06-typing-hints) | 类型注解 | typing 模块、类型提示 |
| [lab-02-functions-advanced](./lab-02-functions-advanced) | 解构赋值、`*args` / `**kwargs` | 函数进阶 |
| [lab-03-decorators](./lab-03-decorators) | 装饰器（Python 版 AOP） | 非常重要 |
| [lab-04-context-managers](./lab-04-context-managers) | `with` 与上下文管理器 | 对比 Java try-with-resources |
| [lab-05-magic-methods](./lab-05-magic-methods) | 魔术方法（`__call__`, `__init__` 等） | 理解 Python 的「协议」 |

---

## 第二阶段：工程化与数据预处理

AI 开发中，数据处理占大部分时间。

| Lab | 主题 | 说明 |
|-----|------|------|
| [lab-07-dependency-management](./lab-07-dependency-management) | 虚拟环境与包管理 | Conda / venv |
| [lab-08-numpy-basics](./lab-08-numpy-basics) | 多维数组与矩阵运算 | 大模型底层数学基础 |
| [lab-09-pandas-dataframes](./lab-09-pandas-dataframes) | 表格化数据清洗与分析 | Pandas |
| [lab-10-pydantic-validation](./lab-10-pydantic-validation) | Pydantic 类型校验与模型定义 | 类似 Java Bean 校验 |

---

## 第三阶段：并发与网络编程

大模型推理多为高延迟 IO，需要掌握异步与 HTTP 调用。

| Lab | 主题 | 说明 |
|-----|------|------|
| [lab-11-asyncio-concurrency](./lab-11-asyncio-concurrency) | `async` / `await` 异步模型 | asyncio |
| [lab-12-api-integration](./lab-12-api-integration) | 调用外部 API | httpx / requests |
| [lab-13-testing-basics](./lab-13-testing-basics) | 测试基础 | pytest、fixture |
| [lab-14-database-basics](./lab-14-database-basics) | 数据库操作 | SQLAlchemy ORM |
| [lab-15-fastapi-service](./lab-15-fastapi-service) | 高性能 Web 接口 | 类似 Spring Boot 控制层 |

---

## 第四阶段：大模型（LLM）专项应用

将 Python 技能转化为 AI 应用能力。

| Lab | 主题 | 说明 |
|-----|------|------|
| [lab-16-openai-sdk](./lab-16-openai-sdk) | 流式输出与 Token 计算 | OpenAI SDK |
| [lab-17-vector-databases](./lab-17-vector-databases) | 向量数据库 | FAISS / ChromaDB |
| [lab-18-langchain-rag](./lab-18-langchain-rag) | 简单 RAG 系统 | 检索增强生成 |

---

## 快速开始

```bash
# 克隆后进入项目
cd Python-LLM-Labs

# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 安装根依赖（用于后续 lab）
pip install -r requirements.txt

# 运行某个 lab（0基础从 lab-00-01 开始）
cd lab-00-01-first-program && python main.py
# 或
cd lab-01-basic-syntax && python main.py
```

每个 lab 目录下均有 `README.md` 与可运行的 `main.py`（或等价入口），可直接 `python main.py` 体验。

---

## 环境要求

- Python 3.10+
- 建议使用 venv 或 Conda 管理环境

## License

MIT
