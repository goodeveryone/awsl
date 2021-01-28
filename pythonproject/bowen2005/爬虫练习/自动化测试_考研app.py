# 从appium中导入webdriver类
from appium import webdriver
# 把设备和app的信息放在字典里
desired_cap={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.tal.kaoyan",
    "appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset":False
}
# 启动app
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
# 隐性等待20秒
driver.implicitly_wait(60)

def skip():
    """点击跳过"""
    driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()
    # driver.find_element_by_class_name("android.widget.TextView").click()
skip()

def agreement():
    """同意条款"""
    driver.find_element_by_id("com.tal.kaoyan:id/tip_commit").click()
    # driver.find_element_by_class_name("android.widget.TextView").click()
agreement()

# def username():
#     """输入账号"""
#     # driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("123456")
#     # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.EditText[1]").send_keys("123456")
#     driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys("123456")
# username()
#
# def password():
#     """输入密码"""
#     driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("123456")
#
# password()

def user_passwd():
    """登录页面输入账号密码"""
    a = driver.find_elements_by_class_name("android.widget.EditText")
    a[0].send_keys("123456")
    a[1].send_keys("111111")

user_passwd()


def A():
    """点击登录"""
    driver.tap([(157,459),(575,459)],100)

A()
import time
time.sleep(0.5)
a=driver.find_element_by_xpath("//*[@text='验证失败次数过多，请15分钟后再试']")
print(a)
print(a.text)





# def post():
#     """点击注册键"""
#     driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()
#
# post()
#
#
# def user_passwd_1():
#     """注册页面输入账号密码邮箱信息"""
#     a = driver.find_elements_by_class_name("android.widget.EditText")
#     print(type(a))
#     a[0].send_keys("abcabcddd")
#     a[1].send_keys("waj123456")
#     a[2].send_keys("an980604@163.com")
# user_passwd_1()
#
# def skip_1():
#     driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn").click()
#
# skip_1()

# def blackness():
#     """相对定位，先点击头像所在页面的空白处,再点击头像"""
#     a = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_parentlayout")
#     # a.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()
#     a.find_element_by_class_name("android.widget.ImageView").click()
#
# blackness()



# id定位
# 跳过键id
# com.tal.kaoyan:id/tv_skip
# 同意条款键id
# com.tal.kaoyan:id/tip_commit
# 账号键id
# com.tal.kaoyan:id/login_email_edittext
# 密码键id
# com.tal.kaoyan:id/login_password_edittext
# 注册键id
# com.tal.kaoyan:id/login_register_text

# com.tal.kaoyan:id/activity_register_parentlayout
# 头像id
# com.tal.kaoyan:id/activity_register_userheader



# class定位
# android.widget.TextView
# android.widget.TextView
# 头像class
# android.widget.ImageView








