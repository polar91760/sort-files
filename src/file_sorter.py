"""
文件分类器模块
用于将指定目录下的文件按后缀名分类到目标目录
"""

import os
import shutil
from pathlib import Path
from typing import Optional
import logging

class FileSorter:
    def __init__(self, source_dir: str, target_dir: str):
        """
        初始化文件分类器
        
        Args:
            source_dir: 源目录路径
            target_dir: 目标目录路径
        """
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.logger = logging.getLogger(__name__)
        
        # 确保目标目录存在
        self.target_dir.mkdir(parents=True, exist_ok=True)
        
    def _get_unique_filename(self, file_path: Path, target_dir: Path) -> Path:
        """
        生成唯一的文件名，避免重名
        
        Args:
            file_path: 原始文件路径
            target_dir: 目标目录
            
        Returns:
            新的文件路径
        """
        base_name = file_path.stem
        suffix = file_path.suffix
        counter = 1
        
        new_path = target_dir / f"{base_name}{suffix}"
        while new_path.exists():
            new_path = target_dir / f"{base_name}_{counter}{suffix}"
            counter += 1
            
        return new_path
    
    def _create_category_dir(self, suffix: str) -> Path:
        """
        根据文件后缀创建分类目录
        
        Args:
            suffix: 文件后缀
            
        Returns:
            分类目录路径
        """
        # 移除点号，将大写转换为小写
        category = suffix.lstrip('.').lower()
        if not category:
            category = 'no_extension'
            
        category_dir = self.target_dir / category
        category_dir.mkdir(exist_ok=True)
        return category_dir
    
    def sort_files(self) -> None:
        """
        开始整理文件
        """
        if not self.source_dir.exists():
            raise FileNotFoundError(f"源目录不存在: {self.source_dir}")
            
        self.logger.info(f"开始整理文件，从 {self.source_dir} 到 {self.target_dir}")
        
        # 遍历源目录及其子目录
        for root, _, files in os.walk(self.source_dir):
            for file in files:
                source_path = Path(root) / file
                try:
                    # 获取文件后缀
                    suffix = source_path.suffix
                    
                    # 创建分类目录
                    category_dir = self._create_category_dir(suffix)
                    
                    # 生成目标文件路径
                    target_path = self._get_unique_filename(source_path, category_dir)
                    
                    # 移动文件
                    shutil.move(str(source_path), str(target_path))
                    self.logger.info(f"已移动: {source_path} -> {target_path}")
                    
                except Exception as e:
                    self.logger.error(f"处理文件 {source_path} 时出错: {str(e)}")
                    
        self.logger.info("文件整理完成") 