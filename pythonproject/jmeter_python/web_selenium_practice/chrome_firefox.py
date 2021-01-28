# 导入selenium模块下webdriver模块
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# 打开浏览器
dr = webdriver.Chrome()
# 请求网址
dr.get('https://www.ctrip.com')

# 切换进框架内——内嵌框架
# 1.只能用name的值或id的值
# 2.先定位到，在切换
dr.switch_to.frame('login_frame')
dd = dr.find_element_by_xpath('//*[@id="tcaptcha_iframe"]')
dr.switch_to.frame(dd)
# 退出框架
# 1.退出到最外层框架
dr.switch_to.default_content()
# 2.退出到上层框架
dr.switch_to.parent_frame()


# 强制等待
sleep(2)
# 隐式等待
dr.implicitly_wait(20)
# 显式等待
WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath(""))

sleep(2)
# dr.find_element_by_xpath('//*[@id="searchBox"]/div[1]')
ww = dr.find_element_by_id('J_roomCountList').find_elements_by_tag_name('option')
for i in ww:
    i.click()
    sleep(2)
sleep(2)
dr.close()


# ——核心——：——定位——
# app：id, class, xpath, list, tap, swipe,
# web：id, class, xpath(路径标记语言), name, css, partial_link_text, link_text, tag_name

# 唯一度css最高
# css > xpath > name > id == class > link_text

# web端id一般是唯一的，class不一定是唯一的
# 单个元素定位方法
# ——id定位——
# dr.find_element_by_id('kw').send_keys('国旗')
# ——class定位——
# dr.find_element_by_class_name('s_ipt').send_keys('国界')
# ——xpath定位——
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('国徽')
# ——name定位——
# dr.find_element_by_name('wd').send_keys('苏联')
# ——css定位——，css层叠样式表：渲染网页
# dr.find_element_by_css_selector('#kw').send_keys('宇宙')
# ——link_text——，通过文本内容定位
# dr.find_element_by_link_text('新闻').click()
# ——partial_link_text——，通过模糊文本定位
# dr.find_element_by_partial_link_text('地').click()
# ——tag_name——，通过标签名来定位，重复率高，通常不用来定位单个元素

# list定位  获取同种属性的所有元素，结果是个列表
# 相对定位  新定义一个大的区域，在从大区域中定位
# 定义的大区域，必须是唯一的，
# 后边在定位，可以是唯一的，也可以是list定位

# dr.find_element_by_id('su').click()

# for i in range(1,11):

# list1=[]
# list1.append(dr.find_element_by_class_name('s_item'))
# print(list1)



# dr.set_window_position(400,400)
# print(dr.title)
# dr.get('https://www.jd.com')
# sleep(2)
# print(dr.title)
# # 返回键
# dr.back()
# sleep(1)
# dr.forward()

# cr = webdriver.Firefox()
# cr.get('https://www.baidu.com')

# 获取网页标题
# print(dr.title)
# 断言
# assert dr.title  == "百度一下，你就知道"
# 设置浏览器窗口大小
# dr.set_window_size(400,400)   # 单位：像素 px
# sleep(1)
# 浏览器窗口最小化
# dr.minimize_window()
# 浏览器窗口最大话
# dr.maximize_window()



# sleep(10)
# 关闭浏览器 dr.quit()
# 关闭窗口（只能关闭一个，如果浏览器只有一个窗口，自然就能关闭浏览器）
# dr.close()
