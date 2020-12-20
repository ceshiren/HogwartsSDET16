from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.base_page import BasePage


class ContactPage(BasePage):
    def add_member(self):
        """
        添加成员操作
        :return:
        """
        pass

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        member_list2 = []
        for i in member_list:
            member_list2.append(i.text)
        return member_list2