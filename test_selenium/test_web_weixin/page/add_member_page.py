from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage


class AddMember(BasePage):
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID,"memberAdd_acctid")
    _location_Add_phone = (By.ID,"memberAdd_phone")

    def add_member(self):
        """添加成员操作
        :return:
        """
        self.driver.find_element(*self._location_username).send_keys("赫敏2")
        self.driver.find_element(*self._location_acctid).send_keys("020")
        self.driver.find_element(*self._location_Add_phone).send_keys("13177778882")
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        """
        添加成员失败操作
        :return:
        """
        self.driver.find_element(*self._location_username).send_keys("赫敏2")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # error_message = self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phone_error_message = self.find(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list = [error_message, phone_error_message]
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list
