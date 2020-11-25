"""
部门操作相关api
"""
import json

import requests

from dingding_api.base import DingBase


class DingDepartment(DingBase):
    def get_department_list(self):
        """
        获取部门列表
        :return:
        """
        urls = self.base_url + 'department/list'
        params = {
            'access_token': self.token
        }
        r = requests.get(urls, params)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['department']
        else:
            raise ValueError('获取部门列表失败, ' + data['errmsg'])

    def get_department_users(self, department_id):
        """
        获取部门成员
        :param department_id:
        :return:
        """
        urls = self.base_url + 'user/simplelist?access_token={}&department_id={}'.format(self.token, department_id)
        r = requests.get(urls)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['userlist']
        else:
            raise ValueError('获取部门成员失败, ' + data['errmsg'])

    def get_department_users_detail(self, department_id):
        """
        获取部门成员(详情)
        :param department_id:
        :return:
        """
        urls = self.base_url + 'user/list?access_token={}&department_id={}'.format(self.token, department_id)
        r = requests.get(urls)
        data = json.loads(r.text, encoding="utf-8")
        if data['errmsg'] == 'ok' and data['errcode'] == 0:
            return data['userlist']
        else:
            raise ValueError('获取部门成员(详情)失败, ' + data['errmsg'])

