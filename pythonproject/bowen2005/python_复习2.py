# 复习-复习-复习-复习-复习——11.1
# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}×{j}={i*j}",end="\t")
#     print()

# for i in range(9):
#     for j in range(i+1):
#         print(f"{i+1}×{j+1}={(i+1)*(j+1)}",end="\t")
#     print()

# 水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i%100//10
#     c=i%10
#     if a**3+b**3+c**3 == i:
#         print(i)

# for i in range(100,1000):
#     if (i//100)**3+(i%100//10)**3+(i%10)**3 == i:
#         print(i)

# 质数
# for i in range(2,10):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 一到四列出不同组合的数
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=c and b!=c and a!=b:
#                 print(f"{a}{b}{c}")

# 倒序列表
# list1=[1,2,3,4,5]
# list2=list1[::-1]
# print(list2)

# 冒泡法排序
# list1=[2,4,1,3,5]
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)

# 选择法排序
# list1=[2,4,3,5,1]
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)

# 查看输入字符串有多少字母，数字，空格，特殊字符
# a=0
# b=0
# c=0
# d=0
# str1=str(input("请输入字符串："))
# for i in str1:
#     # 如果字符串中只包含字母则返回True，否则返回False
#     if i.isalpha():
#         a=a+1
#     # 如果字符串中只包含数字则返回True，否则返回False
#     elif i.isdigit():
#         b=b+1
#     # 如果字符串中只包含空格则返回True，否则返回False
#     elif i.isspace():
#         c=c+1
#     else:
#         d=d+1
# print(f"输入字符串中包含{a}个字母，{b}个数字，{c}个空格，{d}个特殊字符")








list1 = []
for i in range(100):
    if i % 7 == 0:
        print i
        list1.append(i)
    if i // 7 == 0:
        print i
        list1.append(i)
print(list1)








