import unittest
import time
from config.HTMLTestRunner import HTMLTestRunner

case_path=r"D:\PythonProject\jmeter_python\test_case"
# report_path=r"D:\PythonProject\jmeter_python\report\\"
discover=unittest.defaultTestLoader.discover(case_path,pattern="movie_test_*.py")

if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d-%H-%M-%S')
    # report_name=report_path+f'{now1}.html'
    # print(report_name)
    with open(rf'../report/{now}.html','wb') as f:
        runner=HTMLTestRunner(
            stream=f,
            title="测试报告",
            description="测试报告如下",
            tester="王安基",
            # 结果的详细程度
            verbosity=2
        )
        runner.run(discover)


















