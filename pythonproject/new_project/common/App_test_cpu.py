import time
import csv
import os

class Cpu():
    def __init__(self,count):
        self.save=[('now','cpu')]
        self.count=count

    def onetest(self):
        cmd='adb shell dumpsys cpuinfo'
        data=os.popen(cmd)
        # print(data)
        for line in data.readlines():
            if 'com.tal.kaoyan' in line:
                cpu_data=line.split('%')[0]
                now=time.strftime('%Y-%m-%d-%H-%M-%S')
                self.save.append((now,cpu_data))
        print(self.save)

    def run(self):
        while self.count > 0:
            self.onetest()
            time.sleep(3)
            self.count -= 1

    def saveData(self):
        with open('../data/Cpu_Data.csv','a',newline='')as f:
            writer=csv.writer(f)
            writer.writerows(self.save)


if __name__ == '__main__':
    cpu=Cpu(10)
    cpu.run()
    cpu.saveData()



