
# ——————————————————————————————字符串函数和方法：
# 字符串的常用操作方法有查找，修改 和 判断三大类

# str1="abCxyZ"
# str2="have a Good day , See you"

# 1.——find()：检测某个字符串是否包含在这个字符串内，
# 如果在则返回这个字符串所在位置下标，否则返回-1。
# str1="abCxyZ"
# print(str1.find("a"))# 0：
# print(str1.find("e"))# -1

# 2.——index()：检测检测某个字符串是否包含在这个字符串内，
# # # 如果在则返回这个字符串所在位置下标，否则报异常。
# str1="abCxyZ"
# print(str1.index("a"))# 0
# print(str1.index("e"))# 报错
# rfind():和rindex():与find():和index():功能相同，但查找方向从右侧开始。

# 3.——replace()：替换。所谓修改字符串，
# 指的就是通过函数的形式修改字符串中的数据。
# str1="abCxyZ"
# print(str1.replace("a","e"))# ebCxyZ
# print(str1.replace("C",""))# abxyZ

# 4.——split():按照指定字符分割字符串,分割后数据类型变为 列表。
# 如果分割字符是原有字符串中的子串，分割后则丢失该字符。
# str1="abCxyZ"
# str2="have a Good day , See you"
# print(str1.split("C"))# ['ab', 'xyZ']
# print(str2.split(" ",3))# ['have', 'a', 'good', 'day , see you']

# 5.——jion():合并。用一个字符或子串合并字符串，
# 即是将多个字符串合并为一个新的字符串。
# list1=["hello","world","goodbye","world"]
# t1=("aa","b","ccc","d")
# print("-".join(list1))# hello-world-goodbye-world
# print("..".join(t1))# aa..b..ccc..d

# 6.——capitalize():将字符串第一个字符转大写,
# 注意：capitalize函数转换后，字符串第一个字符大写，其余的字符全部小写
# str2="have a Good day , See you"
# print(str2.capitalize())# Have a good day , see you

# 7.——title():将字符串每个单词的首字母转换成大写。
# str2="have a Good day , See you"
# print(str2.title())# Have A Good Day , See You

# lower():将字符串大写转小写
# str2="have a Good day , See you"
# print(str2.lower())# have a good day , see you

# upper():将字符串中小写转大写
# str2="have a Good day , See you"
# print(str2.upper())# HAVE A GOOD DAY , SEE YOU

# istrip():删除字符串左侧空白
# rstrip():删除字符串右侧空白
# strip():删除字符串两侧空白
# str3="   asdaefv   "
# print(str3.lstrip())  # "asdaefv   "
# print(str3.rstrip())  # "   asdaefv"
# print(str3.strip())   # asdaefv

# ljust():返回一个源字符串左侧对齐
# ljust():返回一个源字符串右侧对齐
# center():返回一个源字符串居中对齐
# str4="hello"
# print(str4.ljust(10,"."))# "hello....."
# print(str4.rjust(10,"."))# ".....hello"
# print(str4.center(10,"."))# ..hello...

# 判断。所谓判断既是判断真假，返回的结果是布尔类型：True或False
# startwiith():检查字符串是否以指定子串开头，是返回True,不是则返回False
# str1="abCxyZ"
# print(str1.startswith("a"))# True
# print(str1.startswith("Z"))# False
# endwith():检查字符串是否以指定子串结尾，是返回True,不是则返回False
# str1="abCxyZ"
# print(str1.endswith("a"))# False
# print(str1.endswith("Z"))# True

# isalpha():如果字符串至少有一个字符并且所有的字符都是字母则返回True，否则返回False
# str1="abCxyZ"
# print(str1.isalpha())# True
# mystr="12sdf234ddg45ff"
# print(mystr.isalpha())# False

# isdigit():如果字符串只包含数字则返回True，否则返回False
# mystr="123456789"
# print(mystr.isdigit())# True

# isalnum():如果字符串至少有一个字符并且所有的字符都是字母或数字则返回True，否则返回False
# mystr="123abc"
# print(mystr.isalnum())# True

