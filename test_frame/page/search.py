from test_frame.base_page import BasePage
from test_frame.page.pre_page import PrePage


class Search(PrePage):
    def search(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("xxxxx")
        self.basepage.load("../page/search.yaml")
        return True

