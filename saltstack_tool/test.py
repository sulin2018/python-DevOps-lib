"""
测试代码
"""
from saltstack_tool import config
from saltstack_tool.SaltStack import SaltStackBase

salt_api = SaltStackBase(config.SALT_URL, config.SALT_USER, config.SALT_PASSWORD)
salt_api.login()
print(salt_api.token)
