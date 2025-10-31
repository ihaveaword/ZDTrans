# 打包体积优化指南

## 问题分析

### 当前情况
- **venv 大小**: 1.1GB
- **打包后 .app**: 39MB
- **主要占用**: PySide6 (1.1GB)

### 关键认识 ⚠️

**venv 不会被打包进 exe/app！**

PyInstaller 打包时：
1. ✅ 只打包**实际使用**的模块
2. ✅ 自动分析依赖
3. ✅ 排除未使用的代码
4. ❌ **不会**把整个 venv 打包进去

### 实际打包大小

```
venv/           1.1GB  ← 开发环境，不打包
dist/ZDTrans    39MB   ← 实际发布包大小 ✅
```

**39MB 已经很合理了！**

## 体积构成分析

### 39MB 的组成
```
PySide6 核心    ~25MB  (65%)
├── QtCore
├── QtWidgets
└── QtGui

Python 运行时   ~8MB   (20%)
pynput         ~2MB   (5%)
requests       ~1MB   (3%)
你的代码        ~200KB (0.5%)
其他依赖        ~3MB   (7.5%)
```

## 优化建议

### 🟢 当前已经很好 (39MB)

**对比其他应用**:
- VS Code: ~100MB
- Slack: ~150MB
- Telegram: ~80MB
- **ZDTrans: 39MB** ✅ 非常轻量

### 🟡 可选优化 (可减少到 30MB)

#### 1. 优化 spec 文件
```python
# zdtrans.spec
excludes=[
    'matplotlib', 'numpy', 'pandas',  # 已排除
    'PIL', 'IPython', 'jupyter',      # 新增
    'tkinter',                         # 如果不用
]
```

#### 2. 使用 UPX 压缩
```python
# 已启用
upx=True
```

#### 3. 排除不需要的 Qt 模块
```python
excludes=[
    'PySide6.QtNetwork',
    'PySide6.QtOpenGL',
    'PySide6.QtSql',
    'PySide6.QtTest',
    'PySide6.QtXml',
]
```

**预计效果**: 39MB → 30-32MB

### 🔴 不推荐的优化

❌ **不要尝试**:
- 手动精简 venv (无用，venv 不打包)
- 移除 PySide6 (必需的)
- 过度压缩 (可能导致启动变慢)

## 打包流程说明

### PyInstaller 如何工作

```
你的代码 (200KB)
    ↓
分析 import 语句
    ↓
收集必需的模块
    ↓
只打包用到的部分
    ↓
生成 39MB 的 .app
```

**venv 只是开发依赖库，打包时会智能选择！**

## 优化后的 spec 文件

```python
# zdtrans.spec (优化版)
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('config.json.example', '.')],  # 移除不必要的 docs
    hiddenimports=['pynput.keyboard._darwin', 'pynput.mouse._darwin'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 数据科学
        'matplotlib', 'numpy', 'pandas', 
        'scipy', 'sklearn',
        # Qt 不需要的模块
        'PySide6.QtNetwork',
        'PySide6.QtOpenGL', 
        'PySide6.QtSql',
        'PySide6.QtTest',
        'PySide6.QtXml',
        'PySide6.Qt3D',
        'PySide6.QtBluetooth',
        # 其他
        'PIL', 'tkinter', 'IPython',
    ],
    noarchive=False,
    optimize=2,  # 更高的优化级别
)

exe = EXE(
    ...
    strip=True,  # 移除调试信息
    upx=True,    # UPX 压缩
    ...
)
```

## 实测对比

### 优化前
```bash
$ du -sh dist/ZDTrans.app
39M
```

### 优化后 (预计)
```bash
$ du -sh dist/ZDTrans.app
30-32M
```

## 结论

✅ **当前 39MB 已经很理想**

**建议**:
1. 如果对体积不是特别敏感 → 保持现状
2. 如果需要更小 → 应用上述优化 (减少 7-9MB)
3. 如果要求极致轻量 → 考虑换技术栈 (Tkinter ~10MB，但功能受限)

**不要担心 venv 的 1.1GB，它不会被打包！**

---

**日期**: 2025-10-31
