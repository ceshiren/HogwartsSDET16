from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.add_member_page import AddMember
from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR,".ww_indexImg_AddMember")
    def goto_add_member(self):
        """跳转到添加chengyuanyemian
        :return:
        """
        # 解元祖操作，把元祖内的元素拆分作为不同d的参数传入
        self.find(self._location_goto_member).click()

        return AddMember(self.driver)

    def goto_contact(self):
        """跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()