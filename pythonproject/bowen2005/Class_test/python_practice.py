
# # <class 'int'>
# a=1
# # <class 'str'>
# b="1"
# # <class 'str'>
# c="1.1"
# # <class 'bool'>
# d=True
# # <class 'list'>
# e=["张三","李四","王五"]
# # <class 'tuple'>
# f=("张三","李四","王五")
# # <class 'set'>
# g={"张三","李四","王五"}
# # <class 'dict'>
# h={"name":"","age":"20","sex":"男"}
# print(a,b,c,d)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))


# name="张三"
# age=20
# print("我的名字叫%s" % name)
# print("我的年龄是%d" % age)
# print("我的名字叫{},我的年龄是{}".format(name,age))
# print(f"我的名字叫{name},我的年龄是{age}")

# name=input("请输入你的姓名")
# age=int(input("请输入你的年龄"))
# print(f"你的名字叫{name}，你的年龄是{age}岁")
# print(type(age))
# print(age)


# print("nihao😃",end = "\t" ),print("★☆→✖➗➕➖🚗🏠✈🚢🏢👽🍙🍚🍜🥟🐆🐅🦁😃😟😔😀")
#
# a="10"
# b=eval(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(type(eval(a)))
# print(f"{b+b}")


# a=2
# b=3
# c=4
# print(not(a<b and b<c))


# age=eval(input("请输入你的年龄:"))
# if age >= 18:
#     print(f"已成年，可以上网")
# else:
#     print(f"未成年，不可以上网")
#
# print("程序结束")


# # 0-15
# # 16-17
# # 18-55
# # 56-99
# if 0 <= age <= 15:
#     print("不聘请")
# if 16 <= age <= 17:
#     print("兼职")
# if 18 <= age <= 55:
#     print("全职")
# if 56 <= age <= 99:
#     print("不聘请")


# 0-59不及格
# 60-79及格
# 80-89良好
# 90-100优秀
# sco=float(input("请输入你的成绩:"))
# if 0 <= sco < 60:
#     print(f"你的成绩为{sco}分,成绩不及格")
# elif 60 <= sco < 80:
#     print(f"你的成绩为{sco}分,成绩及格")
# elif 80 <= sco < 90:
#     print(f"你的成绩为{sco}分,成绩良好")
# elif 90 <= sco <= 100:
#     print(f"你的成绩为{sco}分,成绩优秀")
# else:
#     print("无效的成绩,请输入有效的成绩！！")


# money=eval(input("请输入你的金额:"))
# if money >= 1:
#     print("可以上车")
#     seat=eval(input("空座位的个数:"))
#     if seat >= 1:
#         print("就座")
#     else:
#         print("站立")
# else:
#     print("不能上车")


# ticket=eval(input("检票进站:"))
# if ticket==1:
#     print("请过安检")
#     knife=eval(input("刀具长度是否大于10cm:"))
#     if knife > 10:
#         print("不可以上车")
#     else:
#         print("可以上车")
# else:
#     print("不能进站")


# number=int(input("请输入一个整数:"))
# #
# # if number % 2 == 0:
# #     if number % 3 == 0:
# #         print("既可以被2整除，也可以被3整除")
# #     else:
# #         print("可以被2整除，但不可以被3整除")
# # else:
# #     if number % 3 == 0:
# #         print("可以被3整除，但不可以被2整除")
# #     else:
# #         print("既不可以被2整除，也不可以被3整除")


# 判断三角形
# a=eval(input("请输入整数a的值:"))
# b=eval(input("请输入整数b的值:"))
# c=eval(input("请输入整数c的值:"))
# if a+b > c and a+c > b and b+c > a:
#     if a==b==c:
#         print("等边三角形")
#     elif a==b or a==c or b==c:
#         print("等腰三角形")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不是三角形")


# 猜拳（手动输入玩家出拳和电脑出拳）
# player=eval(input("玩家猜拳(0拳头,1剪刀,2布):"))
# computer=eval(input("电脑猜拳(0拳头,1剪刀,2布):"))
# if player==0:
#     if computer==0:
#         print("平局")
#     elif computer==1:
#         print("玩家赢")
#     elif computer==2:
#         print("电脑赢")
#     else:
#         print("请输入正确的代表数字")
# elif player==1:
#     if computer==0:
#         print("电脑赢")
#     elif computer==1:
#         print("平局")
#     elif computer==2:
#         print("玩家赢")
#     else:
#         print("请输入正确的代表数字")
# elif player==2:
#     if computer==0:
#         print("玩家赢")
#     elif computer==1:
#         print("电脑赢")
#     elif computer==2:
#         print("平局")
#     else:
#         print("请输入正确的代表数字")
# else:
#     print("请输入正确的代表数字")


