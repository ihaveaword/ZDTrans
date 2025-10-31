# 文档结构说明

ZDTrans 的文档已经重新整理，所有详细文档都在 `docs/` 目录下。

## 📁 文档组织

```
ZDTrans/
├── README.md                    # 项目主页（快速了解项目）
├── docs/                        # 📚 文档中心
│   ├── README.md               # 文档索引和导航
│   ├── CHANGELOG.md            # 版本更新历史
│   ├── UPDATE_SUMMARY.md       # 最新更新总结
│   │
│   ├── 用户指南/
│   │   ├── QUICK_START.md              # 快速开始
│   │   ├── MAIN_WINDOW_GUIDE.md        # 主窗口使用
│   │   ├── NIGHT_MODE_GUIDE.md         # 夜色模式
│   │   ├── CUSTOM_DOMAIN_GUIDE.md      # 自定义领域
│   │   ├── KEYWORDS_GUIDE.md           # 关键词配置
│   │   └── THEME_COMPARISON.md         # 主题对比
│   │
│   ├── 技术文档/
│   │   ├── PROJECT_STRUCTURE.md        # 项目结构
│   │   ├── VOLCENGINE.md              # API配置
│   │   ├── MODEL_REFERENCE.md         # 模型参考
│   │   ├── PACKAGING_AND_ROADMAP.md   # 打包指南
│   │   └── RELEASE_WORKFLOW.md        # 发布流程
│   │
│   └── 故障排除/
│       └── MACOS_TRAY_TROUBLESHOOTING.md  # macOS托盘问题
│
└── test_theme.py                # 主题演示脚本
```

## 🗂️ 文档分类

### 按用户类型

**新手用户** → 从这里开始
- [快速开始](docs/QUICK_START.md)
- [主窗口指南](docs/MAIN_WINDOW_GUIDE.md)

**普通用户** → 功能使用
- [夜色模式](docs/NIGHT_MODE_GUIDE.md)
- [自定义领域](docs/CUSTOM_DOMAIN_GUIDE.md)
- [关键词配置](docs/KEYWORDS_GUIDE.md)

**高级用户** → 深度配置
- [API配置](docs/VOLCENGINE.md)
- [模型选择](docs/MODEL_REFERENCE.md)

**开发者** → 技术文档
- [项目结构](docs/PROJECT_STRUCTURE.md)
- [打包发布](docs/PACKAGING_AND_ROADMAP.md)
- [发布流程](docs/RELEASE_WORKFLOW.md)

### 按主题分类

**界面相关**
- 夜色模式 (NIGHT_MODE_GUIDE.md)
- 主题对比 (THEME_COMPARISON.md)
- 主窗口使用 (MAIN_WINDOW_GUIDE.md)

**翻译相关**
- 自定义领域 (CUSTOM_DOMAIN_GUIDE.md)
- 关键词配置 (KEYWORDS_GUIDE.md)
- 模型参考 (MODEL_REFERENCE.md)

**配置相关**
- 快速开始 (QUICK_START.md)
- API配置 (VOLCENGINE.md)

## 🎯 快速查找

| 我想要... | 查看文档 |
|---------|---------|
| 快速上手 | [QUICK_START.md](docs/QUICK_START.md) |
| 切换夜色模式 | [NIGHT_MODE_GUIDE.md](docs/NIGHT_MODE_GUIDE.md) |
| 添加自定义领域 | [CUSTOM_DOMAIN_GUIDE.md](docs/CUSTOM_DOMAIN_GUIDE.md) |
| 配置关键词 | [KEYWORDS_GUIDE.md](docs/KEYWORDS_GUIDE.md) |
| 了解更新内容 | [CHANGELOG.md](docs/CHANGELOG.md) |
| 解决托盘问题 | [MACOS_TRAY_TROUBLESHOOTING.md](docs/MACOS_TRAY_TROUBLESHOOTING.md) |
| 参与开发 | [PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) |

## 📋 文档清单

### 用户文档（7个）
- ✅ QUICK_START.md - 快速开始指南
- ✅ MAIN_WINDOW_GUIDE.md - 主窗口使用指南
- ✅ NIGHT_MODE_GUIDE.md - 夜色模式使用指南
- ✅ CUSTOM_DOMAIN_GUIDE.md - 自定义学科领域指南
- ✅ KEYWORDS_GUIDE.md - 关键词使用指南
- ✅ THEME_COMPARISON.md - 主题对比说明
- ✅ MACOS_TRAY_TROUBLESHOOTING.md - macOS故障排除

### 技术文档（5个）
- ✅ PROJECT_STRUCTURE.md - 项目结构说明
- ✅ VOLCENGINE.md - 火山方舟API配置
- ✅ MODEL_REFERENCE.md - 模型参考手册
- ✅ PACKAGING_AND_ROADMAP.md - 打包和路线图
- ✅ RELEASE_WORKFLOW.md - 发布工作流程

### 更新文档（3个）
- ✅ CHANGELOG.md - 完整更新日志
- ✅ UPDATE_SUMMARY.md - 最新更新总结
- ✅ README.md - 文档中心索引

**总计**: 15个文档文件

## ✨ 文档特点

### 结构清晰
- 按功能和用户类型分类
- 层次分明，易于查找
- 统一的命名规范

### 内容完整
- 从入门到精通
- 图文并茂（计划中）
- 示例丰富

### 维护方便
- 集中在 docs 目录
- 避免重复
- 统一更新

## 🔄 文档整理说明

### 已删除的重复文件
之前根目录有多个重复的总结文档，已整理合并：

❌ 已删除：
- `CHANGELOG_THEME.md` → 合并到 `docs/CHANGELOG.md`
- `THEME_FEATURE_SUMMARY.md` → 合并到 `docs/CHANGELOG.md`
- `CUSTOM_DOMAIN_UPDATE.md` → 合并到 `docs/CHANGELOG.md`
- `FEATURE_SUMMARY_FINAL.md` → 合并到 `docs/UPDATE_SUMMARY.md`

✅ 保留：
- `README.md` - 项目主页（必须在根目录）
- `docs/` - 所有详细文档

### 整理原则

1. **单一职责**：每个文档只讲一个主题
2. **避免重复**：相似内容合并到一个文档
3. **层次清晰**：根目录简洁，详细文档在 docs
4. **便于导航**：文档中心提供完整索引

## 📝 如何贡献文档

### 添加新文档
1. 在 `docs/` 目录创建 `.md` 文件
2. 在 `docs/README.md` 中添加链接
3. 在项目 `README.md` 中适当引用

### 更新现有文档
1. 直接编辑 `docs/` 中的文件
2. 更新 `docs/CHANGELOG.md`
3. 如有重大变化，更新 `docs/UPDATE_SUMMARY.md`

### 文档规范
- 使用 Markdown 格式
- 添加清晰的标题和目录
- 包含代码示例
- 注明更新日期

---

**整理日期**: 2025-10-31  
**文档版本**: v1.2.0  
**维护者**: ZDTrans Team
