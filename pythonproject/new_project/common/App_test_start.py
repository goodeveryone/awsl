import time
import os
import csv

class App():
    def __init__(self):
        self.data=[('now','time')]

    def startApp(self):
        """cmd运行adb命令"""
        # cmd="adb shell am start -W -n com.tal.kaoyan/.ui.activity.SplashActivity"
        # time_data = os.popen(cmd)
        cmd="adb shell dumpsys cpuinfo"
        time_data=os.popen(cmd)
        print(time_data)
        for line in time_data:
            if "system_server" in line:
                massage=line.split(" ")[1]
                now=time.strftime("%Y-%m-%d  %H:%M:%S")
                # self.data.append((now,massage))
                print(massage)
                print(1)

#     def closeApp(self):
#         # cmd="adb shell am force-stop com.tal.kaoyan"
#         cmd="adb shell input keyevent 3"
#         os.popen(cmd)
#
#     def saveDate(self):
#         with open("../data/save_ThisTime.csv",'a',newline='')as f:
#             writer=csv.writer(f)
#             writer.writerows(self.data)
#
# class Contorller():
#     def __init__(self,count):
#         # App类的实例化，定义参数count
#         self.app=App()
#         self.count=count
#
#     def oneTest(self):
#         # 执行一次的步骤
#         self.app.startApp()
#         time.sleep(2)
#         self.app.saveDate()
#         self.app.closeApp()
#
#     def run(self):
#         # for循环写入执行的次数
#         for i in range(self.count):
#             self.oneTest()
#             time.sleep(2)

if __name__ == "__main__":
    a=App()
    a.startApp()
    # a.saveDate()
    # a.closeApp()
    # countroller=Contorller(2)
    # countroller.run()



