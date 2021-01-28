# 定义一个列表，这个列表为全局变量
info = [{'id':'10','name':'Tom','sex':'man'},{'id':'9','name':'李华','sex':'女'}]

def print_info():
    """显示界面"""
    print("-"*20)
    print("欢迎登陆学员管理系统")
    print("1：添加学员")
    print("2：删除学员")
    print("3：修改学员信息")
    print("4：查询学员信息")
    print("5：显示所有学员信息")
    print("6：退出系统")
    print("-"*20)

def add_info():
    """添加学员"""
    id = input("请输入学号：")
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    # 将添加过数据的列表定义为全局变量
    global info
    for i in info:
        if i['id'] == id:
            print("该用户已存在")
            return
    dict1 = {}
    dict1['id'] = id
    dict1['name'] = name
    dict1['sex'] = sex
    info.append(dict1)
    print(info)

def del_info():
    """删除学员"""
    del_id = input("请输入要删除的学员学号：")
    for a in info:
        if a.get('id')==del_id:
            answer = input("确定要删除么？yes or no：")
            if answer == "y":
                info.remove(a)
                print(info)
                break
    else:
        print("输入学员信息不存在，请重新输入")

def modife_info():
    """修改学员信息"""
    modife_id=input("请输入你要修改的学员学号：")
    for i in info:
        if i['id']==modife_id:
            print(i)
            i['id']=input("请输入新学号：")
            i['name']=input("请输入新名字：")
            i['sex']=input("请输入性别：")
            print(i)
            print(info)
            break
    else:
        print("输入学员信息不存在，请重新输入")
        modife_info()

def search_info():
    """查询学员信息"""
    search_id=input("请输入学员学号：")
    for i in info:
        if i['id']==search_id:
            print(i)
            break
    else:
        print("该学员信息不存在，请重新输入")

def print_all():
    """显示所有学员信息"""
    print("学号\t\t姓名\t\t性别")
    for i in info:
        print(f"{i['id']}\t\t{i['name']}\t\t{i['sex']}")

while True:
    print_info()
    user_num = input("请选择您需要的功能序号：")
    if user_num == '1':
        print("添加学员")
        add_info()
    elif user_num == '2':
        print("删除学员")
        del_info()
    elif user_num == '3':
        print("修改学员信息")
        modife_info()
    elif user_num == '4':
        print("查询学员信息")
        search_info()
    elif user_num == '5':
        print("显示所有学员信息")
        print_all()
    elif user_num == '6':
        print("退出系统")
        break
    else:
        print("请输入正确的选择序号！")



