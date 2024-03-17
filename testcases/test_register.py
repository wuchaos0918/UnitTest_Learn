"""
注册功能测试用例
"""

import unittest

import pytest


class TestRegister(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp：打开注册页面')

    def tearDown(self) -> None:
        print('tearDown：关闭注册页面')

    def test01(self):
        print('test01：注册成功用例')

    @pytest.mark.xfail
    def test02(self):
        print('test02：注册失败用例')
        assert 1 == 2
