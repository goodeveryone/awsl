from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
import logging.config
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
# 导入模仿键盘操作模块
from selenium.webdriver.common.keys import Keys
# 导入模仿鼠标操作模块
from selenium.webdriver.common.action_chains import ActionChains

# 匹配日志文件
logging.config.fileConfig("../config/peizhi_logcat.conf")
# 采集器
logging=logging.getLogger()

# 登录新增商品
def add():
    # 打开chrome浏览器
    dr = webdriver.Chrome()
    logging.info("打开浏览器")

    # 打开益起买后台管理系统网页页面
    dr.get('http://pcc.tianxingcaifu.cn/')
    logging.info("打开网站")

    # 点击登录\
    a = WebDriverWait(dr,30).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/form/button'))
    a.click()
    # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/form/button').click()
    logging.info("登录网站")
    # 点击商品列表按钮
    a=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[2]'))
    a.click()
    logging.info("跳转商品列表")
    sleep(1)

    # 点击添加按钮
    b=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div[1]/form/div[3]/div/button[2]'))
    b.click()
    logging.info("点击添加商品")
    logging.info("页面跳转至价格信息页面")
    sleep(1)

    # 点击商品名称输入框输入
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[1]/div/div[1]/input').send_keys('123')
    logging.info("输入商品名")
    sleep(1)

    # 点击商品简介输入框输入
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[2]/div/div[1]/textarea').send_keys('123')
    logging.info("商品简介")
    sleep(1)

    # 点击所属分类选择框
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[3]/div/div/div/input').click()
    sleep(2)
    logging.info("选择所属分类")

    # 选择商品种类
    dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/span').click()
    logging.info('选择商品类型')
    sleep(2)

    # 选择商品名称
    dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/span').click()
    logging.info('选择商品名称')
    sleep(2)

    # 点击商品选择便签框
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[4]/div/div/label[1]/span[1]/span').click()
    logging.info("选择商品标签")
    sleep(1)

    # 上传商品主图
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[5]/div/div').find_element_by_css_selector("[type='file']").send_keys(r'C:\Users\admin\Pictures\Camera Roll\1.jpg')
    logging.info("上传主图")
    sleep(2)

    # 上传商品轮播图
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[6]/div/div').find_element_by_css_selector("[type='file']").send_keys(r'C:\Users\admin\Pictures\Camera Roll\2.jpg')
    logging.info("上传轮播图")
    sleep(2)

    # 上传商品详情图
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[7]/div/div[2]').find_element_by_css_selector("[type='file']").send_keys(r'C:\Users\admin\Pictures\Camera Roll\3.jpg')
    logging.info("上传详情图")
    sleep(2)

    # 点击下一步
    dr.find_element_by_xpath('//*[@id="pane-first"]/div/div/button[1]').click()
    logging.info("页面跳转至价格信息页面")
    sleep(2)

    # 输入商品价格
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[2]/div/div/div[1]/input').send_keys('10')
    logging.info("输入商品价格")
    sleep(1)

    # 输入划线价格
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[3]/div/div/div/input').send_keys('50')
    logging.info("输入划线价格")
    sleep(1)

    # 输入商品库存量
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[4]/div/div/div/input').send_keys('1000')
    logging.info("输入商品库存")
    sleep(1)

    # 选择商品是否显示详情
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[5]/div/div/div/label[1]/span[1]/span').click()
    logging.info('商品详情')
    sleep(1)

    # 输入销售件数
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[6]/div/div/div/input').send_keys('100')
    logging.info('输入销售件数')

    # 选择商品是否显示数量
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[7]/div/div/div/label[1]/span[1]/span').click()
    logging.info('商品数量')
    sleep(1)

    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[9]/div/div/div/label[2]/span[1]/span').click()
    logging.info('设置有佣金')
    sleep(1)

    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[10]/div[1]/div/div/div/input').send_keys('5')
    logging.info('输入佣金比例')
    sleep(1)


    # 点击提交
    dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/div/button[1]').click()
    logging.info('提交商品信息')
    sleep(1)

    # 返回商品列表界面
    dr.find_element_by_xpath('//*[@id="tab-/goods/list"]').click()
    logging.info('商品添加成功')
    sleep(1)

    # 上架商品
    dr.find_element_by_xpath(
        '//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div').click()
    sleep(1)

    # 点击展开功能下拉框
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/i').click()
    logging.info('展开功能下拉框')
    sleep(1)












    #点击拼团列表按钮
    a=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[3]'))
    a.click()
    logging.info('点击拼团列表按钮')
    logging.info('页面跳转拼团列表')
    sleep(1)

    # 点击添加按钮
    b=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div[1]/form/button[2]/i'))
    b.click()
    logging.info('添加拼团')
    sleep(1)

    # 输入拼团名称
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[2]/div/div/div[1]/input').send_keys('中华香烟拼团2')
    logging.info('输入拼团名')

    # 选择开始时间
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/input').click()
    sleep(1)
    dr.find_element_by_xpath('/html/body/div[2]/div[2]/button[1]/span').click()
    logging.info('开始时间')
    sleep(1)

    # 选择结束时间
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[4]/div/div/div/input').click()
    sleep(1)
    dr.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[6]/td[7]/div/span').click()
    sleep(1)
    dr.find_element_by_xpath('/html/body/div[3]/div[2]/button[2]').click()
    logging.info('结束时间')
    sleep(1)

    # 输入拼团商品名称
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[5]/div/div/div/div/input').send_keys('中华香烟')
    sleep(1)
    a = WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li'))
    a.click()
    logging.info('选择商品')
    sleep(1)

    # 输如拼团警示价格
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[3]/div/div[1]/input').send_keys('10')
    logging.info('警示价格')
    sleep(1)

    # 选择全款支付
    # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[7]/div/div/div/label[1]/span[1]/span').click()

    # 输入参团人数
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div[1]/div[2]/div[2]/div/div/form/div[10]/div/div/div/input').send_keys('10')
    logging.info('参团人数')

    # 选择固定阶梯支付方式
    # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[10]/div/div/div/label[1]/span[1]/span').click()

    # 点击提交
    dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/div/button[1]').click()
    logging.info('提交拼团')
    logging.info('拼团创建成功')
    sleep(5)
    logging.info('浏览器关闭')



if __name__=="__main__":
    # 忽略userwaring兼容性警告
    import warnings
    warnings.filterwarnings("ignore")
    print('END')
    pass

    add()


