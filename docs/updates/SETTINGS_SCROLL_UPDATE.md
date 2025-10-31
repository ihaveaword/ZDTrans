# 设置窗口滚动优化说明

## 更新内容

### 问题
设置窗口内容较多，在某些屏幕分辨率下会超出屏幕高度，导致底部内容无法访问。

### 解决方案
为设置窗口添加滚动区域，确保所有内容都可访问。

## 技术实现

### 1. 添加滚动区域

**修改文件**: `src/settings.py`

**关键改动**:
```python
# 导入 QScrollArea 和 QWidget
from PySide6.QtWidgets import (..., QScrollArea, QWidget)

# 设置窗口尺寸
self.setMinimumWidth(500)
self.setMinimumHeight(600)   # 最小高度
self.setMaximumHeight(800)   # 最大高度

# 创建滚动区域
scroll = QScrollArea()
scroll.setWidgetResizable(True)
scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

# 创建内容容器
content_widget = QWidget()
layout = QVBoxLayout(content_widget)

# ... 添加所有设置组件到 layout ...

# 将内容设置到滚动区域
scroll.setWidget(content_widget)

# 按钮固定在底部（不滚动）
main_layout.addWidget(scroll)        # 滚动区域
main_layout.addLayout(button_layout)  # 固定按钮
```

### 2. 美化滚动条样式

**修改文件**: `src/theme.py`

**添加滚动条样式**:

#### 夜间模式滚动条
```python
QScrollArea {
    border: none;
    background-color: #1e1e1e;
}
QScrollBar:vertical {
    background-color: #2d2d2d;
    width: 12px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background-color: #5c5c5c;
    border-radius: 6px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background-color: #6c6c6c;
}
```

#### 日间模式滚动条
```python
QScrollBar:vertical {
    background-color: #f0f0f0;
    width: 12px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background-color: #c0c0c0;
    border-radius: 6px;
    min-height: 20px;
}
QScrollBar::handle:vertical:hover {
    background-color: #a0a0a0;
}
```

## 功能特点

### 1. 自适应高度
- **最小高度**: 600px（适合较小屏幕）
- **最大高度**: 800px（防止窗口过大）
- **内容超出**: 自动显示滚动条

### 2. 用户体验优化
- ✅ 隐藏水平滚动条（内容宽度自适应）
- ✅ 按需显示垂直滚动条（内容超出时才显示）
- ✅ 滚动条圆角设计，美观现代
- ✅ 悬停效果，交互反馈清晰

### 3. 固定底部按钮
- 保存和取消按钮固定在窗口底部
- 不会随内容滚动
- 始终可见可访问

### 4. 主题适配
- 日间模式：浅色滚动条
- 夜间模式：深色滚动条
- 自动跟随主题切换

## 适配场景

### 场景 1：笔记本电脑（1366x768）
- 窗口高度 600px
- 内容滚动显示
- 所有设置可访问

### 场景 2：标准显示器（1920x1080）
- 窗口高度可达 800px
- 大部分内容可见
- 少量滚动即可

### 场景 3：小屏幕设备
- 窗口自动适应最小高度 600px
- 滚动条确保所有内容可访问
- 不会超出屏幕

## 视觉效果

### 滚动前
```
┌────────────────────────────┐
│ ZDTrans - 设置             │
├────────────────────────────┤
│ ┌─ API 配置 ─────────────┐ │
│ │ API 提供商: [▼]        │ │
│ │ API Key:    [____]     │ │
│ └────────────────────────┘ │
│                            │
│ ┌─ 翻译配置 ─────────────┐ │
│ │ 学科领域: [▼] [+]     │ │
│ │ 关键词:   [____]       │ │
│ └────────────────────────┘ │ ▲
│                            │ ║ 滚动条
│ ┌─ 快捷键配置 ───────────┐ │ ║
│ │ ...                    │ │ ▼
└────────────────────────────┘
│ [保存]  [取消]             │ ← 固定
└────────────────────────────┘
```

### 滚动中
```
┌────────────────────────────┐
│ ZDTrans - 设置             │
├────────────────────────────┤
│ ┌─ 翻译配置 ─────────────┐ │
│ │ 学科领域: [▼] [+]     │ │
│ │ 关键词:   [____]       │ │ ▲
│ │ □ 学术模式             │ │ ║
│ │ ☑ 保留术语原文         │ │ ║ 滚动条
│ └────────────────────────┘ │ ║
│                            │ ║
│ ┌─ 快捷键配置 ───────────┐ │ ║
│ │ 翻译: Ctrl+Q          │ │ ▼
└────────────────────────────┘
│ [保存]  [取消]             │ ← 固定
└────────────────────────────┘
```

## 测试方法

### 方法 1：运行测试脚本
```bash
python test_settings_scroll.py
```

### 方法 2：主程序测试
```bash
python main.py
# 然后打开设置窗口
```

### 测试点
1. ✅ 窗口高度不超过 800px
2. ✅ 内容超出时显示滚动条
3. ✅ 滚动条样式美观
4. ✅ 保存/取消按钮固定在底部
5. ✅ 主题切换时滚动条同步变化

## 代码统计

- 修改文件: 2 个
- 新增代码: 约 50 行
- 滚动条样式: 约 30 行

## 相关文档

- [夜色模式使用指南](NIGHT_MODE_GUIDE.md)
- [主题对比说明](THEME_COMPARISON.md)

---

**更新日期**: 2025-10-31  
**版本**: v1.2.1  
**类型**: UI优化
