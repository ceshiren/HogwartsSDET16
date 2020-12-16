from time import sleep

import pytest


class Test_demo():

    #  用例失败后自动重新运行：pytest-rerunfailures
    #  可以在脚本中指定定义重跑的次数，这个时候在运行的时候，就无需加上 --reruns 这个参数
    @pytest.mark.flaky(reruns=6, reruns_delay=2)
    def test_example(self):
        print(3)
        assert 1 == 2

    #  pytest-assume可以写多个断言
    def test_simple_assume(self):
        pytest.assume(1 == 1)
        pytest.assume(True)
        pytest.assume(False)

    def test_one_0(self):
        sleep(1)
        assert 1 == 1

    def test_one_1(self):
        sleep(1)
        assert 1 == 1

    def test_one_2(self):
        sleep(1)
        assert 1 == 1

    def test_one_3(self):
        sleep(1)
        assert 1 == 1

    def test_one_4(self):
        sleep(1)
        assert 1 == 1

    def test_one_5(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_one_6(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)
    def test_one_7(self):
        sleep(1)
        assert 1 == 1
