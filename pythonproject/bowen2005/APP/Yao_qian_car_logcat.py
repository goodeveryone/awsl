# 从appium中导入webdriver方法
from appium import webdriver
# 从logging模块中导入config方法
import logging.config
# 匹配日志文件
logging.config.fileConfig("../peizhi/peizhi.conf")
# 采集器
logging=logging.getLogger()
# 导入时间模块
import time


desired_caps={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceNAme":"127.0.0.1:62001",
    "appPackage":"com.monika.yaoqianche",
    "appActivity":"com.monika.yaoqianche.MainActivity",
    "noReset":False
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
logging.info("")
logging.info("App started successfully")

driver.implicitly_wait(20)

class Test():
    def agreement(self):
        """点击同意"""
        driver.find_element_by_id("com.monika.yaoqianche:id/tv_agreement_dialog_sure").click()
        logging.info("Click agreement")

        """点击'我的'"""
        driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="我的"]/android.widget.ImageView').click()
        logging.info("Click mine")

        """点击'去登陆'"""
        driver.find_element_by_id("com.monika.yaoqianche:id/tv_confirm").click()
        logging.info("Click go login")

        """点击输入手机号"""
        driver.find_element_by_id("com.monika.yaoqianche:id/met_login_phone").send_keys("15188385283")
        logging.info("Send phone number")

        """点击输入密码"""
        driver.find_element_by_id("com.monika.yaoqianche:id/met_login_password").send_keys("980604")
        logging.info("Send password")

        """点击'登录'"""
        driver.find_element_by_id("com.monika.yaoqianche:id/stv_login_sure").click()
        logging.info("Click login")

        time.sleep(1)

        """点击广告"""
        driver.find_element_by_id("com.monika.yaoqianche:id/navigation_advs").click()
        logging.info("Click advertisement")

        time.sleep(1)

        """点击导航键‘主页’"""
        driver.find_element_by_id("com.monika.yaoqianche:id/navigation_home").click()
        logging.info("Click homepage")

        """点击‘平台介绍’"""
        a=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()
        logging.info("Click introdution to the platform")

        time.sleep(1)

        for i in range(3):
            time.sleep(1)
            """从下往上滑动屏幕"""
            driver.swipe(375,1080,375,580,1000)
            logging.info(f"Slide {i+1}")
        logging.info("The progrom runs successfuly")
text=Test()
text.agreement()








