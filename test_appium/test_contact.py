from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
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
        # 操作，在 10 内，每 0.5 s 查找一次元素
        self.driver.implicitly_wait(10)

    def test_contact(self):
        # xpath
        contact_ele = self.driver.find_element(MobileBy.XPATH,
                                               "//*[@text='通讯录' and @resource-id ='com.tencent.wework:id/elq']")
        contact_ele.click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        add_new_ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        add_new_ele.click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys("aaaaa")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()

        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys("11114444999")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()





