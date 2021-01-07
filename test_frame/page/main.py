from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_and_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")
        return Market(self.driver)