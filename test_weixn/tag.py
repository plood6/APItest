from test_weixn.wework import WeWork


class Tag(WeWork):
    def creat_tag(self, name, id):
        req = {
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/tag/create',
            "method": 'POST',
            "params": {'access_token': self.token},
            "json": {"tagname": name, "tagid": id}
        }
        r = self.send(req)
        return r.json()

    def update_tag(self, name, id):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/update',
            'method': 'POST',
            'params': {'access_token': self.token},
            'json': {"tagid": id, "tagname": name}
        }
        r = self.send(req)
        return r.json()

    def delete_tag(self, id):
        req = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={id}',
            'method': 'GET'
        }
        r = self.send(req)
        print(r.json())
        return r.json()

    def get_tag_member(self, id):
        req = {
            'url': f'https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={id}',
            'method': 'get'
        }
        r = self.send(req)
        return r.json()

    def get_tag_list(self):
        req = {
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/tag/list',
            'method': 'GET',
            'params': {'access_token': self.token}
        }

        r = self.send(req)
        return r.json()
