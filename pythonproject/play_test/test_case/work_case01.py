import unittest
from common.work_play import duqu_csv
import logging.config
from parameterized import parameterized


logging.config.fileConfig('')  # 匹配日志文件
logging = logging.getLogger()   # 日志采集器

sj = duqu_csv()

class movie_test(unittest.TestCase):
    # Movie = movie()
    sj = duqu_csv()





