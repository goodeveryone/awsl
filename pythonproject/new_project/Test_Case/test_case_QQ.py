import unittest
from common.Android_Helper_QQ import Helper
import logging.config
import time



class change_picture(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.helper=Helper()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.helper.quit()

    def test_01(self):
        """点击登录"""
        self.helper.locate("id","com.tencent.mobileqq:id/btn_login").click()
    logging.info("Click login")

    def test_02(self):
        """输入账号"""
        self.helper.locate("class","android.widget.EditText").send_keys("2089503671")
    logging.info("Send username")

    def test_03(self):
        """输入密码"""
        self.helper.locate("id","com.tencent.mobileqq:id/password").send_keys("wajwaj521.")
    logging.info("Send password")

    def test_04(self):
        """点击登录箭头"""
        self.helper.locate("id","com.tencent.mobileqq:id/login").click()

    def test_05(self):
        """点击拒绝"""
        self.helper.locate("id","com.tencent.mobileqq:id/dialogLeftBtn").click()
    logging.info("Click reject")

    def test_06(self):
        """点击头像"""
        self.helper.locate("id","com.tencent.mobileqq:id/ws").click()
    logging.info("Click Touxiang_1")

    def test_07(self):
        """点击头像"""
        a=self.helper.locate("list_class","android.widget.ImageView")
        a[0].click()
    logging.info("Click Touxiang_2")

    # def test_08(self):
    #     """点击头像"""
    #     self.helper.locate("","").click()

if __name__ == "__main__":
    unittest.main()

















































