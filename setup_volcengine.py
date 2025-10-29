#!/usr/bin/env python3
"""
快速配置火山方舟 API
"""

import json
import os

def setup_volcengine():
    """配置火山方舟 API"""
    print("=" * 60)
    print("🔧 ZDTrans - 火山方舟配置向导")
    print("=" * 60)
    print()
    
    # 获取 API Key
    print("请输入你的火山方舟 API Key:")
    print("(格式类似: ak-xxxxxx)")
    api_key = input("API Key: ").strip()
    
    if not api_key:
        print("❌ API Key 不能为空！")
        return False
    
    # 选择模型
    print("\n请选择模型:")
    print("1. doubao-lite-32k   (快速响应，成本低)")
    print("2. doubao-pro-32k    (推荐，性价比高)")
    print("3. doubao-pro-128k   (长上下文)")
    print("4. 自定义模型/接入点 (输入完整模型名称，如 doubao-1-5-lite-32k-250115)")
    
    choice = input("\n选择 (1-4, 默认2): ").strip() or "2"
    
    model_map = {
        "1": "doubao-lite-32k",
        "2": "doubao-pro-32k",
        "3": "doubao-pro-128k"
    }
    
    if choice in model_map:
        model = model_map[choice]
    elif choice == "4":
        model = input("请输入完整模型名称或接入点ID (如 doubao-1-5-lite-32k-250115): ").strip()
    else:
        print("无效选择，使用默认模型: doubao-pro-32k")
        model = "doubao-pro-32k"
    
    # Base URL
    print("\n使用默认 Base URL: https://ark.cn-beijing.volces.com/api/v3")
    use_default = input("是否使用默认值? (Y/n): ").strip().lower()
    
    if use_default == 'n':
        base_url = input("请输入 Base URL: ").strip()
    else:
        base_url = "https://ark.cn-beijing.volces.com/api/v3"
    
    # 构建配置
    config = {
        "api": {
            "provider": "volcengine",
            "api_key": api_key,
            "base_url": base_url,
            "model": model
        },
        "hotkey": {
            "translate": "ctrl+q",
            "polish": "ctrl+shift+q"
        },
        "ui": {
            "theme": "dark",
            "opacity": 0.95,
            "font_size": 12
        },
        "general": {
            "auto_start": False,
            "cache_enabled": True,
            "language": "zh-CN"
        }
    }
    
    # 保存配置
    config_path = "config.json"
    
    # 如果配置文件已存在，询问是否覆盖
    if os.path.exists(config_path):
        print(f"\n⚠️  配置文件 {config_path} 已存在")
        overwrite = input("是否覆盖? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("❌ 已取消配置")
            return False
    
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 60)
        print("✅ 配置完成！")
        print("=" * 60)
        print(f"\n配置已保存到: {config_path}")
        print("\n配置信息:")
        print(f"  提供商: 火山方舟(豆包)")
        print(f"  模型: {model}")
        print(f"  API Key: {api_key[:8]}...{api_key[-4:]}")
        print(f"\n现在可以运行程序了: python main.py 或 ./start.sh")
        print()
        
        return True
        
    except Exception as e:
        print(f"\n❌ 保存配置失败: {e}")
        return False

if __name__ == "__main__":
    try:
        setup_volcengine()
    except KeyboardInterrupt:
        print("\n\n❌ 配置已取消")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
