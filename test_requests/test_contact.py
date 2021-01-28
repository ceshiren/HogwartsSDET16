import requests



def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc')
    token = r.json()['access_token']
    return token

def test_defect_member():
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=kenan222'
    r = requests.get(get_member_url)
    print(r.json())
    assert  "小柯南" == r.json()['name']

def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid": "kenan222",
        "name": "小柯南",
        "mobile": "13800009999",
    }
    r = requests.post(url=update_member_url, json=data)
    print(r.json())

def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "zhangsan00123",
        "name": "张三hello",
        "mobile": "+86 13812300000",
        'department': [3]
    }
    r = requests.post(url=create_member_url, json=data)
    print(r.json())

def test_delete_member():
    delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan00123'
    r = requests.get(delete_url)
    print(r.json())
