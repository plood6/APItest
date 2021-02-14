import requests


class TestLabel:

    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "ww46af44d604a6f8ff",
            "corpsecret": "y2vDbHWlJXlljDT_e4lgBrtjFFKx6sJYwCOeum_TQEA"}
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()["access_token"]
        assert r.json()["errcode"] == 0

    def test_create(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": "API",
            "tagid": 1}
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errcode"] == 0

    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": 2,
            "tagname": "weixin"}
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errmsg"] == "updated"

    def test_delete(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}"
        data = {"tagid": 1}
        r = requests.request(method="GET", url=url, params=data)
        assert r.json()["errmsg"] == "deleted"
