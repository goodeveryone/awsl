# from time import sleep
# sleep(3)
# print("asdda")


list1 = []
for i in range(100):
    if i % 7 == 0:
        print i
        list1.append(i)
    if i // 7 == 0:
        print i
        list1.append(i)
print(list1)
