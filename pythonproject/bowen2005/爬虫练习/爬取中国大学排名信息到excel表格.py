import requests
import re
import xlwt


class UniversityInfo():
    def __init__(self):
        self.url = f'http://www.shanghairanking.cn/rankings/bcur/202011'
        self.head = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
            }

    def request_info(self):
        list1 = []
        r = requests.get(self.url, headers=self.head)
        a = r.content.decode('utf-8')
        # 所有学校过滤之前的信息，包括链接之类的(以列表的形式显示)
        b = re.findall('<tr data-v-45ac69d8><td data-v-45ac69d8>(.*?)</td></tr>', a, re.S)
        for i in b:
            # 过滤掉</td>等每个学校的信息(以列表的形式显示)
            c = re.findall('data-v-45ac69d8>(.*?)</td>', i ,re.S)
            # 过滤出带链接的学校名(以列表的形式显示，每个列表中只有一个元素)
            d = re.findall('<a (.*?)</a>', c[0], re.S)
            for j in d:
                # 将每个学校名称前的链接取出(以列表的形式显示，每个列表中只有一个元素)
                e = re.findall('href=(.*?) data-v-45ac69d8>', j, re.S)
                # 替换掉学校名称前的内容，只保留学校名称
                f = j.replace(f'href={e[0]} data-v-45ac69d8>', '')
            # 每个学校的除了学校名称以外的信息(以列表的形式显示)
            g = re.findall('<td data-v-45ac69d8>(.*?)</td>', i, re.S)
            # print(g)
            # 存放每个学校的三个信息(为了去除空行)
            list2 = []
            for k in g:
                # 删除空行，并将数据追加到list2列表中
                list2.append(k.strip())
            # 将学校的名称，追加到list2列表中(现在列表中有4个数据)
            list2.insert(0, f)
            list1.append(list2)
        return list1


    # 保存数据到excel表格
    def save_info(self):
        # 接收request_info()方法返回的一个大列表
        # (列表中包含每个小列表，每个小列表中包含4个信息)
        list3 = self.request_info()
        f = xlwt.Workbook(encoding='utf8')
        sheet = f.add_sheet('学校信息')
        # 创建一个列表，用来循环插入表头
        list4 = ["排名", "学校名称", "省市", "类型", "总分"]
        for c, d in enumerate(list4):
            sheet.write(0, c, d)
        # 第一个循环将大列表list3拆成多个小列表，
        # 赋给b，   a是下标，从1开始，用到后面插入数据
        for a, b in enumerate(list3, 1):
            # 每个小列表中少了一个元素(排名)，
            # 将排名插入到每个小列表的第一个
            b.insert(0, a)
            # 将小列表中的数据循环插入到excel表格中
            # j是纵坐标，a是横坐标，k是要插入的值
            for j, k in enumerate(b):
                sheet.write(a, j, k)
        f.save('university.xls')


if __name__ == '__main__':
    u1 = UniversityInfo()
    u1.save_info()


