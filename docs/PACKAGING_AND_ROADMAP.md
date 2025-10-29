# 打包发布指南

## 📦 第一步：打包成可执行文件

### macOS 打包

#### 方法 1：使用 PyInstaller（推荐）

```bash
# 1. 安装 PyInstaller
pip install pyinstaller

# 2. 打包成单个可执行文件
pyinstaller --name="ZDTrans" \
    --windowed \
    --onefile \
    --icon=resources/icon.icns \
    --add-data="config.json.example:." \
    main.py

# 打包后的文件在 dist/ZDTrans
```

**参数说明**：
- `--windowed`: 无终端窗口（GUI 应用）
- `--onefile`: 打包成单个文件
- `--icon`: 应用图标
- `--add-data`: 包含配置文件

#### 方法 2：使用 py2app（macOS 原生）

```bash
# 1. 安装 py2app
pip install py2app

# 2. 创建 setup.py
python setup.py py2app

# 生成 .app 应用包
```

### Windows 打包

```bash
# 使用 PyInstaller
pyinstaller --name="ZDTrans" \
    --windowed \
    --onefile \
    --icon=resources/icon.ico \
    main.py
```

### Linux 打包

```bash
# PyInstaller
pyinstaller --name="zdtrans" \
    --onefile \
    main.py

# 或创建 .desktop 文件
```

---

## 🎨 第二步：创建应用图标

### macOS (.icns)

```bash
# 1. 准备 1024x1024 的 PNG 图标
# 2. 使用在线工具转换：https://cloudconvert.com/png-to-icns
# 或使用命令行
mkdir icon.iconset
sips -z 16 16     icon.png --out icon.iconset/icon_16x16.png
sips -z 32 32     icon.png --out icon.iconset/icon_16x16@2x.png
sips -z 32 32     icon.png --out icon.iconset/icon_32x32.png
sips -z 64 64     icon.png --out icon.iconset/icon_32x32@2x.png
sips -z 128 128   icon.png --out icon.iconset/icon_128x128.png
sips -z 256 256   icon.png --out icon.iconset/icon_128x128@2x.png
sips -z 256 256   icon.png --out icon.iconset/icon_256x256.png
sips -z 512 512   icon.png --out icon.iconset/icon_256x256@2x.png
sips -z 512 512   icon.png --out icon.iconset/icon_512x512.png
sips -z 1024 1024 icon.png --out icon.iconset/icon_512x512@2x.png
iconutil -c icns icon.iconset
```

### Windows (.ico)

使用在线工具：https://convertio.co/png-ico/

---

## 🚀 第三步：创建 GitHub Release

### 1. 准备发布文件

```bash
# 创建发布目录
mkdir -p release/v1.0.0

# 复制打包文件
cp dist/ZDTrans release/v1.0.0/
cp README.md release/v1.0.0/
cp config.json.example release/v1.0.0/

# 打包压缩
cd release/v1.0.0
zip -r ZDTrans-v1.0.0-macOS.zip *
```

### 2. 创建 Release

```bash
# 创建 Git tag
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0

# 在 GitHub 上创建 Release
# 1. 访问 https://github.com/YOUR_USERNAME/ZDTrans/releases/new
# 2. 选择 tag: v1.0.0
# 3. 填写 Release 标题和说明
# 4. 上传打包的 .zip 文件
# 5. 点击 "Publish release"
```

---

## 📝 第四步：编写 Release Notes

### Release Notes 模板

```markdown
# ZDTrans v1.0.0 - 首个稳定版本

## ✨ 主要功能

- 🚀 全局快捷键翻译和润色
- 💡 即时弹窗显示结果
- 🏷️ 专业领域关键词支持
- 🎨 简洁美观的主窗口界面
- 📦 系统托盘常驻

## 📥 安装方法

### macOS

1. 下载 `ZDTrans-v1.0.0-macOS.zip`
2. 解压并移动到应用程序文件夹
3. 首次运行需要在"系统偏好设置 > 安全性与隐私"中允许

### Windows

1. 下载 `ZDTrans-v1.0.0-Windows.zip`
2. 解压到任意文件夹
3. 运行 `ZDTrans.exe`

## ⚙️ 配置

1. 编辑 `config.json`
2. 填入您的 API Key
3. 重启程序

## 🐛 已知问题

- macOS 上首次运行需要授权辅助功能
- Windows 可能需要关闭防火墙提示

## 📚 文档

- [快速开始](QUICK_START.md)
- [关键词使用指南](docs/KEYWORDS_GUIDE.md)
- [主窗口使用指南](docs/MAIN_WINDOW_GUIDE.md)
```

