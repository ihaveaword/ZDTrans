#!/usr/bin/env python3
"""
测试配置文件加载
"""

import sys
sys.path.insert(0, '/Users/code/ZDTrans')

from src.utils import load_config, get_config_path

print("配置文件路径:", get_config_path())
print("\n加载的配置:")
config = load_config()

import json
print(json.dumps(config, indent=2, ensure_ascii=False))

print("\nAPI 配置:")
print("  Provider:", config['api']['provider'])
print("  API Key:", config['api']['api_key'][:10] + "..." if config['api']['api_key'] else "未设置")
print("  Base URL:", config['api']['base_url'])
print("  Model:", config['api'].get('model', '未设置'))
