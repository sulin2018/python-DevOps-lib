# python-dingding
python对接钉钉API库

# 使用
填写正确的公司钉钉秘钥配置信息
```
# 钉钉调用授权秘钥,可在钉钉后台获取
CORP_ID = '',
CORP_SECRET = '',
BASE_URL = 'https://oapi.dingtalk.com/'
# 企业应用的agent id
AGENT_ID = ''
```
安装必要的包:`pip install requests`.

好了,可以开始运行test包中测试程序了.

测试没有问题,可以把dingding_api包放入项目中使用了.