---

## 🎯 功能增强建议

### 短期（1-2周）

#### 1. 翻译历史记录
```python
# 在 src/ 下新建 history.py
- 保存最近 100 条翻译记录
- 支持搜索历史
- 一键复制历史结果
```

#### 2. 关键词预设库
```python
# 预设常用领域的关键词
KEYWORD_PRESETS = {
    "计算机": "深度学习, 神经网络, 机器学习",
    "医学": "临床试验, 病理学, 药物代谢",
    "物理": "量子力学, 相对论, 电磁场",
}
```

#### 3. 快捷键可视化编辑
```python
# 完善之前移除的快捷键编辑器
- 录制快捷键
- 冲突检测
- 实时预览
```

### 中期（1-2月）

#### 4. 多语言支持
```python
# 支持更多翻译方向
- 中文 ↔ 英文
- 中文 ↔ 日文
- 中文 ↔ 韩文
```

#### 5. OCR 截图翻译
```python
# 截图 → OCR → 翻译
- 使用 Tesseract OCR
- 或调用百度/腾讯 OCR API
```

#### 6. 自定义 Prompt
```python
# 让用户自定义翻译提示词
- 专业模式
- 口语模式
- 文学模式
```

### 长期（3月+）

#### 7. 插件系统
```python
# 支持用户自定义插件
- 自定义翻译引擎
- 自定义后处理逻辑
```

#### 8. 团队协作
```python
# 术语库共享
- 团队共享关键词库
- 翻译记忆库
```

#### 9. 浏览器扩展
```javascript
// Chrome/Firefox 扩展
- 网页划词翻译
- 与桌面应用联动
```

---

## 📊 性能优化

### 1. 缓存优化
```python
# 使用 SQLite 或 Redis
- 缓存翻译结果
- 自动过期机制
```

### 2. 异步优化
```python
# 使用 asyncio
- 并发处理多个翻译请求
- 流式返回结果
```

### 3. 启动速度优化
```python
# 延迟加载
- 只在需要时加载模块
- 预编译 .pyc 文件
```

---

## 🔒 安全增强

### 1. API Key 加密
```python
# 使用 keyring 库
import keyring
keyring.set_password("ZDTrans", "api_key", api_key)
```

### 2. 网络请求验证
```python
# SSL 证书验证
- 防止中间人攻击
```

---

## 📈 数据统计

### 1. 使用统计
```python
# 统计功能
- 每日翻译次数
- 最常用功能
- 错误率统计
```

### 2. 匿名数据收集（可选）
```python
# 改进产品（需用户同意）
- 崩溃报告
- 功能使用频率
```

---

## 🎨 UI/UX 改进

### 1. 主题支持
```python
# 亮色/暗色主题
- 跟随系统
- 自定义颜色
```

### 2. 动画效果
```python
# 使用 Qt 动画
- 弹窗淡入淡出
- 平滑过渡
```

### 3. 自定义字体
```python
# 让用户选择字体
- 字体大小
- 字体样式
```

---

## 🛠️ 开发工具

### 1. 单元测试
```bash
pytest tests/
```

### 2. 代码检查
```bash
flake8 src/
black src/
```

### 3. 持续集成
```yaml
# .github/workflows/ci.yml
- 自动测试
- 自动打包
- 自动发布
```

---

## 📞 社区建设

### 1. 创建讨论区
- GitHub Discussions
- 用户反馈
- 功能建议

### 2. 编写贡献指南
- CONTRIBUTING.md
- 代码规范
- Pull Request 模板

### 3. 制作教程
- 视频教程
- 博客文章
- 示例配置

---

**开始行动！** 🚀

选择 1-2 个短期功能开始实现，逐步完善您的产品！
