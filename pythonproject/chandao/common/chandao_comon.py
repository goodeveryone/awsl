from selenium import webdriver
from time import sleep
import csv


def duqu_csv():
    csv_shuju=[]
    with open('../data/chan_dao.csv','r') as f:
        read = csv.reader(f)
        for line in read:
            csv_shuju.append(line)
    return csv_shuju


class Chan_Dao():
    def abc(self):
        dr = webdriver.Chrome()
        dr.get("http://127.0.0.1/zentao")
        dr.implicitly_wait(10)
        return dr

    def chan_dao_login(self,user='admin',passwd='waj521.'):
        dr = self.abc()
        dr.find_element_by_xpath('//*[@id="account"]').send_keys(user)
        dr.find_element_by_xpath('//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys(passwd)
        dr.find_element_by_xpath('//*[@id="submit"]').click()
        sleep(3)
        return dr


if __name__ == "__main__":
    cd = Chan_Dao()
    cd.chan_dao_login()















