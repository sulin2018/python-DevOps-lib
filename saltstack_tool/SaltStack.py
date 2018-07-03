"""
SaltStack api，通过调用salt-api执行相关命令
"""
import re

import requests


class SaltStackBase:
    """
    Salt Api 操作类
    """
    def __init__(self, url, username, password):
        """
        初始化salt api操作类
        :param url: Salt API的服务地址
        :param username: 用户名
        :param password: 密码
        """
        if url.endswith('/'):
            self.url = url
        else:
            self.url = url + '/'
        self.username = username
        self.password = password
        # token有效期为12小时
        self.token = None

    def login(self):
        """
        登陆salt api服务器获取token
        """
        # 1. 构造POST需要登陆的数据
        data = {
            "username": self.username,
            "password": self.password,
            "eauth": 'pam',
        }

        login_url = '{}login'.format(self.url)

        # 2. post登陆salt-api服务器
        response = requests.post(url=login_url, json=data)
        # print(response)

        # 3. 如果成功记录Token
        if response.ok:
            result = response.json()
            # 获取到token
            if 'return' in result:
                self.token = result['return'][0]['token']
            else:
                self.token = None
        else:
            # 登陆获取token失败
            self.token = None

    def run_command(self, tgt=None, fun='test.ping', arg=None, client='local',
                    expr_form='list'):
        """
        执行命令
        :param tgt: 目标target
        :param fun: 要执行的功能：test.ping, cmd.run
        :param arg: 执行功能的传参，比如，uname -a
        :param client: local
        :param expr_form: 可以使tgt的值更加灵活，比如：list可以传多个host，中间用,分隔
        :return:
        """
        # 1. 需要对args进行校验，过滤删除功能
        if fun == 'cmd.run' and arg and re.match(r'\brm\b', arg):
            raise ValueError("cmd.run不能执行rm操作：%s" % arg)

        # 2. 判断token
        if not self.token:
            # 2-1: 登陆获取token
            self.login()
            # 2-2：对token进行判断
            if not self.token:
                raise ValueError("获取Token出错")

        # 3. 通过api执行命令
        # 3-1：构造数据
        headers = {
            "Accept": "application/json",
            "X-Auth-Token": self.token
        }

        # 有无额外参数
        if arg:
            data = {
                "client": client,
                "expr_form": expr_form,
                "tgt": tgt,
                "fun": fun,
                "arg": arg
            }
        else:
            data = {
                "client": client,
                "expr_form": expr_form,
                "tgt": tgt,
                "fun": fun
            }

        # 3-2: post数据
        response = requests.post(url=self.url, headers=headers, json=data)

        if response.ok:
            result = response.json()
            # print(result)
            return result
        else:
            print("{}: 执行命令出错:{}".format(tgt, response.status_code))
            return None