# 猜拳（玩家猜拳键盘输入，电脑随机输出）
# import random
# random工具箱下的randint工具可以输出随机整数
# computer = random.randint(0,2)
# player=eval(input("玩家猜拳(0拳头,1剪刀,2布):"))
#
# if (player == 0 and computer == 1) \
#         or (player == 1 and computer == 2) \
#         or (player == 2 and computer == 0):
#     print("玩家赢")
# elif (player == 1 and computer == 0) \
#         or (player == 2 and computer == 1) \
#         or (player == 0 and computer == 2):
#     print("电脑赢")
# elif 0 <= player == computer <= 2:
#     print("平局")
# else:
#     print("请输入正确出拳的代表数字")


# 三目运算符！！！


# a=1
# while a <= 6:
#     print("咕咕咕")
#     a += 1


# a=1
# # b=0
# # while a <= 10:
# #     print(a)
# #     b = b+a
# #     a = a+1
# # print(b)


# 从一乘到十的结果：3628800
# a=1
# b=1
# while a<=10:
#     print(a)
#     b=b*a
#     a=a+1
# print(b)


# 一百以内偶数之和
# 2550
# a = 1
# b = 0
# while a <= 100:
#     if a % 2 == 0:
#         b = b+a
#     a=a+1
# print(b)



# 吃了第1个苹果
# 吃了第2个苹果
# 程序终止
# a=1
# while a <= 5:
#     if a == 3:
#         print("程序终止")
#         break
#     print(f"吃了第{a}个苹果")
#     a += 1


# 吃了第1个苹果
# 吃了第2个苹果
# 跳过此次程序
# 吃了第4个苹果
# 吃了第5个苹果
# 程序运行完成
# a=1
# while a <= 5:
#     if a==3:
#         a=a+1
#         print("跳过此次程序")
#         continue
#     print(f"吃了第{a}个苹果")
#     a=a+1
# print("程序运行完成")


# ★
# ★★
# ★★★
# ★★★★
# ★★★★★
# b=1
# while b <= 5:
#     a = 1
#     while a <= b:
#         print("★", end="")
#         a += 1
#     print()
#     b += 1


# 九九乘法表
# 1*1=1
# 1*2=2	2*2=4
# 1*3=3	2*3=6	3*3=9
# 1*4=4	2*4=8	3*4=12	4*4=16
# 1*5=5	2*5=10	3*5=15	4*5=20	5*5=25
# 1*6=6	2*6=12	3*6=18	4*6=24	5*6=30	6*6=36
# 1*7=7	2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49
# 1*8=8	2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64
# 1*9=9	2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81
# b=1
# while b <= 9:
#     a = 1
#     while a <= b:
#         print(f"{a}×{b}={a*b}", end="\t")
#         a += 1
#     print()
#     b += 1


#★‍	★‍	★‍	★‍	★‍	★‍	★‍	★‍	★‍
#★‍	★‍	★‍	★‍	★‍	★‍	★‍	★‍
#★‍	★‍	★‍	★‍	★‍	★‍	★‍
#★‍	★‍	★‍	★‍	★‍	★‍
#★‍	★‍	★‍	★‍	★‍
#★‍	★‍	★‍	★‍
#★‍	★‍	★‍
#★‍	★‍
#★‍
# b=9
# while b >= 1:
#     a=1
#     while a <= b:
#         print("★‍",end="\t")
#         a=a+1
#     print(end="\n")
#     b=b-1


#  ‍	 ‍	 ‍	 ‍	 ‍	 ‍	 ‍	 ‍	★
#  ‍	 ‍	 ‍	 ‍	 ‍	 ‍	 ‍	★	★
#  ‍	 ‍	 ‍	 ‍	 ‍	 ‍	★	★	★
#  ‍	 ‍	 ‍	 ‍	 ‍	★	★	★	★
#  ‍	 ‍	 ‍	 ‍	★	★	★	★	★
#  ‍	 ‍	 ‍	★	★	★	★	★	★
#  ‍	 ‍	★	★	★	★	★	★	★
#  ‍	★	★	★	★	★	★	★	★
#★	★	★	★	★	★	★	★	★
# b=9
# while b >= 1:
#     a=1
#     while a <= b-1:
#         print(" ‍",end="\t")
#         a=a+1
#     while b-1 < a <= 9:
#         print("★",end="\t")
#         a=a+1
#     print(end="\n")
#     b=b-1


