import pytest

from test_selenium.test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        # 第一次实例化
        self.main = MainPage()

    def test_add_member(self):
        """添加成员测试用例
        :return:
        """
        #1.跳转添加成员页面  2. 添加成员 3. 自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member().get_member()
        assert "赫敏2" in res

    @pytest.mark.parametrize("accid, phone, expect_res",
                             [("xxx3", "13199998888", "该帐号已被“lx3”占有"),
                              ("xx2", "13388881235", "该手机号已被“lx3”占有")])
    # 第一次参数化， 传入重复的accid， 正确的手机号， 断言信息
    # 第一次参数化， 传入正确的accid， 重复的手机号， 断言信息
    def test_add_member_fail(self, accid, phone, expect_res):
        """
        :param accid: id信息
        :param phone: 手机信息
        :return:
        """
        res = self.main.goto_add_member().add_member_fail(accid, phone)
        assert expect_res in res



    def test_add_member_by_contact(self):
        """通过通讯录页面添加成员
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert "赫敏2" in res

    # 回复到首页还原一开始的状态
    def teardown(self):
        self.main.back_main()

    # def teardown_class(self):
    #     time
    #     self.main.quit()