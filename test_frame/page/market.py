from test_frame.page.pre_page import PrePage
from test_frame.page.search import Search


# 面向对象四大特点
class Market(PrePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.basepage.load("../page/market.yaml")
        return Search(self.basepage)
