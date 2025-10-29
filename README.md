# ZDTrans

一个轻量级桌面翻译和文本润色工具，常驻系统托盘，通过全局快捷键快速调用。

## ✨ 特性

- 🚀 **全局快捷键**：在任何应用中选中文字，按下快捷键即可快速翻译或润色
- 💡 **即时弹窗**：翻译结果在鼠标附近弹出，无需切换窗口
- 🎨 **简洁美观**：半透明无边框窗口，不干扰工作流
- 🔧 **灵活配置**：支持多种API提供商（OpenAI、DeepL等）
- 🏷️ **关键词提示**：为AI提供专业领域关键词，提高翻译准确度
- 📦 **体积小巧**：常驻后台，资源占用极低
- 🖥️ **跨平台**：支持 Windows、macOS、Linux

## 📋 系统要求

- Python 3.8+
- 支持的操作系统：
  - Windows 10/11
  - macOS 10.14+
  - Linux (需要X11支持)

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/ZDTrans.git
cd ZDTrans
```

### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置API

#### 方式 1：使用配置向导（推荐）

```bash
python setup_volcengine.py
```

按照提示输入你的火山方舟 API Key 即可。

#### 方式 2：手动配置

复制配置文件模板：

```bash
cp config.json.example config.json
```

编辑 `config.json`，填入你的API Key：

```json
{
  "api": {
    "provider": "volcengine",
    "api_key": "your-api-key-here",
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "model": "doubao-pro-32k"
  }
}
```

> 💡 **支持的 API 提供商**: OpenAI、火山方舟(豆包)、DeepL、Claude
>
> 💡 **模型名称**: 可使用通用名称（如 `doubao-pro-32k`）或完整版本名称（如 `doubao-1-5-lite-32k-250115`）
>
> 查看 [火山方舟配置指南](docs/VOLCENGINE.md) 了解详细信息

### 5. 运行程序

```bash
python main.py
```

程序会打开一个主窗口，显示运行状态和翻译历史。

💡 **提示**：
- 主窗口可以随时关闭，程序继续在后台运行
- 通过托盘图标可以重新打开主窗口
- macOS 用户：托盘图标在屏幕右上角（蓝色圆形带字母 T）

详见 [主窗口使用指南](docs/MAIN_WINDOW_GUIDE.md)

## ⌨️ 默认快捷键

- **Ctrl + Q**: 翻译选中文本（无选中文本时显示主窗口）
- **Ctrl + Shift + Q**: 润色选中文本

> 注意：macOS 用户需要在"系统偏好设置 > 安全性与隐私 > 辅助功能"中授权本程序。

💡 **提示**: 如需修改快捷键，可编辑 `config.json` 文件中的 `hotkey` 配置项。

## 🏷️ 关键词配置（提高翻译准确度）

在翻译专业领域文章时，可以设置关键词帮助 AI 理解上下文：

**示例：翻译机器学习论文**
```
关键词：深度学习, 神经网络, Transformer, 反向传播
```

**效果**：
- "training" → 训练（而不是"培训"）
- "model" → 模型（而不是"模特"）
- "architecture" → 架构（而不是"建筑"）

**配置方法**：
1. 点击系统托盘图标 → 设置
2. 在"关键词"输入框中输入专业术语（用逗号分隔）
3. 点击保存

详细说明请查看 [关键词使用指南](docs/KEYWORDS_GUIDE.md)

## 🛠️ 开发指南

项目结构详见 [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

### 开发环境设置

```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行测试
python -m pytest tests/
```

## 📦 打包发布

使用 PyInstaller 打包成独立可执行文件：

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包
pyinstaller build/build.spec
```

打包后的文件在 `dist/` 目录下。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 鸣谢

- [PySide6](https://doc.qt.io/qtforpython/) - Qt6 Python绑定
- [pynput](https://pynput.readthedocs.io/) - 全局键盘监听
- [pyperclip](https://github.com/asweigart/pyperclip) - 剪贴板操作

## 📞 联系方式

- 作者：Your Name
- Email: <your.email@example.com>
- GitHub: [@yourusername](https://github.com/yourusername)

---

⭐ 如果这个项目对你有帮助，请给个星标支持一下！
