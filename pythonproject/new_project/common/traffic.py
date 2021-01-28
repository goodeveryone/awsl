# 流量
import os
import time
import csv

class Traffic():
    def __init__(self):
        # self.count=count
        self.save=[('now','time')]

    def oneTest(self):
        pid_data=os.popen("adb shell ps")
        for line in pid_data:
            if "com.tal.kaoyan" in line:
                pid01=line.split(" ")
                pid02=[]
                for i in pid01:
                    if i == "":
                        continue
                    else:
                        pid02.append(i)
                self.pid=pid02[1]

        tra=os.popen(f"adb shell cat /proc/{self.pid}/net/dev")
        for line in tra:
            if "wlan" in line:
                wlan_data01=line.split(" ")
                wlan_data02=[]
                for i in wlan_data01:
                    if i == "":
                        continue
                    elif i == "0":
                        continue
                    else:
                        wlan_data02.append(i)
                # print(wlan_data02)
                # wlan发送数据
                wlan_recevice=wlan_data02[1]
                # wlan接收数据
                wlan_tream=wlan_data02[3]
                # wlan总流量
                self.wlan_traffic=int(wlan_recevice)+int(wlan_tream)

        tra = os.popen(f"adb shell cat /proc/{self.pid}/net/dev")
        for line in tra:
            if "eth" in line:
                eth_data01=line.split(" ")
                # print(eth_data01)
                eth_data02=[]
                for i in eth_data01:
                    if i == "":
                        continue
                    elif i == "0":
                        continue
                    else:
                        eth_data02.append(i)
                # print(eth_data02)
                # eth发送的流量
                eth_Receive=eth_data02[1]
                # eth接受的流量
                eth_Transmit=eth_data02[3]
                # eth总流量
                self.eth_traffic=int(eth_Receive)+int(eth_Transmit)

        # app的总流量
        all_traffic=int(self.wlan_traffic)+int(self.eth_traffic)
        traff = "%.2f" % (all_traffic / 1024)
        print(traff)
        now=time.strftime("%Y-%m-%d%H:%M:%S")
        with open("../data/traffic.csv","a",newline="") as f:
            # writer = csv.writer(f)
            # writer.writerows(self.save)
            f.write(now)

if __name__ == "__main__":
    traffic=Traffic()
    traffic.oneTest()




