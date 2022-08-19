"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : unittest-demo
@File : test_case.py
@Author : 057776
@Time : 2022/8/19 11:17

"""
import unittest


class TestCase(unittest.TestCase):

    def test_one(self):
        pass

    def test_two(self):
        print(self.id())

    def test_three(self):
        self.assertEqual(1, 1, '断言 a == b')

    def test_four(self):
        self.skipTest(reason='this is reason')

    @unittest.skip
    def test_five(self):
        pass


# def suite():
#     testsuite = unittest.TestSuite()
#     tests = [TestCase('test_one'), TestCase('test_two')]
#     suite.addTests(tests)
#     return testsuite


if __name__ == '__main__':
    unittest.main(verbosity=2)

    # TestCase().run()

    # suite = suite()
    # test_result = unittest.TestResult()
    # suite.run(result=test_result)
