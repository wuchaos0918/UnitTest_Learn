"""
测试套件加载测试用例的方法

"""
import sys
from os.path import abspath,dirname
sys.path.insert(0,dirname(dirname(abspath(__file__))))

import unittest
from testcases import TestRegister
from testcases import TestLogin


#加载单个测试用例
def suite1():
    # 测试套件
    suite = unittest.TestSuite()
    #加载测试用例
    suite.addTest(TestRegister('test01'))
    suite.addTest(TestRegister('test02'))
    return suite

#加载多个测试用例
def suite2():
    suite = unittest.TestSuite()
    tests = [TestRegister('test02'),TestLogin('test05')]
    suite.addTests(tests)
    return suite

#使用loader加载器，加载指定类中的所有测试用例,一次只能加载一个测试类
def suite3():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestRegister)
    suite.addTests(tests)
    return suite

#使用loader加载器，加载指定模块的所有测试用例
def suite4():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromModule(test_framework.unittest_demo.testcases.test_login)
    suite.addTests(tests)
    return suite

#根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名，或者一个可调用的是实例对象
def suite5():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromName('unittest_demo.testcases.test_register')
    suite.addTests(tests)
    return suite

#与name功能相同，只不过接受的是字符串列表
def suite6():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.loadTestsFromNames(['unittest_demo.testcases.test_register','unittest_demo.testcases.test_login'])
    suite.addTests(tests)
    return suite

# discover()方法按照文件路径和方法名模糊查询加载测试用例
def suite7():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()       #加载器
    tests = loader.discover(start_dir='testcases', pattern='test*.py')
    suite.addTests(tests)
    return suite

# 运行测试套件,生成测试报告
if __name__ == '__main__':
    suite = suite4()
    with open(file='report/suite_report.txt', mode='a') as file:
        runner = unittest.TextTestRunner(verbosity=2,stream=file)
        runner.run(suite)
        file.close()




