import pytest
import yaml

from test_weixn.tag import Tag


class TestTag:
    def setup(self):
        with open("./conf.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            secret = data["corpsecret"]
        self.tag = Tag(secret=secret)

    @pytest.mark.parametrize("name, id", [("fun", "5"),
                                          ("fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun", "3")
                                          ])
    def test_creat_tag(self, name, id):
        r = self.tag.creat_tag(name=name, id=id)
        if len(name) > 32:
            assert r['errcode'] == 40058
        else:
            assert r['errcode'] == 0

    @pytest.mark.parametrize("name,id", [("sport", "5")])
    def test_update_tag(self, name, id):
        self.tag.update_tag(name=name, id=id)
        r2 = self.tag.get_tag_list()
        tag_list = self.tag.jsonpath_req(r2, '$..tagname')
        tag_name = self.tag.jsonpath_req(r2, '$..taglist[?(@.tagid==5)].tagname')[0]
        assert name in tag_list
        assert name == tag_name

    @pytest.mark.parametrize("id", ["5"])
    def test_delete_tag(self, id):
        r = self.tag.delete_tag(id=id)
        assert r['errcode'] == 0

    @pytest.mark.parametrize("id", ["5"])
    def test_get_tag_member(self, id):
        r = self.tag.get_tag_member(id=id)
        assert r['errmsg'] == 'ok'
