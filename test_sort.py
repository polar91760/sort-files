import logging
from src.file_sorter import FileSorter

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 源目录和目标目录
source_dir = r"C:\Users\Polar.Wu\Desktop\workspace\pyproject\test\core-common"
target_dir = r"C:\Users\Polar.Wu\Desktop\workspace\pyproject\test\data"

# 创建文件分类器实例
sorter = FileSorter(source_dir, target_dir)

# 开始整理文件
sorter.sort_files() 