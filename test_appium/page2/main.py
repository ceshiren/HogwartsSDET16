from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.address_list_page import AddressListPage
from test_appium.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    # address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    address_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq']")

    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self):
        """
        进入到通讯录页
        :return:
        """
        # 进入到通讯录界面
        # self.find(*self.address_element).click()
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)
