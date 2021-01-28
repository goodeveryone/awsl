#
# # paramiko模块：基于SSH用于连接远程服务器的模式
# import paramiko
#
# # 创建一个远程客户端
# ssh1 = paramiko.SSHClient()
# # 跳过验证  不用到know_hosts文件中去解析 (类似于域名解析的hosts文件，该文件存放可以连接的主机地址，
# # 第一次连接新的主机这个文件中是没有记录的，所以会导致连不上主机)
# ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh1.connect(
#     hostname="192.168.2.163",
#     port=22,
#     username="root",
#     password="111111"
# )
# # 命令不支持简写(ll不行，ls-a可以)，
# a,b,c= ssh1.exec_command("cd /opt && ls -l")
# print(b.read().decode())
# ssh1.close()
#
#
# # ssh1=paramiko.Transport(("192.168.2.163"))
# # ssh1.connect(username="root",password="111111")
# # sftp=paramiko.SFTPClient.from_transport(ssh1)
#
# # sftp.get("/opt/a.txt","a.txt")
# # sftp.put("a.txt","/opt/aaaaa.txt")
#
#
#
# import csv
# with open("aa.csv","r") as f:
    # r = csv.reader(f)
    # # 跳过第一行，一般用来跳过表头
    # t = next(r)
    # for i in r:
    #     print(i)

# with open("aa.csv", "r") as f:
#     r = csv.DictReader(f)
#     for i in r:
#         print(i["name"])


# h = ['id','name']
# v = [
#     ("1001","张三"),
#     ("1002","张四"),
#     ("1003","张五"),
#     ("1004","张六"),
#     ("1005","张七"),
#     ("1006","张八")
# ]
# with open("aaa.csv", "w",encoding="utf-8",newline='') as f:
#     w = csv.writer(f)
#     w.writerow(h)
#     w.writerows(v)






a="1.1"
b=float(a)
print(b)