# 水仙花数～～★
# 三位数，所以a直接1赋值100，从最小的三位数开始运算                           水仙花数～～★
# i = 100
# while i < 1000:
#     a = i // 100
#     b = (i - a * 100) // 10
#     c = i % 10
#     if a**3 + b**3 + c**3 == i:
#         print(i)
#     i += 1


# for循环做一到一百加法运算
# a = 0
# for i in range(1,101):
#     a += i
# print(a)


# 1到10阶乘
# range括号内范围不包括括号右边界值★
# a= 1
# for i in range(1,11):
#     a*=i
# print(a)



# for i in range(1,6):
#     if i==3:
#         print("程序终止")
#         break
#     print("对不起")
# else:
#     print("程序正常结束")

# for i in range(1,6):
#     if i==3:
#         print("跳过此次程序")
#         continue
#     print("对不起")
# else:
#     print("程序正常结束")


#  2 3 5 7 11 13 17
# 2到100质数之和
# a=0
# for i in range(2,101):
#     if i%2==0 or i%3==0 or i%5==0 or i%7==0:
#         if i==2 or i==3 or i==5 or i==7:
#             a = a+i
#             print(i)
#     else:
#         a = a+i
#         print(i)
# else:
#     print(a)



# 九九乘法表                                          九九乘法表★
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{i}×{j}={i*j}",end="\t")
#     print()


# 2到100质数之和                                        质数★★
# 质数：只能被一和自身整除的数
# r = 0
# for i in range(2,101):
#     for f in range(2,i):
#         if i % f == 0:
#             break
#     else:
#         r += i
# print(r)


# 完美数★                                      完美数★★
# 6 ：1 2 3
# 28 ：1 2 4 7 14
# 496 ：1 2 4 8 16 31 62 124 248
# a从一到一千集合内依次选择
# 寻求a的全部能被除尽的除数（余数全为零的除数）
# 将筛选出来的除数依次相加
# 判断除数相加是否等于a，相等则为完美数
# for a in range(1,1001):
#     b=0
#     for i in range(1,a):
#         if a % i==0:
#             b += i
#     if b==a:
#         print(a)


# for 循环写三角
#★
#★	★
#★	★	★
#★	★	★	★
#★	★	★	★	★
#★	★	★	★	★	★
#★	★	★	★	★	★	★
#★	★	★	★	★	★	★	★
#★	★	★	★	★	★	★	★	★

# for b in range(1,10):
#     for a in range(1,b+1):
#         if a <= b:
#             print("★",end="\t")
#     print(end="\n")
#
# # for 循环写三角
# for a in range(1,10):
#     for b in range(1,a):
#         print("★",end="\t")
#     print()



# for 循环写倒三角
#  	 	 	 	 	 	 	 	★
#  	 	 	 	 	 	 	★	★
#  	 	 	 	 	 	★	★	★
#  	 	 	 	 	★	★	★	★
#  	 	 	 	★	★	★	★	★
#  	 	 	★	★	★	★	★	★
#  	 	★	★	★	★	★	★	★
#  	★	★	★	★	★	★	★	★
#★	★	★	★	★	★	★	★	★
# b:9 8 7 6 5 4 3 2 1
# for b in range(9,0,-1):
#     for a in range(b,1,-1):
#         if a <= b:
#             print(" ",end="\t")
#     for c in range(1,11-b):
#         if c <= 11-b:
#             print("★",end="\t")
#     print(end="\n")

# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
# from turtle import *
# def curvemove():
#     for i in range(200):
#         right(1)
#         forward(1)
# color('red','pink')
# begin_fill()
# left(140)
# forward(111.65)
# curvemove()
# left(120)
# curvemove()
# forward(111.65)
# end_fill()
# done()


# 正三角
# - - - - - *
# - - - - * * +
# - - - * * * + +
# - - * * * * + + +
# - * * * * * + + + +
# * * * * * * + + + + +

# for a in range(6,0,-1):
#     for b in range(1,a):
#         print("-",end=" ")
#     for c in range(a,7):
#         print("*",end=" ")
#     for d in range(a,6):
#         print("+",end=" ")
#     print(end="\n")


# 倒三角
# - * * * * * + + + +
# - - * * * * + + +
# - - - * * * + +
# - - - - * * +
# - - - - - *

# for a in range(1,6):
#     for b in range(1,a+1):
#         print("-",end=" ")
#     for c in range(5,a-1,-1):
#         print("*",end=" ")
#     for d in range(5,a,-1):
#         print("+",end=" ")
#     print(end="\n")


