# from PIL import Image
#
# img = Image.open('104.jpg')  # 打开图片
# width, height = img.size  # 图片尺寸
#
# img.thumbnail((width / 1, height / 2))  # 缩略图
# img = img.crop((0, 0, width / 2, width / 4)) # 图片裁剪
# img = img.convert(mode='L')  # 图片转换
# # img = img.rotate(180)  # 图片旋转
# img.save('output.jpg')  # 保存图片

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# 导入模仿键盘操作模块
from selenium.webdriver.common.keys import Keys

# 导入模仿鼠标操作模块
from selenium.webdriver.common.action_chains import ActionChains
#
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
# # dr.find_element_by_xpath('//*[@id="ttbar-myjd"]/div[1]/a').click()
# # Select(dr.find_element_by_css_selector('[id="ttbar-myjd"]')).select_by_visible_text("消息")
# move = WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="s-usersetting-top"]'))
# ActionChains(dr).move_to_element(move).perform()
# dr.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()

# 切换进框架
# dr.switch_to.frame('_hjRemoteVarsFrame')
# sleep(2)
# dr.find_element_by_tag_name('ul').find_element_by_tag_name('li').click()
# dr.find_element_by_xpath('//*[@id="cascader-menu-2289-0"]/div[1]/ul').find_element_by_xpath('//*[@id="cascader-menu-446-0-0"]').find_element_by_xpath('//*[@id="cascader-menu-2340-1-0"]').find_element_by_xpath('//*[@id="cascader-menu-2340-1"]/div[1]/ul/svg').click()
# element_a = dr.find_element_by_xpath('//*[@id="cascader-menu-446-0-0"]')
# element_b = dr.find_element_by_xpath('//*[@id="cascader-menu-2340-1-0"]')
# element_c = dr.find_element_by_xpath('//*[@id="cascader-menu-2340-1"]/div[1]/ul/svg')
# ActionChains(dr).move_to_element(element_a).move_to_element(element_b).move_to_element(element_c).perform()
# .find_element_by_xpath('//*[@id="cascader-menu-9160-2-0"]/span').click()
# Select(dr.find_element_by_css_selector('[class="el-cascader-node in-active-path"]')).select_by_visible_text("电器")

# element = dr.find_element_by_xpath('//*[@id="cascader-menu-2289-0-0"]/span')
# ActionChains(dr).move_to_element(element).perform()
# sleep(2)
# element = dr.find_element_by_xpath('//*[@id="cascader-menu-7255-1-0"]/span')
# ActionChains(dr).move_to_element(element).perform()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="cascader-menu-4990-2-0"]/span').click()

# 定位到要悬停的元素
# move = WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="cascader-menu-7309-0-0"]/span'))
# # 对定位到的元素执行悬停操作
# ActionChains(dr).move_to_element(move).perform()
# import csv
# data=[]
# with open(r'C:\Users\admin\Desktop\Yiqimai.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(type(reader))
#     for i in reader:
#         data.append(i)
#     print(data)
#     print(data[1][2])
#
#
# for i in range(1,5):
#     # 商品名称
#     goods_name = data[i][0]
#     # 商品价格
#     goods_price = data[i][1]
#     # 商品主图路径
#     main_picture = data[i][2]
#     # 商品轮播图路径
#     roulette_picture = data[i][3]
#     # 商品详情图路径
#     detail_picture = data[i][4]
#     # 划线价格
#     wrong_price = data[i][5]
#     # 商品库存
#     goods_stock = data[i][6]
#     # 销售件数
#     quantity_sold = data[i][7]
#     # 拼团名称
#     group_name = data[i][8]
#     # 拼团商品
#     group_goods_name = data[i][9]
#     # 参团人数
#     number_of_people = data[i][10]



# from selenium import webdriver
# import unittest
# class Test1(unittest.TestCase):
#     # 一、准备浏览器驱动、网站地址
#     # setUp在每个测试函数运行前运行，注意大小写；self不能省略
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.baseurl="https://www.baidu.com"
#     # 二、打开浏览器，发送请求
#     # 函数名必须以test开头
#     def test_01(self):
#         browser=self.driver
#         browser.get(self.baseurl)
#     # 四、调用方法，判断元素是否存在
#         flag=Test1.isElementExist(self,"input")
#         if flag:
#             print('该元素存在')
#         else:
#             print('该元素不存在')
#     # 三、判断元素是否存在的方法
#     def isElementExist(self):
#         flag=True
#         browser=self.driver
#         try:
#             browser.find_element_by_css_selector(element)
#             return flag
#         except:
#             flag=False
#             return flag
# # 五、运行所有以test开头的测试方法
# if __name__=="__main__":
#     unittest.main()


# from selenium import webdriver
# import unittest
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# class test1(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.baseurl = "http://www.xebest.com"
#
#     #        self.driver.maximize_window()
#
#     def dengLu(self):
#         browser = self.driver
#
#         browser.get(self.baseurl)
#
#         browser.find_element_by_link_text(u"请登录").click()
#         # 调用isElementExist方法，判断元素是否存在
#         flag = test1.isElementExist(self, "div.popup-content")
#
#         if flag:
#
#             browser.find_element_by_id("userName").send_keys("w74581@163.com")
#             browser.find_element_by_id("password").send_keys("w123456")
#             browser.find_element_by_id("imgLogin").click()
#             print(browser.switch_to_alert().text)
#             browser.switch_to_alert().accept()
#
#
#         else:
#             print("没有弹框")
#
#     #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
#     def isElementExist(self, element):
#         flag = True
#         browser = self.driver
#         try:
#             browser.find_element_by_css_selector(element)
#             return flag
#
#         except:
#             flag = False
#             return flag
#
# if __name__=="__main__":
#     # unittest.main()
#     test10=test1
#     test10.setUp()
#     test10.dengLu()
#     test10.isElementExist()





# dr.find_element_by_class_name('el-popper el-cascader__dropdown').find_element_by_class_name('el-cascader-panel').find_element_by_class_name('el-scrollbar el-cascader-menu').find_element_by_class_name('el-cascader-menu__wrap el-scrollbar__wrap').find_element_by_class_name('el-scrollbar__view el-cascader-menu__list').find_element_by_class_name('el-cascader-node').find_element_by_class_name('el-cascader-node__label').click()





from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
# 导入模仿键盘操作模块
from selenium.webdriver.common.keys import Keys
# 导入模仿鼠标操作模块
from selenium.webdriver.common.action_chains import ActionChains
