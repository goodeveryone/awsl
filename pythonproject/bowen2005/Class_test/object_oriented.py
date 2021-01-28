# class person:
#     def __init__(self,a,b,c):
#         self.name=a
#         self.age=b
#         self.height=c
#     def run(self,a):
#         print(f"{a}爱跑步")
#     def eat(self,a):
#         print(f"{a}吃东西")
#         print(self)
#
# xiaoming=person("小明",18,1.75)
# print(xiaoming)
# xiaoming.run(xiaoming.name)
# xiaoming.eat(xiaoming.name)
#
# xiaomei=person("小美",18,1.65)


# class dog():
#     def __init__(self,a,b):
#         self.name=a
#         self.colour=b
#     def barks(self,a):
#         print(f"{a}见到生人汪汪叫")
#     def wag(self,a):
#         print(f"{a}见到家人摇尾巴")
#     def __str__(self):
#         return f"{self.name}的颜色是{self.colour}"
# xiaohuang=dog("小黄","黄色")
# # xiaohuang.barks(xiaohuang.name)
# # xiaohuang.wag(xiaohuang.name)
# print(xiaohuang)
#
# xiaobai=dog("小白","白色")
# # xiaobai.barks(xiaobai.name)
# # xiaobai.wag(xiaobai.name)
# print(xiaobai)

# class target():
#     def __init__(self,a):
#         self.name=a
#     def


# class player():
#     def __init__(self,a,b):
#         self.name=a
#         self.weight=b
#     def run(self):
#         self.weight -= 0.5
#     def eat(self):
#         self.weight += 1
#     def __str__(self):
#         return f"{self.name}的体重为{self.weight}斤"
#
# xiaoming=player("小明",75)
# xiaoming.run()
# xiaoming.eat()
# xiaoming.eat()
# print(xiaoming)
#
# xiaomei=player("小美",45)
# xiaomei.run()
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)

# ————————————————————烤地瓜
# class Food():
#     def __init__(self):
#         self.time=0
#         self.state="生的"
#         self.cond=[]
#     def bake(self,time):
#         self.time=time
#         if 0 < self.time < 3:
#             self.state="生的"
#         elif 3 < self.time < 5:
#             self.state="半生不熟"
#         elif 5 < self.time < 8:
#             self.state="熟的"
#         elif 8 < self.time:
#             self.state="糊了"
#     def add_cond(self,cd):
#         self.cond.append(cd)
#     def __str__(self):
#         return f"烤了{self.time}分钟," \
#                f"现在的状态是{self.state}," \
#                f"放的调料{self.cond}"
#     def __del__(self):
#         print(f"{self}已经被销毁")
# sweetpotato=Food()
# sweetpotato.bake(6)
# sweetpotato.add_cond("胡椒粉")
# sweetpotato.add_cond("辣椒面")
# print(sweetpotato)


# class Furniture():
#     def __init__(self,a,b):
#        self.name=a
#        self.area=b
#
# class House():
#     def __init__(self):
#         self.area=100
#         self.free_area=100
#         self.furniture=[]
#     def add_furniture(self,furn):
#         if self.free_area > furn.area:
#             self.furniture.append(furn.name)
#             self.free_area-=furn.area
#         else:
#             print(f"房子的剩余面积{self.free_area}平米，"
#                   f"家具的面积时{furn.area},无法摆放{furn.name}")
#     def __str__(self):
#         return f"房子的面积有{self.area}平方米，" \
#                f"剩余{self.free_area}平方米，" \
#                f"放置的家具有{self.furniture}"
#
#
# bed=Furniture("床",7)
# sofa=Furniture("沙发",5)
# table=Furniture("桌子",3)
# house1=House()
# house1.add_furniture(bed)
# house1.add_furniture(sofa)
# house1.add_furniture(table)
# print(house1)


# class TestA():
#     def __init__(self):
#         self.name="李白"
#     def testA(self):
#         print(f"我的名字叫{self.name}")
# class TestB(TestA):
#     pass
#
# b=TestB()
# b.testA()


# # 师傅
# class Master():
#     def __init__(self):
#         self.name="古法烹饪手法"
#     def cook(self):
#         print(f"使用{self.name}制作煎饼果子")
# # 学校
# class School():
#     def __init__(self):
#         self.name="现代烹饪手法"
#     def cook(self):
#         print(f"使用{self.name}制作煎饼果子")
# # 学徒
# class Apprentice(Master,School):
#     def __init__(self):
#         self.name="秘制烹饪手法"
#         self.__money = 2000000
#
#     def get_money(self):
#         return self.__money
#
#     def set_money(self):
#         self.__money=1000000
#
#     def cook(self):
#         print(f"使用{self.name}制作煎饼果子")
#
#     def Master_cook(self):
#         Master().__init__()
#         Master().cook()
#
#     def School_cook(self):
#         # super().__init__()
#         # super().cook()
#         # super(School,self).__init__()
#         # super(School,self).cook()
#         School().__init__()
#         School().cook()
# # 徒孙
# class Tusun(Apprentice):
#     pass
#
#
# daming=Apprentice()
# xiaoming=Tusun()
# print(xiaoming.get_money())
# xiaoming.set_money()
# print(xiaoming.get_money())
# xiaoming=Apprentice()
# xiaoming.cook()
# xiaoming.Master_cook()
# xiaoming.School_cook()
# xiaoming.cook()


