from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
# 导入模仿键盘操作模块
from selenium.webdriver.common.keys import Keys
# 导入模仿鼠标操作模块
from selenium.webdriver.common.action_chains import ActionChains



# 打开浏览器
# dr = webdriver.Chrome()
# # 请求的网址
# # dr.get('https://mail.qq.com')
# dr.get('https://www.jd.com')
# # 将鼠标移动到某个元素上
#
# ww = dr.find_elements_by_xpath('//*[@id="J_cate"]/ul/li')
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)

# //*[@id="J_cate"]/ul/li[1]








# ——模拟用户操作（模拟鼠标）——
# 语法格式   控制鼠标去做一些动作     perform()立即去做
# ActionChains(dr).click().perform()

# ww = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_item')
# print(ww)
# for i in ww:
#     start = dr.find


# 打开浏览器
# dr = webdriver.Chrome()
# # 打开豆瓣网址
# dr.get('https://www.douban.com')
# # 定位元素
# dr.find_element_by_xpath('//*[@id="anony-music"]')
# # 定位并定义起始位置
# start = dr.find_element_by_xpath('//*[@id="anony-music"]/div[1]/div[3]/div[1]/ul/li[1]/div[2]')
# # 定位并定义结束位置
# end = dr.find_element_by_xpath('//*[@id="anony-music"]/div[1]/div[3]/div[1]/ul/li[2]/div[3]')
# # 操控鼠标从开始（start）位置点击并按住，移动到结束（end）位置，选中文本，鼠标松开，键盘按下Ctrl+C键复制选中文本，键盘松开Ctrl+C键，perform立即执行
# ww = ActionChains(dr).click_and_hold(start).move_to_element(end).release().key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).send_keys('c').perform()
# sleep(3)
# # 打开百度网址
# dr.get('http://www.baidu.com')
# sleep(5)
# # 定位搜索框并将复制内容粘贴
# dr.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')




# # ——自动登录QQ邮箱发送邮件——
# # 打开浏览器
# dr=webdriver.Chrome()
# # 获取QQ邮箱网页
# dr.get('https://mail.qq.com/')
# # 切换进框架
# dr.switch_to.frame('login_frame')
# sleep(2)
# # 强制等待20秒等待定位qq账号输入框并输入账号
# a=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_id('u'))
# a.send_keys('1557942939')
# # 强制等待20秒等待定位qq密码输入框并输入密码
# b=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_id('p'))
# b.send_keys('meiyoumima233')
# # 定位登录按钮并点击
# dr.find_element_by_id('login_button').click()
# sleep(5)
# # 写入for循环，循环发送邮件
# for i in range(5):
#     # 点击写信按钮
#     dr.find_element_by_id('composebtn').click()
#     # 切换进写信框架
#     dr.switch_to.frame('mainFrame')
#     sleep(2)
#     # 定位发送人输入框并输入
#     dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('729848103@qq.com')
#     # 定位标题输入框并输入
#     dr.find_element_by_id('subject').send_keys("test")
#     sleep(1)
#     # 切换进正文框架
#     dr.switch_to.frame(dr.find_element_by_class_name('qmEditorIfrmEditArea'))
#     sleep(1)
#     # 定位正文输入框位置并输入
#     dr.find_element_by_xpath('/html/body').send_keys('亲爱的达瓦里氏，冬天就要到了，多穿衣服，注意保暖！')
#     # 退出到上层框架
#     dr.switch_to.parent_frame()
#     # 定位发送按钮并点击
#     dr.find_element_by_name('sendbtn').click()
#     # 退出所有框架
#     dr.switch_to.default_content()
#     print("邮件已发送")
#     sleep(3)



# # 18317822978@163.com
# # 1101303023@qq.com


# 打开浏览器
# dr=webdriver.Chrome()
# # 获取网页
# dr.get('file:///D:/liulanqi_asdasda/abc_1.html')
# sleep(2)
# # 定位试一试按钮并点击
# dr.find_element_by_xpath('/html/body/button').click()
# sleep(2)
# # 处理alert弹出框
# ss = dr.switch_to.alert
# # 获取弹出框文本
# ss.text
# # 点击输入
# ss.send_keys('卡瓦斯基')
# # 选项一：点击确定
# ss.accept()
# # 选项二;点击取消
# # ss.dismiss()



# dr=webdriver.Chrome()
# dr.get('https://www.douban.com/')
# sleep(2)
# # 切换窗口  浏览器唯一标识一个窗口：句柄
# # 获取当前所在窗口的句柄 结果是个列表：
# # 在首页打开      【1，4，3，2】
# # 在新打开页面打开【1，2，3，4】
# print(dr.title)
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(5)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()
# # 获取所有打开窗口的句柄
# print(dr.window_handles)
# handles_all=dr.window_handles
# # 切换窗口  值只能填写——句柄——
# dr.switch_to.window(handles_all[-1])
# print(dr.title)
# sleep(2)
# dr.switch_to.window(handles_all[-2])
# print(dr.title)



# ——验证码滑动验证——
# 打开浏览器
# dr=webdriver.Chrome()
# # 获取QQ邮箱网页
# dr.get('https://mail.qq.com/')
# # 切换进账号密码框架
# dr.switch_to.frame('login_frame')
# sleep(2)
# # 定位账号输入框输入账号
# a=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_id('u'))
# a.send_keys('1557945984')
# # 定位密码输入框输入密码
# b=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_id('p'))
# b.send_keys('meiyoumim2533')
# sleep(2)
# # 点击登录
# dr.find_element_by_id('login_button').click()
# sleep(2)
# # 切换进验证码框架
# dr.switch_to.frame('tcaptcha_iframe')
# sleep(2)
# # 定位拖拽按钮
# start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# # 进行拖拽
# ActionChains(dr).drag_and_drop_by_offset(start,188,0).perform()
# print("拖拽完成")
# sleep(5)
# dr.quit()



# ——浏览器上下滑动栏定格滑动——
# dr=webdriver.Chrome()
# dr.get('https://www.jd.com')
#
# # 第一种：通过高度定位，最高点为0
# # 挪动滚动条
# list1=[500,1000,2000,3000,4000,5000]
# for i in list1:
#     js = f"var q=document.documentElement.scrollTop={i}"
#     # 执行jjavascript代码
#     dr.execute_script(js)
#     sleep(2)
#
# # 第二种：通过位置定位滑动结束点
# dd = dr.find_element_by_xpath('//*[@id="J_footer"]/div[1]')
# dr.execute_script('arguments[0].scrollIntoView();',dd)



# # 打开chrome浏览器
# dr = webdriver.Chrome()
# # 打开益起买后台管理系统网页页面
# dr.get('http://pcc.tianxingcaifu.cn/')
#
# # 点击登录
# dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/form/button').click()
# sleep(5)
#
# # 点击首页下拉框
# dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/i').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[2]').move_to_element()
# dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[3]').move_to_element()


from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time as t
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com")
t.sleep(3)
element = driver.find_element_by_link_text(u'设置')
ActionChains(driver).move_to_element(element).perform()
t.sleep(3)
element = driver.find_element_by_link_text(u'搜索设置').click()
st = driver.find_element_by_id('nr')
Select(st).select_by_index(1)#select_by_index
t.sleep(5)
driver.quit()



