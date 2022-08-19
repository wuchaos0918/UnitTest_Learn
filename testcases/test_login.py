"""
登录功能测试用例
"""

import unittest


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass：打开登录页面')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass：关闭登录页面')

    def test03(self):
        print('test03：登录成功用例')

    def test04(self):
        print('test04：登录失败用例')
