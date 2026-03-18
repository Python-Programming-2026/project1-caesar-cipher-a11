# Caesar Cipher Tool (凯撒密码处理工具)

本项目是一个基于 Python 实现的命令行工具，旨在完成字符串及文本文件的凯撒密码加密与解密任务。项目结构遵循现代 Python 工程标准，并针对大文件处理进行了性能优化。

## 功能特性

1. **文本加解密**：支持对任意长度的字符串进行位移处理。
2. **文件加解密**：支持对 `.txt` 格式文件进行处理，采用流式读写机制，确保低内存占用。
3. **大小写保留**：算法自动识别英文字符大小写，非英文字符（如标点、数字、中文）保持原样输出。
4. **命令行交互**：通过子命令（Sub-commands）模式提供清晰的操作入口。

## 项目结构说明

Plaintext

```
caesar-cipher-tool/
├── src/
│   └── caesar_cipher/
│       ├── __init__.py
│       ├── cipher.py        # 核心算法实现：包含字符位移及文本处理逻辑
│       ├── file_handler.py  # 文件处理实现：包含分块读取与字符映射表构建
│       └── cli.py           # 命令行接口：负责参数解析与指令分发
├── tests/                   # 单元测试：包含对核心逻辑的自动化校验
├── examples/                # 示例文件：供测试使用的样本数据
├── pyproject.toml           # 项目构建与依赖配置文件
└── README.md                # 项目技术文档
```

## 技术实现与 Python 知识点

本项目开发过程中应用了以下 Python 核心编程概念：

- **程序流程控制**：利用 `if-elif-else` 实现指令路由，使用 `for` 循环遍历字符流，并通过 `iter()` 函数配合 `lambda` 表达式实现高效的文件分块读取。
- **算术运算**：运用取模运算符 `%` 处理字母表的循环位移，确保偏移后的索引始终处于 0-25 范围内。
- **内置函数与数据类型**：
  - 使用 `ord()` 和 `chr()` 实现字符与 ASCII 码的互相转换。
  - 利用 `str.maketrans` 与 `translate` 构建映射表，提升批量字符替换的执行效率。
- **文件系统操作**：使用 `pathlib.Path` 进行路径管理，并通过 `with` 语句管理文件句柄，确保资源的可靠释放。
- **异常处理**：通过 `try-except` 块捕获潜在的文件缺失（FileNotFoundError）及参数错误。

## 安装与使用方法

### 运行环境

- Python 3.8 或更高版本
- 无第三方库依赖

### 操作示例

在项目根目录下，通过以下命令运行程序：

#### 1. 字符串加密

Bash

```
python -m src.caesar_cipher.cli encrypt "Hello World" --shift 3
```

#### 2. 字符串解密

Bash

```
python -m src.caesar_cipher.cli decrypt "Khoor Zruog" --shift 3
```

#### 3. 文本文件加密

Bash

```
python -m src.caesar_cipher.cli encrypt-file input.txt output.txt --shift 5
```

#### 4. 文本文件解密

Bash

```
python -m src.caesar_cipher.cli decrypt-file output.txt recovered.txt --shift 5
```