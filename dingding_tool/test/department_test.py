from dingding_api.department import DingDepartment

depart = DingDepartment()

# 获取部门列表
print(depart.get_department_list())

# 获取部门详情
users_detail = depart.get_department_users_detail(1)
for u in users_detail:
    print(u)

