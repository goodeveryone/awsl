# 测试用例

import unittest
from common.Android_Helper1 import Helper
import time

class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """类的实例化"""
        cls.helper=Helper()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.helper.quit()

    def test_01(self):
        """输入账号"""
        self.helper.locate("id","com.tal.kaoyan:id/login_email_edittext").clear()
        self.helper.locate("id", "com.tal.kaoyan:id/login_email_edittext").send_keys("abcabcddd")
        self.helper.picture()

    def test_02(self):
        """输入密码"""
        self.helper.locate("id","com.tal.kaoyan:id/login_password_edittext").send_keys("waj123456")
        self.helper.picture()

    def test_03(self):
        """点击登录"""
        self.helper.locate("id","com.tal.kaoyan:id/login_login_btn").click()






if __name__ == "__main__":
    unittest.main()




