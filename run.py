"""
程序主入口，运行测试用例，生成测试报告
1、实例化一个测试套件
2、加载测试用例到测试套件
3、运行测试套件
4、生成测试报告

"""
"""
找不到 unittest_demo 解决方法
import sys
from os.path import abspath,dirname
sys.path.insert(0,dirname(dirname(abspath(__file__))))

"""
import unittest


#封装测试套件方法
def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()  #loader加载器
    tests = loader.discover(start_dir='testcases', pattern='test*.py')
    suite.addTests(tests)   #将多个测试用例加载到测试套件
    return suite

# 运行测试套件，并输出文本测试报告
if __name__ == '__main__':
    suite = suite()
    with open(file='report/report.txt', mode='a') as file:
        runner = unittest.TextTestRunner(verbosity=2,stream=file)   #文件流
        runner.run(suite)
        file.close()

