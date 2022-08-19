"""
测试套件加载测试用例的方法

"""
import unittest
from testcases import test_register, test_login


# addTest(test) 添加一个TestCase或者TestSuite到测试套件中，test必须是已经实例化的对象。
# 加载单个测试用例
def suite1():
    testsuite = unittest.TestSuite()
    test = test_register.TestRegister('test01')
    testsuite.addTest(test)
    return testsuite


# 逐个加载测试用例
def suite11():
    testsuite = unittest.TestSuite()
    test1 = test_register.TestRegister('test01')
    test2 = test_register.TestRegister('test02')
    testsuite.addTest(test1)
    testsuite.addTest(test2)
    return testsuite


# 加载单个测试套件
def suite12():
    testsuite = unittest.TestSuite()
    test2 = test_register.TestRegister('test02')
    testsuite.addTest(suite1())
    testsuite.addTest(test2)
    return testsuite


# addTests(tests) 添加多个TestCase或者TestSuite到测试套件中,tests必须是已经实例化，并且可迭代的对象.
# 加载多个测试用例
def suite2():
    testsuite = unittest.TestSuite()
    tests = [test_login.TestLogin('test03'), test_login.TestLogin('test04')]
    testsuite.addTests(tests)
    return testsuite


# 加载多个测试套件
def suite21():
    testsuite = unittest.TestSuite()
    tests = [suite1(), suite2()]
    testsuite.addTests(tests)
    return testsuite


# TestLoader() 测试加载器
# loadTestsFromTestCase(testCaseClass) 加载某个测试类中的所有测试用例
def suite3():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(test_register.TestRegister)
    testsuite.addTests(tests)
    return testsuite


# loadTestsFromModule(module) 加载某个模块中的所有测试用例
def suite4():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromModule(test_register)
    testsuite.addTests(tests)
    return testsuite


# loadTestsFromName(name) 根据给定的字符串来获取测试用例套件，字符串可以是模块名，测试类名，测试类中的测试方法名
def suite5():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromName('testcases.test_register')
    testsuite.addTests(tests)
    return testsuite


# loadTestsFromNames(names) 与name功能相同，只不过接受的是字符串列表
def suite6():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromNames(['testcases.test_register', 'testcases.test_login'])
    testsuite.addTests(tests)
    return testsuite


# discover(start_dir, pattern='test*.py') 根据指定的目录和匹配规则，递归所有子目录模糊查询加载测试用例
def suite7():
    testsuite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir='./testcases', pattern='test*.py')
    testsuite.addTests(tests)
    return testsuite


# 运行测试套件
if __name__ == '__main__':
    suite = suite1()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
