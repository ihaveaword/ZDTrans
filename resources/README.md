# Resources 资源文件

本目录包含应用程序所需的资源文件。

## 📁 目录结构

```text
resources/
├── icons/          # 图标文件
│   ├── tray.png    # 系统托盘图标 (建议尺寸: 16x16 或 32x32)
│   └── window.png  # 窗口图标 (建议尺寸: 64x64 或更大)
└── styles/         # 样式文件
    └── main.qss    # Qt样式表
```

## 🎨 图标要求

### 托盘图标 (tray.png)

- 尺寸：16x16 或 32x32 像素
- 格式：PNG (支持透明背景)
- 建议：简洁、清晰，在深色和浅色背景下都能看清

### 窗口图标 (window.png)

- 尺寸：64x64 或更大
- 格式：PNG (支持透明背景)

## 📝 使用说明

### 临时方案

在正式图标设计完成前，可以使用以下方式：

1. 使用在线工具生成简单图标
2. 从 [icons8.com](https://icons8.com) 等网站下载免费图标
3. 使用 emoji 转图标的方式

### 样式文件

`styles/main.qss` 文件用于自定义应用程序的外观。
Qt样式表语法类似CSS，可以自定义：

- 窗口背景色
- 字体样式
- 按钮样式
- 等等

## 🔗 参考资源

- Qt样式表文档: <https://doc.qt.io/qt-6/stylesheet.html>
- 免费图标: <https://icons8.com>
- 图标转换工具: <https://convertio.co/zh/>
