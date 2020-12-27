"""
__author__ = 'jaxon'
__time__ = '2020/12/24 下午9:00'
__desc__ = ''
"""
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage


class TestDemo:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def demo(self):
        el1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView")
        el1.click()
        el2 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout")
        el2.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找元素
        # self.driver.find_element(MobileBy.
        #                          ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                               'scrollable(true).instance(0)).'
        #                                               'scrollIntoView(new UiSelector().'
        #                                               'text("打卡").instance(0));').click()
        BasePage.find_by_swip2(self.driver, MobileBy.XPATH, "//*[@text='打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # time.sleep(2)
        print(self.driver.page_source)
        # WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
