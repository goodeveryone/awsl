# 从appium中导入webdriver方法
from appium import webdriver

desired_caps={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"127.0.0.1:62001",
    "appPackage":"com.tal.kaoyan",
    "appActivity":"com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset":False
}
# 启动APP
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# 隐形等待20秒
driver.implicitly_wait(20)

def skip():
    """点击跳过"""
    driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()

skip()

def agreement():
    """点击同意"""
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]").click()

agreement()

# def username():
#     """点击输入用户名密码"""
#     driver.find_element_by_xpath("//android.widget.EditText[@text='请输入用户名']").send_keys("123456")
#
# username()
#
# def password():
#     """点击输入密码"""
#     driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("123456")
#
# password()
#
# def skip_2():
#     """点击登录，提示失败"""
#     driver.tap([(139,459),(540,459)],100)
#
# skip_2()

def post():
    """点击注册键"""
    driver.find_element_by_id("com.tal.kaoyan:id/login_register_text").click()

post()

def blackness():
    """相对定位，先点击头像所在页面的空白处,再点击头像"""
    a = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_parentlayout")
    # a.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader").click()
    a.find_element_by_class_name("android.widget.ImageView").click()

blackness()

def choose_picture():
    """点击选择图片"""
    driver.find_element_by_xpath(	"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout[5]/android.widget.LinearLayout/android.widget.TextView").click()

choose_picture()

def o_k():
    """点击完成"""
    driver.find_element_by_id("com.tal.kaoyan:id/picture_tv_ok").click()

o_k()

def countermark():
    """点击对号"""
    driver.find_element_by_id("com.tal.kaoyan:id/menu_crop").click()

countermark()


import random

def product_name():
    """随机产生账号"""
    username="psprpo1"+"waj"+str(random.randint(1,2000))
    return username
name=product_name()

def product_passwd():
    """随机产生密码"""
    userpasswd="bowen123"+str(random.randint(1,2000))
    return userpasswd
passwd=product_passwd()

def product_email():
    """随机产生邮箱"""
    useremail="paprpo12"+str(random.randint(1,2000))+"@163.com"
    return useremail
email=product_email()

def AAA():
    """输入随机产生的账号密码邮箱"""
    a=driver.find_elements_by_class_name("android.widget.EditText")
    a[0].send_keys(name)
    a[1].send_keys(passwd)
    a[2].send_keys(email)

AAA()

def skip_1():
    """点击立即注册"""
    driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn").click()

skip_1()

# def year():
#     """选择年份"""
#     driver.find_elements_by_id("com.tal.kaoyan:id/activity_perfectinfomation_time").click()
#     driver.find_element_by_xpath("//android.widget.TextView[@text=2020]").click()
# year()


def major():
    """选择专业"""
    driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_marjorsubject_zhuanye").click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.TextView").click()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[5]/android.widget.TextView[1]").click()
    driver.find_element_by_id("com.tal.kaoyan:id/major_search_item_name").click()

major()

def school():
    driver.find_element_by_id("activity_perfectinfomation_school").click()
    driver.tap([(109,1055),(137,1086)],100)
    address_images=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.TextView[1]").click()
    school_images=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.TextView").click()
    driver.tap([(952,1312),(1018,1339)],100)
school()

def kyb_into():
    driver.find_element_by_id("actvity_perfectinfommation_goBtn").click()
kyb_into()




# import yaml
# with open("Smith_Family.yaml","r",encoding="utf8") as f:
#     data=yaml.load(f,Loader=yaml.FullLoader)
# print(data)
# # print(data["childrens"][1]["age"])
#
# for i in range(2):
#     print(data["childrens"][i]["name"])
#     print(data["childrens"][i]["age"])


# with open("Smith_Family.yaml","r",encoding="utf-8") as f:
#     data=yaml.load(f,Loader=yaml.FullLoader)
# print(data)






























































# com.tal.kaoyan:id/activity_perfectinfomation_time  年份
# android.widget.TextView  text=2020
# / hierarchy / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.ListView / \
#   android.widget.TextView[5]

#com.tal.kaoyan:id/activity_perfectinfomation_major  专业
# com.tal.kaoyan: id / activity_marjorsubject_zhuanye  专业硕士
# android.widget.TextView  	text=工学
# android.widget.TextView   text=机械
# com.tal.kaoyan: id / major_search_item_name  机械下的机械

# com.tal.kaoyan: id / activity_perfectinfomation_school  学校
# [(96,1054),(136,1095)]

