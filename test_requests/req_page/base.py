import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = 'wwe653983e4c732493'
        self.corpsecret = 'T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc'
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        return r.json()