# isspace():如果字符串只包含空白则返回True，否则返回False
# mystr1="      "
# mystr2="1 2 3 4 5"
# print(mystr1.isspace())# True
# print(mystr2.isspace())# False


# ——————————————————————————————列表函数和方法：
# 列表可以一次性存储多个数据，
# 可以对数据进行的操作有：增，删，改，差

# 查找：通过下标
# list1=["Tom","Make","Rose"]
# print(list1[0])# Tom
# print(list1[1])#  Make
# print(list1[2])#  Rose

# index():返回指定数据所在位置的下标
# list1=["Tom","Make","Rose"]
# print(list1.index("Tom",0,2))# 0 如果查找数据不存在则报错

# count():统计指定数据在当前列表出现的次数。
# list1=["Tom","Make","Rose"]
# print(list1.count("Tom"))# 1

# len():访问列表长度，即列表中数据的个数
# list1=["Tom","Make","Rose"]
# print(len(list1)) # 3

# 判断是否存在
# in：判断指定数据在某个列表序列，如果在返回True，否则返回False
# list1=["Tom","Make","Rose"]
# print("Tom"in list1)# True
# print("Ben"in list1) # False

# not:判断指定数据在某个列表序列，如果不在返回True，否则返回False
# list1=["Tom","Make","Rose"]
# print("Tom"not in list1)# False
# print("Ben"not in list1) # True

# 增加
# 作用：增加指定数据到列表中。
# append():列表结尾追加数据。
# list1=["Tom","Make","Rose"]
# list1.append("Ben")
# print(list1) # ['Tom', 'Make', 'Rose', 'Ben']

# extend():列表结尾追加数据，
# 如果数据是一个序列，则将这个序列的数据追一添加到列表。
# list1=["Tom","Make","Rose"]
# list2=["zhangsan","lisi"]
# list1.extend(list2)
# print(list1) # ['Tom', 'Make', 'Rose', 'zhangsan', 'lisi']

# insert():指定位置新增数据
# list1=["Tom","Make","Rose"]
# list1.insert(0,"lisi")
# print(list1)  # ['lisi', 'Tom', 'Make', 'Rose']

# 删除
# del→关键字，del()→函数

# 删除列表
# list1=["Tom","Make","Rose"]
# del list1
# print(list1) # NameError: name 'list1' is not defined

# 删除列表中的数据
# list1=["Tom","Make","Rose"]
# del list1[1]
# print(list1) # ['Tom', 'Rose']

# pop():删除指定下标的数据（默认为最后一个），并返回该数据
# list1=["Tom","Make","Rose"]
# list2=["张三","李四","王五"]
# list1.pop()
# print(list1) # ['Tom', 'Make']
# list2.pop(0)
# print(list2) # ['李四', '王五']

# remove():移除列表中某个数据的第一匹配项
# list1=["Tom","Make","Rose"]
# list1.remove("Make")
# print(list1) # ['Tom', 'Rose']

# clear():清空列表
# list1=["Tom","Make","Rose"]
# list1.clear()
# print(list1) # [] 列表数据被清空

# 修改
# 修改指定数据
# list1=["Tom","Make","Rose"]
# list1[0]=""
# print(list1) # ['', 'Make', 'Rose']

# reversed():逆置，颠倒
# reverse排序规则：reverse = True 降序，reverse = False 降序。
# list1=  ["Tom","Make","Rose"]
# list1.reverse()
# print(list1) # ['Rose', 'Make', 'Tom']

# 排序：sort(),sorted():排序，针对集合，元组排序，排序后会将数据格式转为列表
# list1.sort(reverse=False):默认不能颠倒
# list1=  [2,19,7,31,15]
# list1.sort()
# print(list1) # [2, 7, 15, 19, 31]

# ——————————————————————————————元组
# 一个元组可以存储多个数据，元组内的数据是不能修改的
# 元组的特点：定义元组使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型。
# 如果定义的元组只有一个数据，那么这个数据后面也要添加逗号，否则数据类型为唯一的这个数据的数据的数据类型
# 如果元组里边有列表，修改列表里边的数据则是支持的
# t1=(10,)
# print(type(t1)) # <class 'tuple'>
# t2=(20)
# print(type(t2)) # <class 'int'>
# t3=("hello")
# print(type(t3)) # <class 'str'>

