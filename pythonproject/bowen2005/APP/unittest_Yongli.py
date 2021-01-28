
# import logging
# import logging.config
# # 匹配日志配志文件
# logging.config.fileConfig("../Class_test/peizhi.conf")
# # 采集器
# logging=logging.getLogger()


# logging.basicConfig(
#     level="DEBUG",
#     filename="../Class_test/a.txt",
#     filemode="w",
#     format="%(asctime)s %(levelname)s %(message)s %(filename)s"
# )

# 采集点
# logging.debug("111111")
# logging.info("aaaaaa")
# logging.warning("bbbbbb")
# logging.error("cccccc")
# logging.critical("dddddd")





# unittest单元测试框架
# setUpClass():所有用例执行之前执行，只执行一次
# setUp():每条用例执行之前执行一次
# tearDown():每条用例执行过之后执行一次
# tearDownClass():所有用例执行完之后执行，只执行一次
# @unittest.skip:跳过执行某一条用例
# 断言：判断预期结果和实际结果是否一致
# assertEqual(a,b,msg=),判断a和b是否相等，msg值为该断言的功能描述
# assertNotEqual(a,b,msg=),判断a和b是否不相等
# assertIn("a",b),b为字符串,列表等，判断"a"是否在b里边
# assertNotIn("a",b),判断"a"是否不在b里边

# import unittest
#
# class Test_test(unittest.TestCase):
#     def setUp(self):
#         print("BeforEeryone")
#     @classmethod
#     def setUpClass(cls):
#         print("First")
#
#     @unittest.skip
#     def test_01(self):
#         print("01")
#     def test_02(self):
#         a=1
#         self.assertEqual(a,1,msg="判断a等于2")
#     def test_03(self):
#         b=2
#         self.assertNotEqual(b,3,msg="b不等于2时通过")
#     def test_04(self):
#         b=[1,2,3,4]
#         self.assertNotIn(0,b)
#
#
#     def tearDown(self):
#         print("AfterEveryone")
#     @classmethod
#     def tearDownClass(cls):
#         print("Last")
#
# # 私有方法
# if __name__ == '__main__':
#     unittest.main()


import unittest

class Test_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    def setUp(self):
        print("setUp")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def tearDown(self):
        print("tearDown")
    def test_01(self):
        a=1
        self.assertEqual(1,a,msg="判断a与1是否相等")
    def test_02(self):
        b=1
        self.assertNotEqual(2,b,msg="判断b与2是否不相等")
    def test_03(self):
        c=[1,2,3,4,5]
        self.assertIn(1,c,msg="判断1是否在列表c中")
    def test_04(self):
        d="asdfg"
        self.assertNotIn("a",d,msg="判断a是否不在字符串d中")
    @unittest.skip
    def test_05(self):
        e=(1,2)
        p=e[0]+e[1]
        self.assertEqual(4,p,msg="p=3时断言通过")


if __name__ == "__main__":
    unittest.main()















































































