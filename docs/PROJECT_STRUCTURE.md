# ZDTrans 项目结构说明

## 📁 项目概览

ZDTrans 是一个轻量级桌面翻译和文本润色工具，常驻系统托盘，通过全局快捷键快速调用。

## 🗂️ 目录结构

```text
ZDTrans/
├── main.py                 # 程序入口文件
├── requirements.txt        # Python依赖包列表
├── config.json            # 用户配置文件（API Key、快捷键等）
├── .gitignore             # Git忽略文件配置
├── README.md              # 项目说明文档
├── PROJECT_STRUCTURE.md   # 本文件 - 项目结构说明
│
├── venv/                  # Python虚拟环境（不纳入版本控制）
│
├── src/                   # 源代码目录
│   ├── __init__.py        # 包初始化文件
│   ├── tray.py            # 系统托盘管理模块
│   ├── hotkey.py          # 全局快捷键监听模块
│   ├── translator.py      # API调用模块（翻译/润色）
│   ├── popup.py           # 弹出窗口UI模块
│   ├── settings.py        # 设置界面模块
│   ├── clipboard.py       # 剪贴板操作模块
│   └── utils.py           # 工具函数模块
│
├── resources/             # 资源文件目录
│   ├── icons/             # 图标文件
│   │   ├── tray.png       # 托盘图标
│   │   └── window.png     # 窗口图标
│   ├── styles/            # 样式文件
│   │   └── main.qss       # Qt样式表
│   └── README.md          # 资源文件说明
│
├── build/                 # 打包构建目录
│   ├── build.spec         # PyInstaller配置文件
│   └── README.md          # 打包说明文档
│
├── tests/                 # 测试文件目录（可选）
│   ├── __init__.py
│   └── test_translator.py
│
└── docs/                  # 文档目录（可选）
    ├── API.md             # API文档
    └── DEVELOPMENT.md     # 开发指南
```

## 📄 核心文件说明

### 1. **main.py**

- **职责**：应用程序入口
- **功能**：
  - 初始化Qt应用
  - 加载配置文件
  - 创建系统托盘
  - 注册全局快捷键
  - 启动事件循环

### 2. **src/tray.py**

- **职责**：系统托盘管理
- **功能**：
  - 创建托盘图标
  - 托盘菜单（设置、退出等）
  - 托盘消息通知
  - 处理托盘交互事件

### 3. **src/hotkey.py**

- **职责**：全局快捷键监听
- **功能**：
  - 注册全局快捷键
  - 监听快捷键触发
  - 快捷键冲突检测
  - 动态修改快捷键

### 4. **src/translator.py**

- **职责**：翻译和润色API调用
- **功能**：
  - 支持多个API提供商（DeepL、OpenAI等）
  - 异步API请求
  - 错误处理和重试机制
  - 结果缓存

### 5. **src/popup.py**

- **职责**：弹出窗口UI
- **功能**：
  - 无边框半透明窗口
  - 在鼠标附近显示
  - 显示翻译/润色结果
  - 加载动画
  - 复制结果到剪贴板

### 6. **src/settings.py**

- **职责**：设置界面
- **功能**：
  - API Key配置
  - 快捷键自定义
  - 主题/样式设置
  - 配置保存和加载

### 7. **src/clipboard.py**

- **职责**：剪贴板操作
- **功能**：
  - 保存/恢复剪贴板内容
  - 模拟Ctrl+C获取选中文本
  - 监听剪贴板变化

### 8. **src/utils.py**

- **职责**：通用工具函数
- **功能**：
  - 资源路径解析（支持打包后）
  - 日志管理
  - 配置文件读写
  - 版本检查

## 📦 依赖包（requirements.txt）

- **PySide6**: Qt6 Python绑定，GUI框架
- **pynput**: 全局快捷键和鼠标事件监听
- **pyperclip**: 剪贴板操作
- **requests**: HTTP请求（API调用）
- **python-dotenv**: 环境变量管理（可选）

## ⚙️ 配置文件（config.json）

```json
{
  "api": {
    "provider": "openai",
    "api_key": "",
    "base_url": ""
  },
  "hotkey": {
    "translate": "ctrl+q",
    "polish": "ctrl+shift+q"
  },
  "ui": {
    "theme": "light",
    "opacity": 0.95,
    "font_size": 12
  },
  "general": {
    "auto_start": false,
    "cache_enabled": true,
    "language": "zh-CN"
  }
}
```

## 🚀 开发阶段

### Phase 1: MVP（最小可行产品）

- [x] 项目结构搭建
- [ ] 基础UI框架（托盘+弹窗）
- [ ] 快捷键监听
- [ ] Mock数据测试

### Phase 2: 核心功能

- [ ] API集成
- [ ] 剪贴板监听
- [ ] 实际翻译功能
- [ ] 错误处理

### Phase 3: 完善体验

- [ ] 设置界面
- [ ] 配置持久化
- [ ] 样式美化
- [ ] 多语言支持

### Phase 4: 打包发布

- [ ] PyInstaller打包
- [ ] 测试安装流程
- [ ] 编写用户文档
- [ ] GitHub Release

## 📝 注意事项

1. **venv/** 和 **config.json** 不应提交到Git
2. 所有用户敏感信息应使用环境变量或配置文件
3. 资源文件路径需要支持打包后的临时目录
4. macOS需要申请辅助功能权限
5. Windows可能需要管理员权限运行

## 🔗 相关链接

- PySide6文档: <https://doc.qt.io/qtforpython/>
- pynput文档: <https://pynput.readthedocs.io/>
- PyInstaller文档: <https://pyinstaller.org/>
