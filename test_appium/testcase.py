from test_appium.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwarts"
        gender = "男"
        phone_number = "11111111111"
        result = self.main.goto_address().click_addmember().add_member_menual().add_contact(name, gender, phone_number)