# 菱形★
# for a in range(6,0,-1):
#     for b in range(1,a):
#         print(" ",end=" ")
#     for c in range(a,7):
#         print("*",end=" ")
#     for d in range(a,6):
#         print("+",end=" ")
#     print(end="\n")
# for a in range(1,6):
#     for b in range(1,a+1):
#         print(" ",end=" ")
#     for c in range(5,a-1,-1):
#         print("+",end=" ")
#     for d in range(5,a,-1):
#         print("*",end=" ")
#     print(end="\n")


# for i in range(1,7):
# #     for j in range(1,7):
# #         if j<7-i:
# #             print('',end='  ')
# #         else:
# #
# #             print('*',end=' ')
# #     for k in range(1,7):
# #         if k < i:
# #             print('*',end=' ')
# #     print()


# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a == b or a == c or b == c:
#                 continue
#             else:
#                 print(f"{a}{b}{c}")


# a=8
# for i in range(1,4):
#     num = int(input("猜数字(请输入10以内数字)："))
#     if num > a:
#         print("猜的数大了")
#     elif num < a:
#         print("猜的数小了")
#     else:
#         print("恭喜你，猜对了！")
#         break
# else:
#     print("你失败了，菜鸟😛")

# a = 8
# b=1
# while b <= 3:
#     c=int(input("猜数字(请输入10以内数字)："))
#     if c < a:
#         print("猜小了")
#     elif c > a:
#         print("猜大了")
#     elif c == a:
#         print("猜对了")
#     b += 1
# else:
#     print("结束")




# 从一加到一百
# a=1
# b=0
# while a <= 100:
#     b = b+a
#     a = a+1
# print(b)


# a = 0
# for b in range(1,101):
#     if b % 5 == 0:
#        a = a+b
# print(a)

# 格式化输出三种方式
# a=0.120
# b=0.13000
# print("%.2f,%.3f"%(a,b))
# print(f"{a:.2f},{b:.3f}")
# print("{},{}".format(a,b))


# 因数之和
# a=int(input("请输入整数："))
# c=0
# for b in range(1,a+1):
#     if a%b == 0:
#         c=c+b
# print(c)



# 阶乘
# 6的阶乘：1×2×3×4×5×6
# a =int(input("请输入整数："))
# c = 1
# for b in range(1,a+1):
#     if b <= a:
#         c *= b
# print(f"{a}的阶乘为：{c}")


# 阶乘之和
# d=0
# for a in range(1,6):
#     c=1
#     for b in range(1,a+1):
#         if b<=a:
#             c=c*b
#     d=d+c
# print(d)

# d=0
# c=1
# for a in range(1,6):
#     c=c*a
#     d=d+c
# print(d)

# b = 1
# c = 0
# for a in range(1,6):
#     b *= a
#     c += b
# print(c)




# 引号特点
# 1.可以混用
# 2.三单和三双既可以当注释，也可以当字符串，还可以保留原有的格式
# a='123'
# print(type(a))
# a="123"
# print(type(a))
# a='''123'''
# print(type(a))
# a="""123"""
# print(type(a))
# a="12"\
#     "34"
# print(a)
# # 三引号保留原有的格式
# a='''12
# 34'''
# print(a)

# a=[1,2,3]
# print(type(a))
# b=str(a)
# print(type(b))


# 字符串(不可变)
# 字符串(有序)
# 字符串(支持索引)
# 可变：程序运行时，内容发生改变，内存位置不发生改变
# 不可变：程序运行时，内容发生改变，内存位置发生改变
# 有序：程序运行的时候，输入与输出的顺序是相同的
# 无序：程序运行的时候，输入与输出的顺序是不相同的
# id(数据)：可以查看数据的内存位置

# # 有序
# print("123")
# # 无序
# print({3,2,1})

# 默认从0开始
# a="qwer"
# print(a[0],a[1])
# print(a[-2],a[-1])


# b=0
# for a in range(1,11):
#     b+=a
# print(b)
# print(a)


# a=1
# b=0
# while a <= 10:
#     # b=0+1=1 b=1+2=3
#     b+=a
#     # a=a+1=2 a
#     a+=1
# print(b)
# print(a)

# a=1
# for b in range(1,11):
#     a*=b
# print(a)

# name="zhangsan"
# print(name[0:5:1])
# print(name[:])
# print(name[:9])
# print(name[::2])
# print(name[:-1])
# print(name[::-1])
# print(name[-3:-1])
# print(name.find("a"))
# print(name.index("s",1,5))
# print(name.rindex())
# print(name)
# print(id(na
# name = "1 2 3 2 4 5 6 2 7 8"
# print(name.split(" "))

# name="hao are you  hao old are you"
# print(name.startswith("hao",10,15))
# print(name.endswith("ou"))

