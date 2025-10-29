#!/usr/bin/env python3
"""
翻译历史记录功能 - 示例实现
这是一个功能增强的模板，可以直接使用
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class TranslationHistory:
    """翻译历史记录管理"""
    
    def __init__(self, history_file='data/history.json', max_records=100):
        self.history_file = history_file
        self.max_records = max_records
        self.records = []
        self._load_history()
        
    def _load_history(self):
        """加载历史记录"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.records = json.load(f)
            except Exception as e:
                print(f"加载历史记录失败: {e}")
                self.records = []
        else:
            # 确保目录存在
            os.makedirs(os.path.dirname(self.history_file) if os.path.dirname(self.history_file) else '.', exist_ok=True)
            
    def _save_history(self):
        """保存历史记录"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.records, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存历史记录失败: {e}")
            
    def add_record(self, original: str, translated: str, action_type: str, keywords: List[str] = None):
        """添加一条记录"""
        record = {
            'timestamp': datetime.now().isoformat(),
            'original': original,
            'translated': translated,
            'action_type': action_type,  # 'translate' or 'polish'
            'keywords': keywords or []
        }
        
        # 添加到列表开头（最新的在前）
        self.records.insert(0, record)
        
        # 限制记录数量
        if len(self.records) > self.max_records:
            self.records = self.records[:self.max_records]
            
        self._save_history()
        
    def search(self, keyword: str) -> List[Dict]:
        """搜索历史记录"""
        keyword_lower = keyword.lower()
        results = []
        
        for record in self.records:
            if (keyword_lower in record['original'].lower() or 
                keyword_lower in record['translated'].lower()):
                results.append(record)
                
        return results
        
    def get_recent(self, count: int = 10) -> List[Dict]:
        """获取最近的记录"""
        return self.records[:count]
        
    def clear(self):
        """清空历史记录"""
        self.records = []
        self._save_history()
        
    def export_to_csv(self, output_file: str):
        """导出为 CSV 文件"""
        import csv
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['timestamp', 'original', 'translated', 'action_type', 'keywords'])
            writer.writeheader()
            for record in self.records:
                # 将 keywords 列表转为字符串
                record_copy = record.copy()
                record_copy['keywords'] = ', '.join(record['keywords'])
                writer.writerow(record_copy)


# 使用示例
if __name__ == "__main__":
    # 创建历史记录管理器
    history = TranslationHistory()
    
    # 添加记录
    history.add_record(
        original="Hello World",
        translated="你好世界",
        action_type="translate",
        keywords=["计算机", "编程"]
    )
    
    # 搜索
    results = history.search("world")
    print(f"搜索结果: {len(results)} 条")
    
    # 获取最近记录
    recent = history.get_recent(5)
    for i, record in enumerate(recent, 1):
        print(f"{i}. {record['original'][:30]}... → {record['translated'][:30]}...")
        
    # 导出
    history.export_to_csv("translation_history.csv")
    print("已导出到 translation_history.csv")
