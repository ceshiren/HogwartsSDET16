from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.addresss_list_page import AddresssListPage
from test_appium.po.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页 PO
    """
    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        # todo 点击通讯录按钮
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id ='com.tencent.wework:id/elq']")
        return AddresssListPage(self.driver)
