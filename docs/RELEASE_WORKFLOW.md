# GitHub Release 发布流程速查表

## 🚀 完整流程（5步）

### 1️⃣ 打包应用
```bash
cd /Users/code/ZDTrans
source .venv/bin/activate
./build.sh
# 生成：dist/ZDTrans.app
```

### 2️⃣ 创建发布包
```bash
cd dist
zip -r ../release/ZDTrans-v1.0.0-macOS.zip ZDTrans.app
cd ..
# 生成：release/ZDTrans-v1.0.0-macOS.zip
# 注意：此文件仅用于上传 Release，不会提交到 Git
```

### 3️⃣ 提交代码
```bash
git add -A
git commit -m "Release v1.0.0"
git push origin main
# 注意：.gitignore 会自动忽略 release/*.zip，不占用仓库空间
```

### 4️⃣ 创建并推送 Tag
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### 5️⃣ 在 GitHub 创建 Release
访问：https://github.com/YOUR_USERNAME/ZDTrans/releases/new

- **Tag**: v1.0.0
- **标题**: ZDTrans v1.0.0 - 首个稳定版本
- **描述**: 复制 `release/RELEASE_NOTES_v1.0.0.md` 内容
- **上传**: `release/ZDTrans-v1.0.0-macOS.zip`
- 点击 **Publish release**

---

## ⚡ 快捷方式（使用 GitHub CLI）

### 安装 GitHub CLI
```bash
brew install gh
gh auth login
```

### 一键发布
```bash
# 打包
./build.sh

# 创建发布包
cd dist && zip -r ../release/ZDTrans-v1.0.0-macOS.zip ZDTrans.app && cd ..

# 提交并发布
git add -A
git commit -m "Release v1.0.0"
git push origin main
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# 创建 GitHub Release
gh release create v1.0.0 \
  release/ZDTrans-v1.0.0-macOS.zip \
  --title "ZDTrans v1.0.0 - 首个稳定版本" \
  --notes-file release/RELEASE_NOTES_v1.0.0.md
```

---

## 📝 版本更新流程

### 发布新版本（例如 v1.1.0）

1. **修改代码并测试**
2. **更新版本号**
   - 修改 `CHANGELOG.md`
   - 修改 `zdtrans.spec` 中的版本号
3. **打包**
   ```bash
   ./build.sh
   cd dist && zip -r ../release/ZDTrans-v1.1.0-macOS.zip ZDTrans.app && cd ..
   ```
4. **创建 Release Notes**
   ```bash
   cp release/RELEASE_NOTES_v1.0.0.md release/RELEASE_NOTES_v1.1.0.md
   # 编辑新文件
   ```
5. **发布**
   ```bash
   git add -A
   git commit -m "Release v1.1.0"
   git push
   git tag -a v1.1.0 -m "Release v1.1.0"
   git push origin v1.1.0
   gh release create v1.1.0 release/ZDTrans-v1.1.0-macOS.zip \
     --title "ZDTrans v1.1.0" \
     --notes-file release/RELEASE_NOTES_v1.1.0.md
   ```

---

## 🎯 关键点

| 步骤 | 命令 | 说明 |
|------|------|------|
| 打包 | `./build.sh` | 生成 .app 文件 |
| 压缩 | `zip -r xxx.zip ZDTrans.app` | 创建发布包 |
| 提交 | `git push` | 推送代码 |
| Tag | `git tag v1.0.0 && git push origin v1.0.0` | 创建版本标记 |
| Release | 网页或 `gh release create` | 发布下载 |

---

## ⚠️ 注意事项

1. **版本号规则**：遵循语义化版本 (v主版本.次版本.补丁)
2. **Tag 必须先推送**：GitHub Release 需要先有 Tag
3. **压缩包大小**：当前约 39MB，GitHub Release 单文件限制 2GB
4. **不要提交打包文件到 Git**：
   - ❌ `release/*.zip` 已在 .gitignore 中
   - ✅ 仅保留在本地，用于上传 Release
   - ✅ 避免 Git 仓库变得巨大
5. **发布前测试**：先本地运行 `./dist/ZDTrans` 确保正常

---

## 🛠️ 工具脚本

### 开发时
```bash
./dev_run.sh      # 清理缓存并启动（开发用）
./start.sh        # 正常启动
```

### 打包时
```bash
./build.sh        # 一键打包
```

### 清理
```bash
rm -rf build dist *.spec
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
```

---

## 📚 相关文件

- `build.sh` - 打包脚本
- `zdtrans.spec` - PyInstaller 配置
- `release/RELEASE_NOTES_*.md` - 发布说明模板
- `docs/PACKAGING_AND_ROADMAP.md` - 详细文档

---

**快速参考**：打包 → 压缩 → 提交 → Tag → Release ✅