# a1="asdfghj"
# print(a1.isalpha())
# a2="asdf123"
# print(a2.isalpha())

# b1="12345678"
# print(b1.isdigit())
# b2="123456ytr"
# print(b2.isdigit())

# c1="234werrew"
# print(c1.isalnum())
# c2="sdfgh1234@#$%^"
# print(c2.isalnum())

# d1="   "
# # print(d1.isspace())
# # d2="sdf  "
# # print(d2.isspace())

# —————————————————判断字符串内有多少字母，数字，空格和特殊字符
# b=0
# c=0
# d=0
# e=0
# name=str(input("请输入任意字符串："))
# for a in name:
#     if a.isalpha():
#         b+=1
#     elif a.isdigit():
#         c+=1
#     elif a.isspace():
#         d+=1
#     else:
#         e+=1
# print(f"字母的个数是：{b}")
# print(f"数字的个数是：{c}")
# print(f"空格的个数是：{d}")
# print(f"特殊符号的个数是：{e}")

# list1=["张三","李四","王五","张三"]
# print(list1)
# list2=["赵六","小二"]
# for i in list1:
#     print(i)
# print(list1.index("李四"))
# list1.append(list2)
# print(list1)
# print(list1[3][0])
# list1.extend(list2)
# print(list1)
# print(list1[3])
# del list1[1]
# list1.clear()
# print(list1)
# list1.insert(0,"八百")
# print(list1)
# print(list1)
# list1.pop()
# print(list1)
# list1.pop()
# print(list1)
# list1.pop(2)
# list1.remove()
# print(list1)
# list1=[7,34,6,9,21,5,18]
# list1.sort(reverse=True)
# print(list1)


# list1=["关羽","张飞","赵云","马超","黄忠"]
# import random
# # i=random.randint(0,4)
# # a=int(input(""))
# while True:
#     a=int(input("请输入点名的次数："))
#     for b in range(a):
#         list1=["关羽","张飞","赵云","马超","黄忠"]
#         print(list1[random.randint(0,3)])


# 排序法排序
# list1=[16,65,28,90,34,5,14]
# for a in range(len(list1)):
#     for b in range(len(list1)):
#         if list1[a]<list1[b]:
#             list1[a],list1[b]=list1[b],list1[a]
# print(list1)


# 冒泡法排序
# list1=[16,65,28,90,34,5,14]
# for a in range(len(list1)):
#     for b in range(len(list1)-1):
#         if list1[b]>list1[b+1]:
#             list1[b],list1[b+1]=list1[b+1],list1[b]
# print(list1)


# set1={20,10,30,30,10,40}
# print(set1)
# set1.add(50)
# print(set1)
# set1.update([100,200])
# print(set1)
# set1.update("abc")
# print(set1)
# set1.remove(80)
# print(set1)
# set1.discard(80)
# print(set1)
# set1.pop()
# set1.pop()
# print(set1)
# print(10 in set1)

# dict1={"name":"李四","sex":"男","age":"20"}
# print(dict1)
# dict1["birthday"]="1996-09-08"
# print(dict1)
# del dict1["birthday"]
# print(dict1)
# dict1["name"]="张三"
# print(dict1)
# dict1.clear()
# print(dict1)
# print(dict1.keys())
# for i in dict1.keys():
#     print(i)
# print(dict1.values())
# for j in dict1.values():
#     print(j)
# print(dict1.items())
# for k in dict1.items():
#     print(k)
# dict1={"name":"李四","sex":"男","age":"20"}
# dict1["telephone"]="12342364178"
# print(dict1)
# del dict1["telephone"]
# print(dict1)
# dict1["name1"]="张三"
# print(dict1)
# dict1["name"]="王五"
# print(dict1)


# 100块钱100只鸡
# 小鸡价钱为一块钱三只
# 母鸡为三块钱一只
# 公鸡为五块钱一只

# for a in range(0,21):
#     for b in range(0,34):
#         for c in range(0,101):
#             if a*5 + b*3 + c*1/3 == 100 and a + b+ c==100:
#                 print(f"公鸡个数{a}，母鸡个数{b}，小鸡个数{c}")

# ——————————————————————字典增删改查
# 字典的特点：
# 括号为大括号
# 数据为键值对形式出现
# 各个键值对之间用逗号隔开
# 字典是可变的，有序的（依靠键值对查找）
# dict1={"name":"张三
# ","age":"20","sex":"男"}
# print(dict1)
# dict1["birthday"]="1998-06-04"
# print(dict1)
# del dict1["birthday"]
# print(dict1)
# dict1["name"]="李四"
# print(dict1)
# print(dict1["name"])
# 打印字典中所有的键
# print(dict1.keys())
# for key in dict1.keys():
#     print(key)
# # 打印字典中所有的值
# print(dict1.values())
# for value in dict1.values():
#     print(value)
# # 打印字典中所有的元素
# for item in dict1.items():
#     print(item)
# # 打印字典中所有的键值对
# print(dict1.items())
# for key,value in dict1.items():
#     print(f"{key}:{value}")

