import datetime
import time

from selenium import webdriver

name = ‘账号’
password = ‘密码’

# 指定webdriver位置
driver = webdriver.Chrome(executable_path=‘C:\chromedriver.exe’)

# 打开淘宝网址
driver.get(‘https://www.taobao.com/’)

class pay:
    # 登录模块
    def login_in(self, num, pwd, times):
    # 点击登入
        driver.find_element_by_class_name(‘h’).click()
        time.sleep(0.3)
        # 发送账号密码
        driver.find_element_by_id(‘fm-login-id’).send_keys(num)
        driver.find_element_by_id(‘fm-login-password’).send_keys(pwd)
        time.sleep(0.2)
        # 点击登入
        driver.find_element_by_class_name(‘fm-btn’).click()
        time.sleep(1)
        # 进入购物车
        driver.get(“https://cart.taobao.com/cart.htm”)
        # driver.find_element_by_id(‘mc-menu-hd’).click()
        # time.sleep(0.2)
        driver.find_element_by_id(‘J_SelectAll1’).click()
        time.sleep(0.5)
        self.auto_check1(times)


#反复结算
def auto_check(self,times):
    while True:
        try:
            if driver.find_element_by_id('J_SelectAll1'):
                driver.find_element_by_id('J_SelectAll1').click()
                time.sleep(0.5)
                break
        except:
            time.sleep(0.5)
            pass

    while True:
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') >= times:
            while True:
                try:
                    driver.find_element_by_id("J_Go").click()
                    print("成功结算")
                    driver.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
                    time.sleep(5)
                    return 0
                except:
                    print("无法结算，重试")
                    time.sleep(1)
                    driver.get("https://cart.taobao.com/cart.htm")
                    self.auto_check(times)
def auto_check1(self,times):
    while True:
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') >= times:
            while True:
                try:
                    driver.find_element_by_id("J_Go").click()
                    print("成功结算")
                    driver.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
                    time.sleep(5)
                    return 0
                except:
                    print("无法结算，重试")
                    time.sleep(1)
                    driver.get("https://cart.taobao.com/cart.htm")
                    self.auto_check(times)
# 运行
def run_driver(self, num, pwd, times):
    self.login_in(num, pwd, times)
