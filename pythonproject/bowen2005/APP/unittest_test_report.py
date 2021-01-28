import unittest
import time
from peizhi.HTMLTestRunner import HTMLTestRunner

# 执行的用例的路径
case_path=r"D:\PythonProject\bowen2005\APP"
# 生成的报告的路径
report_path=r"D:\PythonProject\bowen2005\report\\"
# 找到case_path目录下以unittest开头的所有文件
discover=unittest.defaultTestLoader.discover(case_path,pattern="unittest*.py")

if __name__ == "__main__":
    # 获取当前时间
    now=time.strftime("%Y%m%d%H%M%S")
    # 在report_path目录下产生一个.html文件
    report_name=report_path+f"{now}.html"
    # 打开文件并以二进制形式写入
    with open(report_name,"wb") as f:
        # HTMLTestRunner类的实例化
        runner=HTMLTestRunner(
            stream=f,
            title="测试报告",
            description="测试报告详情如下",
            tester="王安基",
            verbosity=2
        )
        runner.run(discover)






