import pytest
import yaml


def step1():
    print("打开浏览器")


def step2():
    print("注册新账号")


def step3():
    print("登录新账号")


def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "step1" in steps:
            step1()
        if "step2" in steps:
            step2()
        if "step3" in steps:
            step3()


def test_fuc():
    steps("./steps.yml")
