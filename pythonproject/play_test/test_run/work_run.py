import unittest
from time import *
from config.HTMLTestRunner import HTMLTestRunner


case_path = r''
discover = unittest.defaultTestLoader.discover(case_path,pattern='')

if __name__ == "__main__":
    now = strftime("%Y-%m-%d-%H-%M-%S")
    with open(rf'','wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title="测试报告",
            description="测试报告入下",
            tester="王安基",
            verbosity=2
        )
        runner.run(discover)
