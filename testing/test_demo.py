import pytest

def add_function(a, b):
    return a + b

@pytest.mark.parametrize("a", [0, 1, 5])
@pytest.mark.parametrize("b", [2, 3, 8])
def test_add(a, b):
    print("测试数据组合：a->%s,b->%s" % (a, b))
