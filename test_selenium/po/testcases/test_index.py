from test_selenium.po.page.index_page import IndexPage

#2. 编写业务测试用例

class TestIndex:

    def setup_class(self):
        # 实例变量可以在类的其他方法使用
        self.index_page = IndexPage()

    def test_login(self):
        # 1.跳转到登录页面， 2. 在登录页面扫码登录
        self.index_page.goto_login().login_scanf()

    def test_register(self):
        # 1.跳转到注册页面， 2. 在注册页面进行注册
        self.index_page.goto_register().register()