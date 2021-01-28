# 生成测试报告
import unittest
from config.HTMLTestRunner import HTMLTestRunner
import time
# from common.dingding import message

case_path=r"D:\PythonProject\new_project\Test_case"
report_path=r"D:\PythonProject\new_project\report\\"
discover=unittest.defaultTestLoader.discover(case_path,pattern="test_case_QQ.py")

if __name__ == "__main__":
    """获取当前时间"""
    now=time.strftime("%Y%m%d%H%M%S")
    report_name=report_path+f'{now}.html'
    with open(report_name,"wb") as f:
        runner=HTMLTestRunner(
            stream=f,
            title="测试报告",
            description="测试报告如下",
            tester="王安基",
            # 结果的详细程度
            verbosity=2
        )
        runner.run(discover)
        # 生成钉钉机器人报告
        # message()




# import time
# import unittest
# from config.HTMLTestRunner import HTMLTestRunner
#
#
#
# case_path=r"D:\PythonProject\new_project\Test_Case"
# report_path=r"D:\PythonProject\new_project\report"
# discover=unittest.defaultTestLoader.discover(case_path,pattern="test_case_log*.py")
#
# if __name__ == "__main__":
#     now=time.strftime("%Y%m%d%H%M%S")
#     report_name=report_path+f"{now}.html"
#     with open(report_name,"wb") as f:
#         runner=HTMLTestRunner(
#             tester="王安基",
#             title="测试报告",
#             stream=f,
#             description="测试报告如下",
#             verbosity=2
#         )
#         runner.run(discover)






























































