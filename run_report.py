"""
生成测试报告的几种方式

"""
import unittest
# import HTMLTestRunner
from BeautifulReport import BeautifulReport


def suite():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='./testcases', pattern='test*.py')
    testsuite.addTests(tests)
    return testsuite


# TextTestRunner
# if __name__ == '__main__':
#     suite = suite()
#     with open(file='./report/report.txt', mode='a') as file:
#         runner = unittest.TextTestRunner(verbosity=2, stream=file)
#         runner.run(suite)

# HTMLTestRunner
# if __name__ == '__main__':
#     suite = suite()
#     with open(file='HTMLReport.html', mode='w') as file:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2)
#         runner.run(suite)

# BeautifulReport
if __name__ == '__main__':
    suite = suite()
    result = BeautifulReport(suite)
    result.report(report_dir='./report', filename='breport.html', description='注册和登录功能测试报告')
