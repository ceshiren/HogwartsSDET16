import pytest
import requests


class TestContact:

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc')
        token = r.json()['access_token']
        return token

    def create_member(self):
        # 1. 判断错误类型 ： 手机号已经存在
        # 2. 进行错误处理：根据错误信息，查找 zhangsan00123 ，调用查找接口
        # 3. 调用删除接口：删除冗余数据
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}'
        data = {
            "userid": "zhangsan00123",
            "name": "张三hello",
            "mobile": "+86 13812300000",
            'department': [3]
        }
        r = requests.post(url=create_member_url, json=data)
        # assert 'created' == r.json().get('errmsg', None)

    def setup(self):
        self.create_member()

    def test_delete_member(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zhangsan00123'
        proxies = {"https": "127.0.0.1:8888"}
        r = requests.get(delete_url, proxies=proxies, verify=False)
        print(r.json())

    def teardown(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zhangsan00123'
        r = requests.get(delete_url)
        print(r.json())


def get_token():
    r = requests.get(
        'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc')
    token = r.json()['access_token']
    return token

@pytest.mark.parametrize("tmp", range(50))
def test_defect_member(tmp):
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=kenan222'
    r = requests.get(get_member_url)
    print(r.json())
    assert "小柯南" == r.json()['name']


def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid": "kenan222",
        "name": "小柯南",
        "mobile": "13800009999",
    }
    r = requests.post(url=update_member_url, json=data)
    print(r.json())


@pytest.mark.parametrize("left, right", [(2, 6), (3, 8), (4, 5)])
def test_generate(left, right, pre=1):
    """
    七点法数据生成
    :param left:
    :param right:
    :param pre:
    :return:
    """
    result = []
    # 提取左边界三个值
    lefts = [left - pre, left, left + pre]
    # 提取右边界三个值
    rights = [right - pre, right, right + pre]
    # 提取中间值
    mid = (left + right) // 2  # c 语言除法
    # 将三组值组合
    result += lefts
    result.append(mid)
    result += rights
    print(set(result))
