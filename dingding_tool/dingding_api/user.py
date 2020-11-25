"""
员工操作相关api
"""
import json

import requests

from dingding_api.base import DingBase


class DingUser(DingBase):
    def get_user_detail(self, userid):
        """
        获取成员详情
        :param userid:
        :return:
        """
        urls = self.base_url + 'user/get?access_token={}&userid={}'.format(self.token, userid)
        r = requests.get(urls)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data
        else:
            raise ValueError('获取成员详情失败, ' + data['errmsg'])
