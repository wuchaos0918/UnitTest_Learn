
import unittest

class  TestSkip(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    @unittest.skip('跳过该条测试用例')
    def test_01(self):
        print('test_01')

    @unittest.skipIf(2>1,'条件为真，跳过该条测试用例')
    def test_02(self):
        print('test_02')

    @unittest.skipUnless(2>3,'条件为不为真，跳过该条测试用例')
    def test_03(self):
        print('test_03')

    @unittest.expectedFailure
    def test_04(self):
        print('test_04')

    def test_05(self):
        print('test_05')


if __name__ == '__main__':
    unittest.main(verbosity=2)


