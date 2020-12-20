from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.add_member_page import AddMember
from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage


class MainPage(BasePage):
    def goto_add_member(self):
        """跳转到添加chengyuanyemian
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()

        return AddMember(self.driver)

    def goto_contact(self):
        """跳转到通讯录页面
        :return:
        """
        return ContactPage()