import logging
# 定义日志的输出格式
fatmo = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
# 定义日志的输出位置，，FileHandler 输出到文件
# StreamHandler   输出到控制台
b = logging.FileHandler(filename='../log/login.txt',encoding='utf-8')
# 将日志的输出格式添加到输出位置
b.setFormatter(fatmo)
def loggg(filename):
    # 定义日志的文件名
    l = logging.getLogger(filename)
    # 将文件中的日志输出
    l.addHandler(b)
    # 定义日志级别
    l.setLevel(logging.INFO)
    return l

