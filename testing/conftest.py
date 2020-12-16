import pytest


@pytest.fixture(params=["参数1", "参数2"])
def myfixture(request):
    print("\n执行我的fixture，里面的参数是:%s\n" % request.param)
    yield request.param  # return直接返回，yield后面可以添加teardown
    print("清理数据，关闭数据库连接")


def pytest_collection_modifyitems(session, config, items):
    print(type(items))  # items是一个列表list
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print("item.name是%s" % item.name)
        print("item.nodeid是%s" % item._nodeid)
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