# 元组数据不支持修改，只支持查找
# index():查找某个数据，如果数据存在返回对应的下标，否则报错。
# t1=("aa","bb","cc","dd","ee")
# print(t1.index("cc"))  # 2

# count():统计某个元素在当前元组中出现的次数
# t1=("aa","bb","cc","dd","ee")
# print(t1.count("aa")) # 1

# len():统计元组中数据的个数
# t1=("aa","bb","cc","dd","ee")
# print(len(t1)) # 5


# ——————————————————————————————集合
# 创建集合使用{}或set{}，但是如果要创建空集合只能使用set()，因为{}用来创建空字典
# set1={10,40,30,20}
# print(set1) # 集合是无序的：{40, 10, 20, 30}
# set2={10,10,40,30,40,30,20,20}
# print(set2) # 集合具有去重功能：{40, 10, 20, 30}
# set3=set("sdfhhgdsa")
# print(set3) # 字符串转集合，每个字符会被当成一个元素：{'g', 'a', 'd', 'h', 's', 'f'}
# set4=set()
# print(type(set4)) # 数据类型：<class 'set'>
# set5={}
# print(type(set5)) # 数据类型：<class 'dict'>

# add():增加数据
# s1={10,20}
# s1.add(100)
# print(s1) # {100, 10, 20}

# 因为集合有去重功能，所以，当向集合中追加数据的数据是当前已有的数据的话，则不进行任何操作
# update():追加的数据是序列
# s1={10,20}
# s1.update([100,200])
# print(s1) # {100, 10, 20, 200}
# s1.update("abc")
# print(s1) # {100, 'a', 200, 'b', 10, 'c', 20}
# s1.update(100)
# print(s1) # TypeError: 'int' object is not iterable
#           # 报错，追加的必须是一个序列

# 删除
# remove()：删除集合中的指定数据，如果数据不存在则报错
# s1={10,20,30}
# s1.remove(10)
# print(s1) # {20, 30}
# s1.remove(10)
# print(s1) # KeyError: 10

# discard():删除集合中的指定数据，如果数据不存在也不会报错
# s1={10,20,30}
# s1.discard(10)
# print(s1) # {20, 30}
# s1.discard(10)
# print(s1) # {20, 30}

# pop():随机删除集合中的某个数据，并返回这个数据
# s1={10,20,30}
# a=s1.pop()
# print(a) # 10
# print(s1) # {20, 30}

# 查找数据
# in：判断数据在集合序列
# not in：判断数据不在集合序列
# s1={10,20,30,40}
# print(10 in s1) # True
# print(60 in s1)# False
# print(20 not in s1)# False
# print(50 not in s1)# True


# ——————————————————————————————字典
# 字典是可变的，有序的（依靠键值对的形式查找），以键值对形式存储数据
# 字典的特点：符号为大括号；
#            数据为键值对的形式出现；
#            各个键值之间用逗号隔开

# 增
# 字典序列[key]=值
# 如果key值存在则修改对应的值，如果key不存在则新增此键值对。
# dict1={"name":"lisi","age":20,"sex":"men"}
# dict1["name"]="Make"
# print(dict1) # {'name': 'Make', 'age': 20, 'sex': 'men'}
# dict1["id"]=1001
# print(dict1) # {'name': 'Make', 'age': 20, 'sex': 'men', 'id': 1001}

# # 十进制转八进制
# print(oct(10))
# # 十进制转十六进制
# print(hex(10))
# # 十进制转二进制
# print(bin(10))
# 任何进制转十进制
# print(int("20"))


import pymysql


conn=pymysql.connect(
    host="192.168.2.163",
    port=3306,
    user="root",
    passwd="111111"
)


mycusor=conn.cursor()
#
mycusor.execute("show databases")
mycusor.execute("use bowen")
mycusor.execute("show tables")
conn.commit()
# a=mycusor.fetchall()
# print(a)
a=mycusor.fetchmany(2)
print(a)
# a=mycusor.fetchone()
# print(a)



