# class Sunflower:
#     def __init__(self):
#         self.HP=3
#     def shake(self):
#         print("向日葵摇晃～")
#     def outsun(self):
#         print("向日葵生产太阳")
#
# # 单向日葵
# class Singlesunflower(Sunflower):
#     def __init__(self):
#         self.power=25
#     def outsun(self):
#         print("向日葵生产一个阳光")
#
# # 双向日葵
# class Doublesunflower(Sunflower):
#     def __init__(self):
#         self.power=50
#     def outsun(self):
#         print("向日葵生产两个太阳")
# import time
# # 玩家
# class person(object):
#     def __init__(self):
#         self.power=0
#     def plant(self,sunflower,time1):
#         for i in range(time1):
#             self.power += sunflower.power
#             time.sleep(2)
#     def __str__(self):
#         return f"收集到的总能量为{self.power}"
#
# single=Singlesunflower()
# double=Doublesunflower()
# P1=person()
# # P1.plant(single,2)
# P1.plant(double,2)
# print(P1)


# class Test(object):
#     HP=100
#     # def __init__(self):
#     #     HP=100
#
# A=Test()
# A.HP=20
# B=Test()
# print(Test.HP)
# print(A.HP)
# print(B.HP)




# class Rifle:
#     # 定义弹药，给定弹药量30发
#     def __init__(self):
#         self.bullet=30
#         self.name="ak47"
#     # 更换弹夹
#     def change(self):
#         self.bullet += 30
#
#     # 开火次数
#     def open_file(self,a):
#         for i in range(a):
#             self.bullet -= 1
#             if self.bullet == 0:
#                 print("弹夹打空！")
#                 AK47.change()
#                 self.bullet += 30
#                 print("更换弹夹，子弹加满！")
#                 break
#         else:
#             print(f"开火{a}次")
#             print(f"剩余子弹{self.bullet}发")
#
#     # def __str__(self):
#
#
# class Soldier(Rifle):
#         HP=100
#
# xusanduo = Soldier()
# AK47=Rifle()
# xusanduo.open_file(28)
# xusanduo.open_file(2)

# ————————————————————————————————异常
# try:
#     f=open("test.txt","r",encoding="utf8")
# except Exception as r:
#     print(r)
#     f=open("test.txt","w",encoding="utf8")
#     f.write("test.txt文件不存在，新建test.txt")
# else:
#     print(f.read())
# finally:
#     # print(f.read())
#     f.close()

# class ShortInputError(Exception):
#     def __init__(self,length,min_len):
#         self.length=length
#         self.min_len=min_len
#
#     def __str__(self):
#         return f"你输入的长度是{self.length},不能少于{self.min_len}个字符"
#
# def main():
#     try:
#         con=input("请输入密码：")
#         if len(con)<3:
#             raise ShortInputError(len(con),3)
#     except Exception as r:
#         print(r)
#     else:
#         print("密码已经输入完成")
#
# main()



# print(os.listdir(r"c:"))
# print(len(os.listdir(r"c:")))
# print(os.path.isdir("c:\Intel"))
# ——————————————30题
# import os
# class Test(object):
#     def __init__(self):
#         self.a=0
#         self.b=0
#     def count1(self,path):
#         os.chdir(rf"{path}")
#         list1=os.listdir("./")
#         for i in list1:
#             if os.path.isdir(i):
#                 self.a+=1
#             elif os.path.isfile(i):
#                 self.b+=1
#     def __str__(self):
#         return f"目录的个数是{self.a},文件的个数是{self.b}"
#
# # print(os.listdir(r"D:\notepad++"))
# path1=Test()
# path1.count1("D:\python")
# print(path1)

# import os
# class Test(object):
#     def find(self):
#         a=input("输入路径：")
#         for i in os.listdir(rf"{a}"):
#             if i.endswith(".txt"):
#                 print(i)
#
# A=Test()
# A.find()


# import time as t
# t.sleep(2)
# from time import sleep as s
# s(2)
# from time import *
# sleep(2)
# print("上下上下 左右左右 B A B A")


# import xlrd
#
# import xlwt

# import test.module1,test.module2
# test.module1.testa()
# test.module2.testb()
# from test import module1,module2



































