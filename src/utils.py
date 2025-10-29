"""
工具函数模块
"""

import sys
import os
import json
import logging
from pathlib import Path


def get_resource_path(relative_path):
    """
    获取资源文件的绝对路径
    支持开发环境和PyInstaller打包后的环境
    
    Args:
        relative_path: 相对路径
        
    Returns:
        str: 绝对路径
    """
    try:
        # PyInstaller创建临时文件夹,将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except AttributeError:
        # 开发环境
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)


def get_config_path():
    """
    获取配置文件路径
    优先使用项目目录下的 config.json，如果不存在则使用用户目录
    
    Returns:
        Path: 配置文件路径
    """
    # 首先检查项目目录下是否有 config.json
    project_config = Path('config.json')
    if project_config.exists():
        return project_config
    
    # 如果项目目录没有，使用用户目录
    home = Path.home()
    config_dir = home / '.zdtrans'
    
    # 确保目录存在
    config_dir.mkdir(exist_ok=True)
    
    return config_dir / 'config.json'


def load_config():
    """
    加载配置文件
    
    Returns:
        dict: 配置字典
    """
    config_path = get_config_path()
    
    # 默认配置
    default_config = {
        'api': {
            'provider': 'openai',
            'api_key': '',
            'base_url': 'https://api.openai.com/v1',
            'model': 'gpt-3.5-turbo'
        },
        'translation': {
            'domain': 'general',
            'custom_context': '',
            'preserve_terms': True,
            'academic_mode': False
        },
        'hotkey': {
            'translate': 'ctrl+q',
            'polish': 'ctrl+shift+q'
        },
        'ui': {
            'theme': 'dark',
            'opacity': 0.95,
            'font_size': 12
        },
        'general': {
            'auto_start': False,
            'cache_enabled': True,
            'language': 'zh-CN'
        }
    }
    
    # 如果配置文件不存在，创建默认配置
    if not config_path.exists():
        save_config(default_config)
        return default_config
        
    # 读取配置文件
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            
        # 合并默认配置（处理新增的配置项）
        merged_config = merge_config(default_config, config)
        return merged_config
        
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        return default_config


def save_config(config):
    """
    保存配置文件
    
    Args:
        config: 配置字典
    """
    config_path = get_config_path()
    
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Error saving config: {e}")


def merge_config(default, current):
    """
    合并配置，保留current中的值，但添加default中新增的键
    
    Args:
        default: 默认配置
        current: 当前配置
        
    Returns:
        dict: 合并后的配置
    """
    merged = default.copy()
    
    for key, value in current.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = merge_config(merged[key], value)
        else:
            merged[key] = value
            
    return merged


def setup_logging():
    """设置日志"""
    log_dir = Path.home() / '.zdtrans' / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / 'zdtrans.log'
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


def check_first_run():
    """
    检查是否首次运行
    
    Returns:
        bool: True if first run
    """
    config_path = get_config_path()
    return not config_path.exists()
