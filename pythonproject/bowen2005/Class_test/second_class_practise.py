# ————————————————————九九乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(f"{b}×{a}={a*b}",end="\t")
#     print()


# ————————————————————质数之和
# c=0
# for a in range(2,101):
#     for b in range(2,a):
#         if a % b == 0:
#             break
#     else:
#         # c += a
#         print(a)
# # print(c)


# ————————————————————水仙花数
# for i in range(100,1000):
#     a = i // 100
#     b = (i-a*100) // 10
#     c = i % 10
#     if a**3+b**3+c**3==i:
#         print(i)
# ————————————————————水仙花数2
# for i in range(100,1000):
#     if (i//100)**3+((i//10)%10)**3+(i%10)**3==i:
#         print(i)
# for i in range(1000,10000):
#     if (i//1000)**4+((i//100)%10)**4+((i//10)%10)**4+(i%10)**4==i:
#         print(i)
# for i in range(10000,100000):
#     if (i//10000)**5+((i//1000)%10)**5+((i//100)%10)**5+((i//10)%10)**5+(i%10)**5==i:
#         print(i)


# ————————————————————1到4组合出不重复的数
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and a!=c:
#                 print(f"{a}{b}{c}")


# ————————————————————10的阶乘
# a=1
# b=0
# for c in range(1,11):
#     a=a*c
#     b=b+a
# print(b)


# ————————————————————1到100偶数累加和
# b=0
# for a in range(1,101):
#     if a%2 == 0:
#         b += a
# print(b)


# ————————————————————判断三角形
# a=eval(input("请输入三角形a边的值："))
# b=eval(input("请输入三角形b边的值："))
# c=eval(input("请输入三角形c边的值："))
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print("等边三角形")
#     elif a==b or b==c or a==c:
#         print("等腰三角形")
#     elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")


# —————————————————————判断字符串内有多少字母，数字，空格和特殊字符
# b=0
# c=0
# d=0
# e=0
# str1=str(input("请输入任意字符串："))
# for a in str1:
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


# ———————————————————————选择法排序
# list1=[15,77,3,21]
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[j]>list1[i]:
#             list1[j],list1[i]=list1[i],list1[j]
# print(list1)
# ————————————————————————冒泡法排序
# list1=[15,77,3,21]
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)


# ————————————————————回文
# str1=str(input("输入字符串："))
# for a in range(len(str1)):
#     if str1[a]!=str1[len(str1)-a-1]:
#         print("不是回文")
#         break
# else:
#     print("是回文")


# ————————————————————倒序列表
# list1=[1,2,3,4,5,6]
# list2=list1[::-1]
# print(list2)



# ——————————————————（1）将test1文件内的大写转小写
# with open(r"C:\Users\Admin\Desktop\test1.txt","r") as f:
#     with open(r"C:\Users\Admin\Desktop\test1.txt", "r+") as ff:
#         ff.write(f.read().upper())
#         ff.seek(0,0)
#         print(ff.read())
# ——————————————————(2)将test1文件内的大写转小写
# with open(r"C:\Users\Admin\Desktop\test1.txt","r+") as f:
#     b=f.read()
#     b.upper()
#     f.seek(0,0)
#     f.write(b)
#     print(f.read())


# 实心菱形
# for y in range(4,-5,-1):
#     for x in range(-4,5):
#         if abs(x)+abs(y)<=4:
#             print('*',end =' ')
#         else:
#             print(' ',end =' ')
#     print()


# 九九乘法表
# for i in range(1,10):
# #     for j in range(1,i+1):
# #         print(f"{j}×{i}={i*j}",end="\t")
# #     print()
# ————————————————————————冒泡法排序
# list1=[15,77,3,21]
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)

# 冒泡法排序
list1=[12,34,6,77]
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)




























