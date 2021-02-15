from test_weixn.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, secret):
        self.token = self.get_token(secret=secret)

    def get_token(self, secret):
        req = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww46af44d604a6f8ff",
                "corpsecret": secret
            },
            "method": "GET"
        }
        r = self.send(req)
        self.access_token = r.json()["access_token"]
        return self.access_token
