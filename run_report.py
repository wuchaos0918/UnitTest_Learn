"""
生成测试报告的几种方式

"""

import unittest
# from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='testcases', pattern='test*.py')
    suite.addTests(tests)
    return suite

#BeautifulReport
if __name__ == '__main__':
    suite=suite()
    result=BeautifulReport(suite)
    result.report(report_dir='report', filename='breport.html', description='注册和登录功能测试报告')

# # TextTestRunner
# if __name__ == '__main__':
#     suite = suite()
#     with open(file='./report/report.txt',mode='a') as file:
#         runner = unittest.TextTestRunner(verbosity=2,stream=file)
#         runner.run(suite)

# #HTMLTestRunner
# if __name__ == '__main__':
#     suite = suite()
#     fp = open('./report/report.html',mode='w',encoding='utf8')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='这是我的测试报告',verbosity=2)
#     runner.run(suite)
#     fp.close()