# 集合常见操作
# 符号为大括号
# 数据用逗号隔开
# 集合特点：
# 集合可以去掉重复数据
# 集合数据是无序的，故不支持下标
# set1={10,3,6,2,9,3,4}
# print(set1)
# # 增加数据
# set1.add(20)
# print(set1)
# # 追加数据
# set1.update([1,34,25])
# print(set1)
# # 删除数据
# set1.remove(10)
# print(set1)
# set1.discard(100)
# print(set1.pop())
# ————————————————————去除重复
# a=[11,22,11,22,33,22,22,22,22,44]
# for b in a:
#     if a.count(b)>1:
#         for c in range(a.count(b)-1):
#             a.remove(b)
# print(a)

# a=[11,33,11,44,44,33,22,22]
# b=[]
# [b.append(i) for i in a if not i in b]
# print(b)




# ————————————————————冒泡法排序
# a=[16,65,28,90,34,5,14]
# for x in range(len(a)):
#     for y in range(len(a)-1):
#         if a[y]>a[y+1]:
#             a[y],a[y+1]=a[y+1],a[y]
# print(a)

# ————————————————————筛选第一大和第二大的数值
# a=[11,22,33,33,44,44,77,77,88,88]
# # for i in range(a.count(max(a))):
# #     print(max(a))
# #     a.remove(max(a))
# # for j in range(a.count(max(a))):
# #     print(max(a))

# list1=[1,1,2,3,3,2,2,3,1]
# list1.sort(reverse=True)
# print(list1)
# for i in list1:
#     if i == list1[0]:
#         print(i,end="\t")
#     num = list1.count(list1[0])
#     if i == list1[num]:
#         print(i)

# print(a.count(max(a)))
# str1="bo"
# str2="wen"
# print(str1+str2)
# list1=[1,2,3]
# list2=[4,5,6]
# print(list1+list2)
# print("*"*5)
# print(list1*3)
# tuple1=(10,20,30)
# print(10 in tuple1)
# print((22 in tuple1))
# dict1={"name":"lisi","age":20}
# print("age" in dict1)
# list1=[10,20,30,40]
# for a,b in enumerate(list1,start=2):
#     print(a)
# print(min(list1))
# del list1[0]
# print(list1)

# list1=[30,20,10,0]
# int1=int(input("输入数值："))
# list1.append(int1)
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# for i in range(len(list1)):
#     if list1[i] >= int1 >= list1[i+1]:
#         list1.insert(i+1,int1)
#         break
#     elif int1 > max(list1):
#         list1.insert(0,int1)
#         break
#     elif int1 < min(list1)

# ——————————————————————推导式练习
# list1=[i for i in range(0,10)]
# print(list1)
# list2=[i for i in range(2,10,2)]
# print(list2)
# list3=[i for i in range(0,10) if i % 2 == 0]
# print(list3)
# list4=[(i,j) for i in range(3) for j in range(3) ]
# print(list4)
# list1=["name","age","sex"]
# list2=["lisi",20,"man"]
# dict1={list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
# list3=[1,2,3,4]
# list4=[5,6,7,8]
# set1={i**2 for i in list4}
# print(set1)

# ————————————————————回文
# str1=str(input("输入字符串："))
# for a in range(len(str1)):
#     if str1[a]!=str1[len(str1)-1]:
#         break
#     else:
#         print(str1)


# def service():
#     print("转账明细")
#     print("更改密码")
#     print("存款")
#     print("取款")
#
# service()
# print("——————————————")
# print("转账成功，跳转选择服务项目页面")
# print("——————————————")
# service()
# print("——————————————")
# service()
# def add(a):
#     "这个函数是用来求阶乘之和的"
#     b=1
#     c=0
#     for i in range(1,a+1):
#         b=b*i
#         c=b+c
#     print(f"{a} 的阶乘之和为：{c}")
# add(int(input("输入数字：")))
# print(help(add))

# def dog():
#     print("-"*20)
# def cat(num):
#     for i in range(num):
#         print(dog())
# cat(int(input("输入数字：")))

