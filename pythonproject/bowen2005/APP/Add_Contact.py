from appium import webdriver

desired_caps={
    "platformName":"Android",
    "platformVersion":"7.1.2",
    "deviceName":"127.0.0.1:62001"
}

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.implicitly_wait(20)

driver.find_element_by_id("com.vphone.launcher:id/preview_background").click()

driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()

driver.find_element_by_id("com.android.contacts:id/floating_action_button_container").click()

import random

def product_name():
    """随机产生账号"""
    username="同桌"+str(random.randint(1,2000))
    return username
name=product_name()


def telephone():
    """随机产生手机号"""
    Phone="1310"+"5678"+str(random.randint(100,999))
    return Phone
phone=telephone()

def email_A():
    """随机产生邮箱"""
    Email="bowen"+str(random.randint(1,2000))+"@163.com"
    return Email
email=email_A()

8


a = driver.find_elements_by_class_name("android.widget.EditText")
a[0].send_keys(name)
a[1].send_keys(phone)
a[2].send_keys(email)

driver.find_element_by_id("com.android.contacts:id/menu_save").click()




























































