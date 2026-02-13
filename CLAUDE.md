# CLAUDE.md

本文档为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

Python-LLM-Labs 是一个教育性仓库，通过渐进式实验室结构学习 Python 基础知识，重点关注 AI/LLM 应用。项目分为 4 个阶段：

- **第零阶段**：Python 基础入门（labs 00-01 至 00-09）- 零基础入门
- **第一阶段**：Pythonic 基础（labs 01 至 05）- 从 Java 过渡到 Python 风格
- **第二阶段**：工程化与数据处理（labs 06, 08 至 10）- NumPy、Pandas、Pydantic
- **第三阶段**：并发与网络编程（labs 11 至 15）- asyncio、API 集成、测试、数据库、FastAPI
- **第四阶段**：LLM 应用（labs 16 至 18）- OpenAI SDK、向量数据库、LangChain RAG

## 实验室结构

每个实验室都遵循一致的模式：
- `README.md` - 中文文档，解释概念和运行方法
- `main.py` - 交互式演示脚本，带有教育性注释
- `exercises.py` - 自包含的练习，包含预期输出用于验证

注意：实验室 07（依赖管理）是个例外 - 没有 `main.py`，只有练习和文档。

## 运行实验室

标准实验室：
```bash
cd lab-XX-<名称>
python main.py
```

练习：
```bash
cd lab-XX-<名称>
python exercises.py
```

测试实验室（lab-13-testing-basics）：
```bash
cd lab-13-testing-basics
pytest
pytest test_example.py -v  # 详细输出
```

FastAPI 服务（lab-15-fastapi-service）：
```bash
cd lab-15-fastapi-service
uvicorn main:app --reload
# 然后访问 http://127.0.0.1:8000 和 http://127.0.0.1:8000/docs
```

注意：FastAPI 实验室的 `main.py` 也可以直接用 `python main.py` 运行 - 它包含启动 uvicorn 服务器的回退逻辑。

## 依赖管理

所有依赖项都通过根目录的 `requirements.txt` 管理。设置环境：
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

依赖项按阶段组织（见文件注释中的映射）。

## 架构说明

- **教学设计**：所有代码都为学习设计 - 包含大量中文注释解释概念，使用 `>>> [说明]` 标记解释，`>>> [触发]` 标记输出触发
- **独立性**：每个实验室都可以独立运行
- **渐进难度**：实验室按顺序编号，在各阶段内相互依赖
- **语言**：所有文档和注释都是中文

## 代码风格

- Python 3.10+
- 4 空格缩进（不用 Tab）
- 优先使用中文注释（符合项目教育性质）
- 在需要教育意义的地方使用类型提示（如 `def rough_token_count(text: str) -> int:`）