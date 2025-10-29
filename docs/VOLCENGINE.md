# 火山方舟（豆包）API 配置指南

本项目支持使用字节跳动的火山方舟大模型服务（豆包）。

## 📝 获取 API Key

### 1. 注册账号

访问 [火山方舟控制台](https://console.volcengine.com/ark)

### 2. 创建 API Key

1. 登录后进入 **API 访问**
2. 点击 **创建 API Key**
3. 复制生成的 API Key（格式类似：`ak-xxxxxx`）

### 3. 获取接入点 ID（可选）

如果你使用的是推理接入点：
1. 进入 **在线服务**
2. 选择你的模型
3. 复制 **接入点 ID**（例如：`ep-20240101-xxxxx`）

## ⚙️ 配置方法

### 方式 1：使用配置文件（推荐）

编辑 `config.json` 文件：

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

> 💡 **提示**: `model` 字段可以填写：
> - 通用模型名称（如 `doubao-pro-32k`）
> - 带版本号的完整名称（如 `doubao-1-5-lite-32k-250115`）
> - 推理接入点 ID（如 `ep-20240101-xxxxx`）

### 方式 2：使用 GUI 设置界面

1. 运行程序后，右键点击托盘图标
2. 选择 **设置**
3. 填写配置：
   - **API 提供商**: 选择 "火山方舟(豆包)"
   - **API Key**: 填入你的 API Key
   - **Base URL**: `https://ark.cn-beijing.volces.com/api/v3`
   - **Model**: `doubao-pro-32k`（或其他可用模型）

## 🎯 可用模型

火山方舟提供多个模型系列，按需选择：

| 模型系列 | Model ID 格式 | 特点 |
|---------|--------------|------|
| 豆包 Lite | `doubao-lite-32k` 或 `doubao-1-5-lite-32k-xxxxxx` | 快速响应，成本低 |
| 豆包 Pro（推荐） | `doubao-pro-32k` 或 `doubao-1-5-pro-32k-xxxxxx` | 32k 上下文，性价比高 |
| 豆包 Pro 128k | `doubao-pro-128k` 或 `doubao-1-5-pro-128k-xxxxxx` | 128k 长上下文 |

> **注意**: 不同版本的模型会有不同的版本号后缀（如 `-250115`），请在火山方舟控制台查看你有权限访问的具体模型名称。

### 使用推理接入点（高级）

如果你创建了推理接入点，可以直接使用接入点 ID 作为 model 值：

```json
{
  "api": {
    "provider": "volcengine",
    "api_key": "your-api-key-here",
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "model": "ep-20240101-xxxxx"
  }
}
```

推理接入点的优势：
- 固定的模型版本
- 更稳定的服务
- 可以自定义参数

## 💰 计费说明

火山方舟按 token 计费，不同模型系列价格不同：

- **豆包 Lite 系列**: 约 0.0003-0.0005元/1k tokens
- **豆包 Pro 系列**: 约 0.0008-0.001元/1k tokens  
- **豆包 Pro 128k 系列**: 约 0.005元/1k tokens

> 具体价格以火山方舟控制台显示为准，不同版本可能有差异。
>
> 新用户通常有免费额度，查看 [定价页面](https://www.volcengine.com/pricing?product=doubao) 了解详情。

## 🔧 故障排查

### 1. API Key 无效

错误信息: `401 Unauthorized`

**解决方案**:
- 确认 API Key 正确复制（包含 `ak-` 前缀）
- 检查 API Key 是否已激活
- 确认账号余额充足

### 2. 模型不存在

错误信息: `model not found`

**解决方案**:
- 检查模型 ID 是否正确
- 确认模型已在控制台启用
- 如果使用接入点，确认接入点 ID 正确

### 3. 接口调用失败

错误信息: `Connection error`

**解决方案**:
- 检查网络连接
- 确认 Base URL 正确
- 尝试更换接入点区域（如 `cn-beijing` 改为 `cn-shanghai`）

## 📚 参考链接

- [火山方舟官网](https://www.volcengine.com/product/doubao)
- [API 文档](https://www.volcengine.com/docs/82379)
- [控制台](https://console.volcengine.com/ark)
- [定价说明](https://www.volcengine.com/pricing?product=doubao)

## 💡 使用建议

1. **首次使用**: 建议使用 `doubao-lite-32k` 进行测试，成本低
2. **日常使用**: `doubao-pro-32k` 性价比最高
3. **长文本**: 如果需要处理长文档，使用 `doubao-pro-128k`
4. **成本控制**: 在配置中启用缓存功能，避免重复请求

## 🆚 与 OpenAI 对比

| 特性 | 火山方舟 | OpenAI |
|-----|---------|--------|
| 价格 | 更便宜 | 较贵 |
| 中文能力 | 优秀 | 良好 |
| 访问速度 | 国内快 | 国外需代理 |
| 稳定性 | 高 | 高 |

对于国内用户，推荐使用火山方舟！
