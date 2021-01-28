from appium import webdriver

desired_caps={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceNAme":"127.0.0.1:62001",
    "appPackage":"com.monika.yaoqianche",
    "appActivity":"com.monika.yaoqianche.MainActivity",
    "noReset":False
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.implicitly_wait(20)

def agreement():
    """点击同意"""
    driver.find_element_by_id("com.monika.yaoqianche:id/tv_agreement_dialog_sure").click()

agreement()


def into_mine():
    """点击'我的'"""
    driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="我的"]/android.widget.ImageView').click()

into_mine()


def log_on():
    """点击'去登陆'"""
    driver.find_element_by_id("com.monika.yaoqianche:id/tv_confirm").click()

log_on()


def iphone():
    """点击输入手机号"""
    driver.find_element_by_id("com.monika.yaoqianche:id/met_login_phone").send_keys("15188385283")

iphone()


def password():
    """点击输入密码"""
    driver.find_element_by_id("com.monika.yaoqianche:id/met_login_password").send_keys("980604")

password()


def register():
    """点击'登录'"""
    driver.find_element_by_id("com.monika.yaoqianche:id/stv_login_sure").click()

register()

import time
time.sleep(2)

def advertisement():
    """点击广告"""
    driver.find_element_by_id("com.monika.yaoqianche:id/navigation_advs").click()

advertisement()

time.sleep(2)

def Home():
    """点击导航键‘主页’"""
    driver.find_element_by_id("com.monika.yaoqianche:id/navigation_home").click()

Home()


def Past_advertisement():
    """点击‘平台介绍’"""
    a=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]").click()

Past_advertisement()

time.sleep(2)

def slide():
    """从下往上滑动屏幕"""
    driver.swipe(375,1080,375,580,1000)

for i in range(3):
    time.sleep(1)
    slide()



































