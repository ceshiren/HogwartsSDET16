import pytest

from test_requests.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = "hello00123"
        self.name = "hello_today"

    @pytest.mark.parametrize("corpid, corpsecret, result",
                             [(None, None, 0), ('xxx', None, 40013), (None, 'xxx', 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get('errcode') == result
        raise ValueError()

    def test_create(self):

        self.contact.create_member(userid=self.userid, name=self.name, mobile="13866666766", department=[1], alias="xxxxx")
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result["name"] == self.name

    def test_update(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="13866666766", department=[1],
                                   alias="xxxxx")
        changed_mobile = "13866666767"
        self.contact.update_member(self.userid,self.name, changed_mobile)
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result["mobile"] == changed_mobile




    def test_delete(self):
        pass

    def test_find(self):
        r = self.contact.find_member("labixiaoxin")
        print(r)
