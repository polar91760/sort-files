"""
命令行接口模块
"""

import argparse
import logging
from pathlib import Path
from .file_sorter import FileSorter

def setup_logging():
    """配置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='按文件后缀整理文件')
    parser.add_argument('source_dir', help='源目录路径')
    parser.add_argument('target_dir', help='目标目录路径')
    
    args = parser.parse_args()
    
    # 设置日志
    setup_logging()
    
    # 创建文件分类器实例
    sorter = FileSorter(args.source_dir, args.target_dir)
    
    try:
        # 开始整理文件
        sorter.sort_files()
    except Exception as e:
        logging.error(f"发生错误: {str(e)}")
        return 1
        
    return 0

if __name__ == '__main__':
    exit(main()) 