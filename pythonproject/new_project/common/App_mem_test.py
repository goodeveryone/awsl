import time
import os
import csv


class App():
    def __init__(self,count):
        self.save=[('now','mem_Virtual(G)',"mem_True(G)")]
        self.count=count

    def onetest(self):
        cmd="adb shell top -n 1"
        data=os.popen(cmd)
        # print(list(data))
        for line in list(data):
            if "com.tal.kaoyan\n" in line:
                print(line)
                a=line.split(" ")[7].replace("G","")
                mem_data_01=a
                # print(mem_data_01)
                b=line.split(" ")[8].replace("M","")
                mem_data_02=int(b)/1000
                # print(mem_data_02)
                now=time.strftime("%Y/%m/%d %H:%M:%S")
                self.save.append((now,mem_data_01,mem_data_02))
                print(self.save)

    def saveData(self):
        with open("../data/mem_test.csv","a") as f:
            writr=csv.writer(f)
            writr.writerows(self.save)

    def run(self):
        # for循环写入执行的次数
        for i in range(self.count):
            self.onetest()
            time.sleep(2)


if __name__ == "__main__":
    app=App(2)
    app.run()
    app.saveData()
































