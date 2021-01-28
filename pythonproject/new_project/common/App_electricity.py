import time
import os
import csv

class App():
    def __init__(self,count):
        self.save=[('now','electricity')]
        self.count=count

    def onetest(self):
        cmd="adb shell dumpsys battery"
        electr=os.popen(cmd)
        # print(list(electr))
        for line in list(electr):
            if "level" in line:
                ele_data=line.split(" ")[3].replace('\n','')
                now=time.strftime("%Y-%m-%d %H:%M:%S")
                # print(ele_data)
                self.save.append((now,ele_data))
                print(self.save)

    def saveData(self):
        with open("../data/electricity_test.csv","a",newline='') as f:
            writer=csv.writer(f)
            writer.writerows(self.save)

    def run(self):
        for i in range(self.count):
            self.onetest()
            time.sleep(2)

# 本文件自己运行是执行if下代码，
# 别的文件调用时不执行if下代码。
if __name__ == "__main__":
    app=App(2)
    app.run()
    app.saveData()
    



































