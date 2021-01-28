import unittest
from common.jmeter_code import Movie
from common.jmeter_code import duqu_csv
import logging.config
from parameterized import parameterized,param
from time import sleep
from time import strftime
from time import strptime
import unittest
from common.jmeter_code import Movie
import logging.config
from parameterized import parameterized




# 匹配日志文件
# 采集器
logging.config.fileConfig("../config/peizhi_logcat.conf")
logging=logging.getLogger()


sj = duqu_csv()

# 继承unittest下的类
class Movie_test(unittest.TestCase):
    movie = Movie()
    sj = duqu_csv()
    @parameterized.expand([param(i[0],i[1],i[2])for i in sj])
    def test_99(self,a,b,c):
        res=self.movie.find(a,b,c)
        if b != 'ff887797d7c16a9d50bfbf7f60caecc5':
            self.assertEqual(10001,res['error_code'])
        elif a != '双龙会':
            self.assertNotEqual('200',res['result'])
        else:
            self.assertEqual('双龙会',res['result'][0]['title'])
        if c == 1 or c == 0:
            if c == 1:
                self.assertEqual(len('result'),2)
                # self.assertEqual('双龙会', res['result'][0]['title'])
            else:
                self.assertGreater(len('result'),1)


    # def test_01(self):
    #     res=self.movie.find(self.sj[1][0],self.sj[1][1],self.sj[1][2])
    #     self.assertEqual('双龙会',res['result'][0]['title'])
    #     logging.info('')
    #
    # def test_02(self):
    #     res=self.movie.find(self.sj[2][0],self.sj[2][1],self.sj[2][2])
    #     self.assertNotEqual('200', res['error_code'])
    #     # self.assertEqual(None,res('result'))
    #     logging.info('')
    #
    # def test_03(self):
    #     res = self.movie.find(self.sj[3][0],self.sj[3][1],self.sj[3][2])
    #     self.assertEqual(10001, res['error_code'],msg='断言不通过')
    #     logging.info('')

    # def test_04(self):
    #     pass

if __name__ == '__main__':
    unittest.main()






























