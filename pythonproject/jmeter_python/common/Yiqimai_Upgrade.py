from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
import logging.config
import csv
logging.config.fileConfig("../config/peizhi_logcat.conf") # 匹配日志文件
logging=logging.getLogger() # 采集器


def add():
    # 打开chrome浏览器
    dr = webdriver.Chrome()
    logging.info("打开浏览器")

    # 打开益起买后台管理系统网页页面
    dr.get('http://pcc.tianxingcaifu.cn/')
    logging.info("打开网站")

    # 点击登录\
    a = WebDriverWait(dr, 30).until(
        lambda dr: dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/form/button'))
    a.click()
    # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/form/button').click()
    logging.info("登录网站")
    sleep(2)

    # 读取csv文件数据
    data = []
    with open(r'C:\Users\admin\Desktop\Yiqimai.csv', 'r') as f:
        reader = csv.reader(f)
        # print(type(reader))
        for i in reader:
            data.append(i)
        # print(data)

    for i in range(1,2):
        # 商品名称
        goods_name = data[i][0]
        # 商品简介
        goods_introduce = data[i][1]
        # 商品价格
        goods_price = data[i][5]
        # 商品主图路径
        main_picture = data[i][2]
        # 商品轮播图路径
        roulette_picture = data[i][3]
        # 商品详情图路径
        detail_picture = data[i][4]
        # 划线价格
        wrong_price = data[i][6]
        # 商品库存
        goods_stock = data[i][7]
        # 销售件数
        quantity_sold = data[i][8]
        # 拼团名称
        group_name = data[i][9]
        # 拼团商品
        group_goods_name = data[i][10]
        # 警示价格
        minimum_price = data[i][11]
        # 参团人数
        number_of_people = data[i][12]

        # 点击展开功能下拉框
        a = WebDriverWait(dr, 20).until(
            lambda dr: dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/i'))
        a.click()
        # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/i').click()
        logging.info('展开功能下拉框')
        sleep(1)

        # 点击商品列表按钮
        # a=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[2]'))
        # a.click()
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[1]/div/ul/li[2]').click()
        logging.info("跳转商品列表")
        sleep(1)

        # 点击添加按钮
        b=WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div[1]/form/div[3]/div/button[2]'))
        b.click()
        logging.info("点击添加商品")
        logging.info("页面跳转至基本信息页面")
        sleep(1)

        # 点击商品名称输入框输入
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[1]/div/div[1]/input').send_keys(goods_name)
        logging.info("输入商品名")
        sleep(1)

        # 点击商品简介输入框输入
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[2]/div/div[1]/textarea').send_keys(goods_introduce)
        logging.info("商品简介")
        sleep(1)

        # 点击所属分类选择框
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[3]/div/div/div/span/span/i').click()
        sleep(1)
        logging.info("选择所属分类")

        # 选择商品种类
        dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/span').click()
        logging.info('选择商品类型')
        sleep(1)

        # 选择商品名称
        dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/span').click()
        logging.info('选择商品名称')
        sleep(1)

        # 点击商品选择便签框
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[4]/div/div/label[1]/span[1]/span').click()
        logging.info("选择商品标签")
        sleep(2)

        # 上传商品主图
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[5]/div/div').find_element_by_css_selector(
            "[type='file']").send_keys(main_picture)
        logging.info("上传主图")
        sleep(2)

        # 上传商品轮播图
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[6]/div/div/div/div').find_element_by_css_selector("[type='file']").send_keys(roulette_picture)
        # dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[6]/div/div/div[2]/div').find_element_by_css_selector("[type='file']").send_keys()
        logging.info("上传轮播图")
        sleep(2)

        # 上传商品详情图
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/form/div[7]/div/div[2]/div/div').find_element_by_css_selector("[type='file']").send_keys(detail_picture)
        logging.info("上传详情图")
        sleep(2)

        # 点击下一步
        dr.find_element_by_xpath('//*[@id="pane-first"]/div/div/button[1]').click()
        logging.info("页面跳转至价格信息页面")
        sleep(2)

        # 输入商品价格
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[2]/div/div/div[1]/input').send_keys(goods_price)
        logging.info("输入商品价格")
        sleep(1)

        # 输入划线价格
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[3]/div/div/div/input').send_keys(wrong_price)
        logging.info("输入划线价格")
        sleep(1)

        # 输入商品库存量
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[4]/div/div/div/input').send_keys(goods_stock)
        logging.info("输入商品库存")
        sleep(1)

        # 选择商品是否显示详情
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[5]/div/div/div/label[1]/span[1]/span').click()
        logging.info('商品详情')
        sleep(1)

        # 输入销售件数
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[6]/div/div/div/input').send_keys(quantity_sold)
        logging.info('输入销售件数')

        # 选择商品是否显示数量
        dr.find_element_by_xpath('//*[@id="pane-second"]/div/div/form/div[7]/div/div/div/label[1]/span[1]/span').click()
        logging.info('商品数量')
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
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div').click()
        logging.info('商品上架')
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
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[2]/div/div/div[1]/input').send_keys(group_name)
        logging.info('输入拼团名')

        # 选择开始时间
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/input').click()
        sleep(2)
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
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[5]/div/div/div/div/input').send_keys(group_goods_name)
        sleep(1)
        a = WebDriverWait(dr,20).until(lambda dr:dr.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li'))
        a.click()
        logging.info('选择商品')
        sleep(1)

        # 输如拼团警示价格
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[3]/div/div[1]/input').send_keys(minimum_price)
        logging.info('警示价格')
        sleep(1)

        # 选择全款支付
        # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[7]/div/div/div/label[1]/span[1]/span').click()

        # 输入参团人数
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div[1]/div[2]/div[2]/div/div/form/div[10]/div/div/div/input').send_keys(number_of_people)
        logging.info('参团人数')

        # 选择固定阶梯支付方式
        # dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/form/div[10]/div/div/div/label[1]/span[1]/span').click()

        # 点击提交
        dr.find_element_by_xpath('//*[@id="vue-admin-beautiful"]/div/div/div[2]/div[2]/div/div/div/button[1]').click()
        logging.info('提交拼团')
        logging.info('拼团创建成功')
        sleep(3)
        logging.info('')
        logging.info('')

    # 关闭浏览器
    dr.quit()
    logging.info('浏览器关闭')


if __name__=="__main__":
    # 忽略userwarning兼容性警告
    import warnings
    warnings.filterwarnings("ignore")
    print('END')
    pass
    # 运行add函数下代码
    add()










