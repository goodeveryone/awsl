from appium import webdriver
import time
#
from selenium.webdriver.support.ui import WebDriverWait
import logging.config
# 匹配日志配置文件
logging.config.fileConfig("../peizhi/peizhi.conf")
# 采集器
logging=logging.getLogger()


desired_cap={
    "platformName":"Android",
    "platformVersion":"10",
    "deviceName":"192.168.2.114",
    "appPackage":"com.tencent.mobileqq",
    "appActivity":"com.tencent.mobileqq.activity.SplashActivity",
    "noReset":False
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
logging.info("")
logging.info("App started successfully")

driver.implicitly_wait(60)

class Test():
    def agreement(self):
        """点击同意"""
        """显示等待10秒"""
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")).click()
        # driver.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn").click()
        logging.info("Click agreement")

        """点击登录"""
        driver.find_element_by_id("com.tencent.mobileqq:id/btn_login").click()
        logging.info("Click login")

        """点击账号输入框输入账号"""
        driver.find_element_by_class_name("android.widget.EditText").send_keys("2089503671")
        logging.info("Send QQ account")

        """点击密码框输入密码"""
        driver.find_element_by_id("com.tencent.mobileqq:id/password").send_keys("wajwaj521.")
        logging.info("Send password")

        """点击登录"""
        driver.find_element_by_id("com.tencent.mobileqq:id/login").click()
        logging.info("Click login")

        """点击拒绝"""
        driver.find_element_by_id("com.tencent.mobileqq:id/dialogLeftBtn").click()
        logging.info("Click resufe")

        time.sleep(3)

        """点击联系人"""
        driver.tap([(400,2220),(420,2240)],100)
        logging.info("Click person to contact")

        time.sleep(3)

        """点击第一位好友"""
        a=driver.tap([(400,1040),(700,1040)],100)
        logging.info("Click First friend")

        time.sleep(3)

        """点击发消息按钮"""
        a=driver.find_elements_by_class_name("android.widget.Button")
        a[3].click()
        logging.info("Click Send_news")

        time.sleep(3)

        """点击输入框输入内容"""

        driver.find_element_by_id("com.tencent.mobileqq:id/input").send_keys("这是一条测试对话！")
        logging.info("Send news")

        """点击发送"""
        driver.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()
        logging.info("Click send")
        logging.info("The progrom runs successfuly")
test=Test()
test.agreement()


