# ————————————————列表左移一位
# list1=[1,2,3,4,5]
# for i in range(len(list1)-1):
#     list1[i],list1[i-1]=list1[i-1],list1[i]
# print(list1)
# ————————————————左移n位
# A=[1,2,3,4,5]
# a=int(input("请输入移动的位数："))
# for i in range(a):
#         b = A.pop(0)
#         A.append(b)
# print(A)
# 带if的列表推导式
# list1=[i for i in range(10) if i % 2 == 0]
# print(list1)
# 创建字典
# dict1={i:i**2 for i in range(4)}
# print(dict1)
# 将两个列表合并为一个字典
# list1=["name","age","sex"]
# list2=["lisi",20,"man"]
# dict1={list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
# list1=[1,1,2]
# set1={i**2 for i in list1}
# print(set1)
# list1=[1,2,3]
# print(id(list1))
# list1.append(4)
# print(id(list1))
# tuple1=(1,"we",2,(12,39))
# print(tuple1)


# def testa():
#     return 50
#
# def testb(num):
#     return 1,2
#
# result=testa()
# testb(result)
# print(testb(result))
# 位置参数，关键字参数，默认参数：
# def testA(name,age,sex):
#     print(f"他名字叫{name},年龄是{age}岁,性别{sex}")
# def testB(name,age,sex="女"):
#     print(f"他名字叫{name},年龄是{age}岁,性别{sex}")
#
# testA("李四",20,"男")
# testA(name="李四",age=20,sex="男")
# testA(sex="男",name="李四",age=20)
# testA("李四",age=20,sex="男")
# testB("张三",18)
# 可变参数：包裹位置参数，包裹关键字参数
# def testA(*args):
#     name,age,sex=args
#     print(f"名字叫{args[0]},年龄{args[1]}岁,性别{args[2]}")
#     print(f"名字叫{name},年龄{age}岁,性别{sex}")
# testA("李四",20,"男")
# def testB(**kwargs):
#     name,age,sex=kwargs
#     print(f"名字叫{kwargs['name']},年龄{kwargs['age']}岁,性别{kwargs['sex']}")
# testB(name="李四",age=20,sex="男")

# dict1={'id':'10','name':'Tom','sex':'man'}
# print(dict1['id'])
# if dict1['id']=='10':
#     print(1)
# ——————————————————————————lambda
# def fn1():
#     return 200
# print(fn1)
# print(fn1())
#
# fn2=lambda :100
# print(fn2)
# print(fn2())

# test1=lambda : 300
# print(test1)
# print(test1())

# def add(a,b):
#     c=a+b
#     return c
# d = add(1,2)
# print(d)
# d=lambda a,b:a*b
# print(d(3,4))
# print((lambda a,b:a+b)(10,2))
# print((lambda a,b,c=10:a+b+c)(100,90))
# print((lambda *args:args)(10,20,30,40))
# print((lambda **kwargs:kwargs)(name="lisi",age=20,sex="男"))
# print((lambda *args:args)(10,20,30))
# print(a)
# ————————————————————————map
# a=[2,4,6,8,10]
# def testA(x):
#     return x**2
# c=map(testA,a)
# print(c)
# # 迭代器
# print(list(c))
# print(list(c))

# str1="abacddefff"
# set1=set()
# for i in range(len(str1)-1):
#     if str1[i] == str1[i+1]:
#         set1.add(str1[i])
# print(set1)

# str1="abb acd def ff"
# str2=str1.replace(" ","")
# print(str2)
# set1={str2[i] for i in range(len(str2)-1) if str2[i]==str2[i+1]}
# print(set1)

# result=lambda x:x*x
# print(result(5))


# def A(x):
#     if x==1:
#         return 1
#     else:
#         return x+A(x-1)
#
# print(A(4))

# f=open("a.txt","r")
# print(f.read())
# f=open("a.txt","r")
# print(f.readlines())
# f=open("a.txt","r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# 文件基本操作————————————读与写
# f=open("a.txt","w",encoding="utf8")
# f.write("博文，你好！A B C D E F G")
# f.close()
# f=open("a.txt","r",encoding="utf8")
# print(f.read())
# f.close
# f=open("a.txt","a",encoding="utf8")
# f.write("\n世界，你好！H I G K L M N")
# f.close()
# f=open(r"C:\Users\Admin\Desktop\test.txt","r",encoding="utf8")
# print(f.read())
# f.close()

# ————————————将a.txt文件的内容添加到c.txt文件中
# ff=open("a.txt","r",encoding="utf8")
# f=open("c.txt","w",encoding="utf8")
# f.write(ff.read())
# ff.close()
# f.close()

# ————————————复制图片文件
# with open("01.jpg","rb") as f:
#     with open("a.jpg","wb") as ff:
#         ff.write(f.read())

