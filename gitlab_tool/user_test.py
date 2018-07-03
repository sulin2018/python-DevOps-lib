from gitlab_tool.user import UserApi

user = UserApi()
# 获取分组信息
print(user.get_groups_info())
# 获取用户信息
print(user.get_users_info())