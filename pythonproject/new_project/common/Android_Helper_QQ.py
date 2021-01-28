import yaml
import time
from time import sleep
import logging.config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


with open("../data/Smith_Family.yaml","rb") as f:
    data=yaml.load(f,Loader=yaml.FullLoader)
# print(data)

desired_caps={
    "platformName":data["platformName"],
    "platformVersion":data["platformVersion"],
    "deviceName":data["deviceName"],
    "appPackage":data["appPackage"],
    "appActivity":data["appActivity"],
    "noReset":bool(data["noReset"])
}
# print(desired_caps)

logging.config.fileConfig("../config/peizhi_logcat.conf")
logging=logging.getLogger()

class Helper():
    def __init__(self):
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        try:
            WebDriverWait(self.driver,40)\
                .until(lambda x:x.find_element_by_id("com.tencent.mobileqq:id/dialogRightBtn")).click()
        except:
            logging.info("no agreement ")

    def quit(self):
        """退出app"""
        self.driver.quit()

    def get_now(self):
        """获取当前时间"""
        now=time.strftime("%Y%m%d%H%M%S")
        return now

    def locate(self,method,element):
        """封装定位"""
        ele=None
        if method == "id":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_element_by_id(element))
        elif method == "class":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_element_by_class_name(element))
        elif method == "xpath":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_element_by_xpath(element))
        elif method == "list_id":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_elements_by_id(element))
        elif method == "list_class":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_elements_by_class_name(element))
        elif method == "list_xpath":
            ele=WebDriverWait(self.driver,40).until(lambda x:x.find_elements_by_xpath(element))
        # elif method == "swipe":
        #     ele=WebDriverWait(self.driver,40).until(lambda x:x.swipe(element))
        else:
            logging.info("no locate method")
        if ele is not None:
            return ele



  # a=Helper

















































