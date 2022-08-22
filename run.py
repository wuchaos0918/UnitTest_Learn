"""
程序主入口

"""
import unittest


# 封装测试套件方法
def suite():
    # 实例化测试套件
    testsuite = unittest.TestSuite()

    # TestLoader测试加载器
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='testcases', pattern='test*.py')

    # 加载测试用例到测试套件
    testsuite.addTests(tests)

    return testsuite


# 运行测试套件
if __name__ == '__main__':
    suite = suite()
    # 测试运行器，生成文本格式测试报告
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
