# # 创建学生类
class Student(object):
    def __init__(self, name, id, age):
        self.s_name = name
        self.s_id = id
        self.s_age = age

    def __str__(self):
        return f"{self.s_name}, {self.s_id}, {self.s_age}"


# 创建管理类
class StudentManger:
    def __init__(self):
        # 定义一个列表，用来存储学生对象
        self.student_info = []
    # 定义成静态方法，节省资源
    @staticmethod
    def print_info():
        print("-" * 30)
        print("欢迎登陆学员管理系统！")
        print("1 添加学员")
        print("2 删除学员")
        print("3 修改学员信息")
        print("4 查询学员信息")
        print("5 显示所有学员信息")
        print("6 退出系统")
        print("-" * 30)

    # 读取文件中的数据
    def read_info(self):
        with open("student.txt", 'r', encoding="utf8") as f:
            for i in eval(f.read()):
                # 将文件中读取到的字典，转换为对象，存入到列表中
                S1 = Student(i["s_name"], i["s_id"], i["s_age"])
                self.student_info.append(S1)
            print(self.student_info)

    # 新增学员
    def add_info(self):
        stu_id = input("请输入学号：")
        # 依次取出学生对象，
        # 通多对象.属性取出所有已存在的学生的学号
        for i in self.student_info:
            if stu_id == i.s_id:
                print("该学员已存在！")
                break
        else:
            stu_name = input("请输入姓名：")
            stu_age = input("请输入年龄：")
            # 创建一个学生对象
            S1 = Student(stu_name, stu_id, stu_age)
            # 将学生对象追加到列表中
            self.student_info.append(S1)
            print(self.student_info)

    # 删除学员
    def del_info(self):
        stu_id = input("请输入学号：")
        # 依次取出学生对象，
        # 通多对象.属性取出所有已存在的学生的学号
        for i in self.student_info:
            if stu_id == i.s_id:
                self.student_info.remove(i)
                break
        else:
            print("该学生信息不存在")

    # 修改学员信息
    def modify_info(self):
        stu_id = input("请输入学号：")
        # 依次取出学生对象，
        # 通多对象.属性取出所有已存在的学生的学号
        for i in self.student_info:
            if stu_id == i.s_id:
                i.s_id = input("请输入新的学号：")
                i.s_name = input("请输入新的姓名：")
                i.s_age = input("请输入新的年龄：")
                break
        else:
            print("该学生信息不存在")

    # 查询单个学员信息
    def search_info(self):
        stu_id = input("请输入学号：")
        # 依次取出学生对象，
        # 通多对象.属性取出所有已存在的学生的学号
        for i in self.student_info:
            if stu_id == i.s_id:
                print(f"学生的学号是{i.s_id}，"
                      f"姓名叫{i.s_name}，"
                      f"年龄是{i.s_age}岁！")
                break
        else:
            print("该学生信息不存在")

    # 查询所有学员信息
    def all_info(self):
        print("学号\t\t姓名\t\t年龄")
        for i in self.student_info:
            print(f'{i.s_id}\t\t{i.s_name}\t\t{i.s_age}')

    # 保存学员信息到文件中
    def save_info(self):
        with open('student.txt', 'w', encoding="utf8") as f:
            list1 = []
            for i in self.student_info:
                # 将对象转换成字典，存入到文件中
                list1.append(i.__dict__)
            f.write(str(list1))

    def main(self):
        self.read_info()
        while True:
            self.print_info()
            num1 = int(input("请选择你需要的功能需要："))
            if num1 == 1:
                self.add_info()
            elif num1 == 2:
                self.del_info()
                print(self.student_info)
            elif num1 == 3:
                self.modify_info()
            elif num1 == 4:
                self.search_info()
            elif num1 == 5:
                self.all_info()
            elif num1 == 6:
                self.save_info()
            elif num1 == 7:
                print("退出系统")
                break
            else:
                print("请输入正确的序号")
                

if __name__ == '__main__':
    stm = StudentManger()
    stm.main()
    # stm.save_info()

