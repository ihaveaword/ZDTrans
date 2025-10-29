"""
翻译和润色API调用模块
支持多个API提供商
"""

import requests
from PySide6.QtCore import QObject, Signal, QThread
import json
import time


class TranslatorWorker(QThread):
    """翻译工作线程"""
    
    # 信号定义
    result_ready = Signal(str, str)  # (result_text, action_type)
    error_occurred = Signal(str)
    
    def __init__(self, text, action_type, api_config, keywords=None):
        super().__init__()
        self.text = text
        self.action_type = action_type  # 'translate' or 'polish'
        self.api_config = api_config
        self.keywords = keywords or []  # 关键词列表
        
    def run(self):
        """执行翻译/润色"""
        try:
            result = self._call_api()
            self.result_ready.emit(result, self.action_type)
        except Exception as e:
            self.error_occurred.emit(str(e))
            
    def _call_api(self):
        """调用API"""
        provider = self.api_config.get('provider', 'openai')
        
        if provider == 'openai':
            return self._call_openai()
        elif provider == 'volcengine' or provider == 'doubao':
            return self._call_volcengine()
        elif provider == 'deepl':
            return self._call_deepl()
        else:
            raise ValueError(f"Unsupported API provider: {provider}")
            
    def _call_openai(self):
        """调用OpenAI API"""
        api_key = self.api_config.get('api_key', '')
        base_url = self.api_config.get('base_url', 'https://api.openai.com/v1')
        
        if not api_key:
            raise ValueError("API Key is not configured")
            
        # 构建提示词
        keyword_context = ""
        if self.keywords:
            keyword_context = f"\n\n关键词提示：{', '.join(self.keywords)}"
            
        if self.action_type == 'translate':
            prompt = f"请将以下文本翻译成中文（如果是中文则翻译成英文）{keyword_context}：\n\n{self.text}"
        else:  # polish
            prompt = f"请润色以下文本，使其更加流畅和专业{keyword_context}：\n\n{self.text}"
            
        # 调用API
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.3
        }
        
        response = requests.post(
            f'{base_url}/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
            
    def _call_volcengine(self):
        """调用火山方舟（豆包）API"""
        api_key = self.api_config.get('api_key', '')
        base_url = self.api_config.get('base_url', 'https://ark.cn-beijing.volces.com/api/v3')
        model = self.api_config.get('model', 'doubao-pro-32k')
        
        if not api_key:
            raise ValueError("API Key 未配置")
            
        # 构建关键词上下文
        keyword_context = ""
        if self.keywords:
            keyword_context = f"\n\n专业领域关键词：{', '.join(self.keywords)}\n请在翻译时注意这些领域的专业术语。"
            
        # 构建提示词
        if self.action_type == 'translate':
            prompt = f"请将以下文本翻译成中文（如果是中文则翻译成英文），只返回翻译结果，不要添加任何解释{keyword_context}：\n\n{self.text}"
        else:  # polish
            prompt = f"请润色以下文本，使其更加流畅和专业，只返回润色后的文本，不要添加任何解释{keyword_context}：\n\n{self.text}"
            
        # 调用API
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.3
        }
        
        response = requests.post(
            f'{base_url}/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            raise Exception(f"API 错误: {response.status_code} - {response.text}")
    
    def _call_deepl(self):
        """调用DeepL API"""
        # TODO: 实现DeepL API调用
        raise NotImplementedError("DeepL API not implemented yet")


class TranslatorManager(QObject):
    """翻译管理器"""
    
    # 信号定义
    translation_ready = Signal(str, str)
    translation_error = Signal(str)
    
    def __init__(self, api_config):
        super().__init__()
        self.api_config = api_config
        self.worker = None
        self.cache = {}  # 简单的缓存
        self.keywords = []  # 当前关键词列表
        
    def set_keywords(self, keywords):
        """设置关键词列表"""
        if isinstance(keywords, str):
            # 如果是字符串，按逗号分割
            self.keywords = [k.strip() for k in keywords.split(',') if k.strip()]
        elif isinstance(keywords, list):
            self.keywords = keywords
        else:
            self.keywords = []
        print(f"关键词已更新: {self.keywords}")
        
    def translate(self, text):
        """翻译文本"""
        self._process(text, 'translate')
        
    def polish(self, text):
        """润色文本"""
        self._process(text, 'polish')
        
    def _process(self, text, action_type):
        """处理文本（翻译或润色）"""
        if not text or not text.strip():
            self.translation_error.emit("No text to process")
            return
            
        # 检查缓存（包含关键词的缓存键）
        cache_key = f"{action_type}:{','.join(self.keywords)}:{text}"
        if cache_key in self.cache:
            self.translation_ready.emit(self.cache[cache_key], action_type)
            return
            
        # 创建工作线程
        self.worker = TranslatorWorker(text, action_type, self.api_config, self.keywords)
        self.worker.result_ready.connect(self._on_result)
        self.worker.error_occurred.connect(self._on_error)
        self.worker.start()
        
    def _on_result(self, result, action_type):
        """处理结果"""
        # 缓存结果（包含关键词）
        cache_key = f"{action_type}:{','.join(self.keywords)}:{self.worker.text}"
        self.cache[cache_key] = result
        
        # 发送信号
        self.translation_ready.emit(result, action_type)
        
    def _on_error(self, error_msg):
        """处理错误"""
        self.translation_error.emit(error_msg)
        
    def update_config(self, api_config):
        """更新API配置"""
        self.api_config = api_config
        self.cache.clear()  # 清空缓存
