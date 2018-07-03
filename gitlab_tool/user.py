"""
用户、分组相关api
"""
import requests

from gitlab_tool.base import GitLabBase


class UserApi(GitLabBase):
    def get_groups_info(self, search=''):
        """
        获取分组信息
        :param search:组名称,如果不传默认返回所有分组信息
        :return:
        """
        url = '{}/groups'.format(self.base_url)
        params = {'search': search}

        response = requests.get(url, params=params, headers=self.headers)
        if response.ok:
            result = response.json()
            return result
        else:
            return []

    def get_users_info(self, search='', page=1, per_page=20):
        """
        获取用户信息
        :param search:用户名称,如果不传默认返回所有用户信息(有权限管理)
        :param page: 第几页
        :param per_page: 每页多少
        :return:
        """
        url = '{}/users'.format(self.base_url)
        params = {
            'page': page,
            'search': search,
            'per_page': per_page
        }
        response = requests.get(url, params=params, headers=self.headers)
        if response.ok:
            return response.json()
        else:
            return []