# lab-06-dependency-management

**虚拟环境与包管理**

## 知识点

- `python -m venv .venv`：创建虚拟环境
- `pip install -r requirements.txt`：从依赖文件安装
- `pip freeze > requirements.txt`：导出当前环境
- Conda：`conda create -n myenv python=3.11`、`conda activate myenv`

## 运行

本 lab 为操作指引，无 `main.py`。按 README 在项目根执行：

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
