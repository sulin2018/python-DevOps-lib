"""
python-etcd对接示例
对接文档：http://python-etcd.readthedocs.io/en/latest/index.html#
"""
import etcd

from etcd_tool.config import ETCD_CLUSTER

client = etcd.Client(
    host=ETCD_CLUSTER, allow_reconnect=True)
cron = client.read('')
print(type(cron))
for child in cron.children:
    print("%s: %s" % (child.key,child.value))
