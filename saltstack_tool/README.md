# python-saltstack
python对接SaltStack api库

# 使用
填写正确配置信息saltstack_api/config.py
```python
# 调用salt-api的url账号密码
SALT_URL = ''
SALT_USER = ''
SALT_PASSWORD = ''
```
安装必要的包:`pip install requests`.

好了,可以开始运行test测试脚本了.

测试脚本正确打印了token,可以把saltstack_api包放入项目中使用了.