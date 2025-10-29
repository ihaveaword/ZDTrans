# ZDTrans v1.0.0 - 首个稳定版本 🎉

**发布日期**: 2024-10-29

## ✨ 主要功能

- 🚀 **全局快捷键翻译** - 在任何应用中选中文字，按 Ctrl+Q 即可翻译
- ✨ **学术润色** - 使用 Ctrl+Shift+Q 润色学术文本
- 💡 **即时弹窗显示** - 翻译结果即刻呈现，不打断工作流
- 🏷️ **专业领域关键词** - 支持自定义关键词，提高术语翻译准确度
- 🎨 **简洁主窗口界面** - 实时查看运行状态和翻译历史
- 📦 **系统托盘常驻** - 后台运行，随时可用

## 📥 下载安装

### macOS

**下载**: [ZDTrans-v1.0.0-macOS.zip](https://github.com/YOUR_USERNAME/ZDTrans/releases/download/v1.0.0/ZDTrans-v1.0.0-macOS.zip) (39 MB)

**安装步骤**:
1. 下载并解压 `ZDTrans-v1.0.0-macOS.zip`
2. 将 `ZDTrans.app` 拖入"应用程序"文件夹
3. 首次运行时，右键点击应用 → 选择"打开"
4. 在"系统偏好设置 > 安全性与隐私 > 辅助功能"中授权

**系统要求**:
- macOS 10.13 或更高版本
- 约 40 MB 磁盘空间

### Windows (即将推出)

敬请期待！

### Linux (即将推出)

敬请期待！

## ⚙️ 快速配置

### 1. 配置 API Key

首次启动后：
1. 点击托盘图标 → "设置"（或按 Ctrl+Q 打开主窗口 → 点击"设置"）
2. 选择 API 提供商（Google Gemini / OpenAI / 火山方舟等）
3. 输入您的 API Key
4. 点击"保存"

### 2. 设置关键词（可选）

在设置界面的"关键词"输入框中，输入您的专业领域关键词，用逗号分隔：

```
深度学习, 神经网络, 机器学习, PyTorch, TensorFlow
```

这将帮助 AI 更准确地翻译专业术语。

### 3. 开始使用

1. 在任何应用中选中文字
2. 按 `Ctrl+Q` 翻译
3. 按 `Ctrl+Shift+Q` 润色
4. 翻译结果会在鼠标附近弹出

## 🎯 使用技巧

### 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl+Q` | 翻译选中文字（无选中时显示主窗口） |
| `Ctrl+Shift+Q` | 润色选中文字 |

### 自定义快捷键

编辑配置文件 `config.json`:

```json
{
  "hotkey": {
    "translate": "Cmd+T",
    "polish": "Cmd+P"
  }
}
```

### 关键词最佳实践

**计算机科学**:
```
深度学习, 神经网络, 机器学习, 算法, 数据结构
```

**医学**:
```
临床试验, 病理学, 药物代谢, 诊断, 治疗
```

**物理**:
```
量子力学, 相对论, 电磁场, 粒子物理, 热力学
```

## 📚 文档

- [快速开始指南](QUICK_START.md)
- [关键词使用指南](docs/KEYWORDS_GUIDE.md)
- [主窗口使用指南](docs/MAIN_WINDOW_GUIDE.md)
- [macOS 托盘问题排查](docs/MACOS_TRAY_TROUBLESHOOTING.md)

## 🐛 已知问题

### macOS
- 首次运行需要在"系统偏好设置"中授权辅助功能
- 托盘图标在某些 macOS 版本上可能不太明显（蓝色圆形）

### 通用
- 翻译长文本时可能需要等待几秒钟
- 某些应用（如 Terminal）的文本选择可能不被支持

## 🔧 故障排除

### 问题: 快捷键不工作
**解决方案**: 
1. 检查是否授予了辅助功能权限
2. 确保没有其他应用占用相同快捷键
3. 重启应用

### 问题: 翻译失败
**解决方案**:
1. 检查 API Key 是否正确
2. 检查网络连接
3. 查看主窗口的错误信息

### 问题: 找不到托盘图标
**解决方案**:
- 按 `Ctrl+Q`（不选中文字）可直接打开主窗口
- 托盘图标是蓝色圆形，在屏幕右上角

## 🙏 致谢

感谢以下开源项目:
- [PySide6](https://www.qt.io/qt-for-python) - GUI 框架
- [pynput](https://github.com/moses-palmer/pynput) - 全局快捷键
- [pyperclip](https://github.com/asweigart/pyperclip) - 剪贴板管理
- [google-generativeai](https://github.com/google/generative-ai-python) - Google Gemini API

## 📝 更新日志

### v1.0.0 (2024-10-29)

**新功能**:
- ✨ 全局快捷键翻译和润色
- 📱 可视化主窗口界面
- 🏷️ 关键词功能
- 🎨 系统托盘常驻
- 💡 即时弹窗显示

**改进**:
- 🍎 macOS 兼容性优化
- 🎨 简洁清晰的界面设计
- 📚 完善的文档

## 📞 反馈与支持

- 🐛 **报告问题**: [GitHub Issues](https://github.com/YOUR_USERNAME/ZDTrans/issues)
- 💡 **功能建议**: [GitHub Discussions](https://github.com/YOUR_USERNAME/ZDTrans/discussions)
- 📧 **联系邮箱**: your.email@example.com

## 📜 开源协议

MIT License - 详见 [LICENSE](LICENSE) 文件

---

**⭐ 如果觉得有用，请给项目点个 Star！**

[下载最新版本](https://github.com/YOUR_USERNAME/ZDTrans/releases/latest) | [查看文档](README.md) | [贡献代码](CONTRIBUTING.md)
