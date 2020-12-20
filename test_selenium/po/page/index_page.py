from test_selenium.po.page.login_page import LoginPage
from test_selenium.po.page.register_page import RegisterPage


class IndexPage:
    def goto_login(self):
        """跳转到登录页面
        :return:
        """
        return LoginPage()

    def goto_register(self):
        """跳转到注册页面
        :return:
        """
        return RegisterPage()
