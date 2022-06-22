"""
注册功能测试用例
"""

import unittest


class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')

    def test03(self):
        print('test03')




