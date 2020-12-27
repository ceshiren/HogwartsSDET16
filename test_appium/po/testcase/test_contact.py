from test_appium.po.page.app import App


def test_add_member():
    app = App()
    app.start()
    result = app.goto_main().goto_address().click_addmember().add_member_manual().add_contact()
    assert result
