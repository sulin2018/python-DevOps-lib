# python-gitlab
python对接Gitlab API

# 使用
1. 搭建一个gitlab服务器,拥有一个账户
2. 生成token文件,请看这里`https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html`
3. 填写正确的gitlab服务器地址和token信息gitlab_api/config.py
```
# 用户授权凭证token
GITLAB_TOKEN = ''
# gitlab api地址
GITLAB_BASE_URL = 'http://127.0.0.1:7780/api/v4'
```
4. 安装必要的包:`pip install requests`.

好了,可以开始运行test包中测试脚本了.

测试没有问题,可以把gitlab_api包放入项目中使用了.

# 注意
获取信息是基于用户权限的,确保用于生成token的账户权限足够大.