# ——————————————————seek重新定位指针
# with open("a.txt","w+",encoding="utf8") as f:
#     f.write("博文，你好！")
#     # f.seek能够将指针放至文档开头，以便f.read能够读取
#     f.seek(0,0)
#     print(f.read())

# lambda表达式——————————————又称匿名函数
# def test():
#     return 10
# print(test())
# print((lambda :20)())
# print((lambda a:a)(30))
# print((lambda a,b:a+b)(10,30))
# print((lambda a,b,c=10:a+b+c)(10,30))
# print((lambda *args:args)(10,20,30))
# print((lambda **kwargs:kwargs)(name="lisi",age=20))
# print((lambda a,b:a if a > b else b)(59,60))

# f=open("a.txt","w",encoding="utf8")
# f.write("你好，博文！ \n你好，世界！")
# f.close()
# f=open("a.txt","r",encoding="utf8")
# print(f.read())
# f.close()
# f=open("a.txt","w+",encoding="utf8")
# f.write("你好，新世界！")
# f.seek(0,0)
# print(f.read())

# ——————————————————将test1文件内的大写转小写
# with open(r"C:\Users\Admin\Desktop\test1.txt","r") as f:
#     with open(r"C:\Users\Admin\Desktop\test1.txt", "r+") as ff:
#         ff.write(f.read().upper())
#         ff.seek(0,0)
#         print(ff.read())
# ——————————————————(2)
# with open(r"C:\Users\Admin\Desktop\test1.txt","r+") as f:
#     b=f.read()
#     b.upper()
#     f.seek(0,0)
#     f.write(b)
#     print(f.read())
# ————————一个函数，传两个参数a,b，a是数组，b是一个数字，
# ————————找出a数组中两数之和等于b，打印出来这两个数20.
# def test(a,b):
#     for i in range(len(a)-1):
#         if a[i]+a[i+1]==b:
#             print(a[i],a[i+1])
# test([1,4,10,2,3,0,5,7,8,9],5)
# def test(a):
#     for i in a.values():
#         if len(i) > 2:
#             i[:2]
#
# test({"name":"lisi","age":"二十岁"})

# a={"a":"b","c":"d"}
# for i in a:
#     print(i)
# 写一个函数，检查传入的字典的每一个值的长度，如果长度大于2，
# 则保留该值的前两位的字符，如果不大于2，则不做任何改变
# def a(dict1):
#     for i in dict1:
#         a=dict1[i]
#         if len(a)>2:
#             dict1[i]=a[:2]
#     print(dict1)
# a({'name':'zhangsan','age':'180'})


# def testa():
#     print(123)
# def testb():
#     print(456)
#
# print(__name__)
# if __name__=="__main__":
#     testa()
#     testb()

# ————————————————正则表达式
# import re
# str1 = "abcdea"
# a = re.findall("b.*d",str1)
#
# print(a)
# str1 = "abcdea"
# b = re.findall("a(.*)a",str1)
# print(b)
#
# str1 = "abc\ndea"
# # re.S作用：当字符串中有换行符，也可以进行匹配
# c = re.findall("a(.*)a",str1,re.S)
# print(c)
#
# str1 = "abcdeA"
# # re.I作用：不区分大小写匹配字符串内容
# d = re.findall("a(.*)a",str1,re.I)
# print(d)
#
# # ————————非贪婪匹配
# str1 = "abcdeAadcba"
# e = re.findall("a(.*)a",str1,re.I)
# print(e)

# a = ['bcd']
# b = ['bcde']
# c = ['bc\nde']
# d = ['bcde']
# e = ['bcdeAadcb']

# import time
# print(time.mktime(time.localtime()))

#
# # ——————————————————————爬取图片
# import re
# import requests
# import xlwt
# import os
#
# url = 'https://movie.douban.com/top250?start=0&filter='
# head = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
# }
# r = requests.get(url, headers=head)
# a = r.content.decode('utf-8')
# b=re.findall('<img width="100" alt=(.*?)</a>',a,re.S)
# list1=[]
# for i in b:
#     c=(i.strip().replace('class="">','').replace('src=','').replace('"',''))
#     list2=c.split(' ')
#     d=list2[0]
#     e=list2[1]
#     list1.append((d,e))
#     print(c)
# for k in list1:
#     # 网址循环遍历
#     res=requests.get(k[1])
#     # print(k[1])
#     # 字节类型的二进制
#     htt = res.content
#     # 保存图片
#     f = open(fr'D:\PythonProject\bowen2005\pictures\{k[0]}.jpg','wb')
#     f.write(htt)
#     f.close()





























































