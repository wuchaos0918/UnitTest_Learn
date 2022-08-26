"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : unittest-demo
@File : conftest.py
@Author : 057776
@Time : 2022/8/26 10:05

"""
import pytest


@pytest.fixture(scope="session", autouse=True)
def browser():
    print("打开浏览器")
    yield True
    print("关闭浏览器")
