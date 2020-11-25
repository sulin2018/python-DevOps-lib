import json

import requests

from dingding_api.config import AGENT_ID, CORP_ID, CORP_SECRET, BASE_URL


class DingBase(object):
    """
    钉钉api基础对象:获取并提供钉钉凭证token
    """

    def __init__(self):
        self.agent_id = AGENT_ID
        self.corp_id = CORP_ID
        self.corp_secret = CORP_SECRET
        self.base_url = BASE_URL
        self.headers = {'content-type': 'application/json'}

    @property
    def token(self):
        """
        钉钉token
        :return:
        """
        urls = self.base_url + 'gettoken'
        params = {
            'corpid': self.corp_id,
            'corpsecret': self.corp_secret,
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['access_token']
        else:
            raise ValueError('获取凭证失败, ' + data['errmsg'])
