import pytest


class Test_demo2():
    def test_one2(self, myfixture):
        print("执行test_one2")
        assert 1 + 1 == 2

    def test_two2(self, myfixture):
        print("执行test_two2")
        assert 1 + 1 == 2

    def test_three2(self):
        print("执行test_three2")
        assert 1 + 1 == 2
