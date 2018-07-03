from gitlab_tool.config import GITLAB_BASE_URL, GITLAB_TOKEN


class GitLabBase(object):
    """
    gitlab基础类,设置了基础url、请求凭证token
    """
    def __init__(self):
        self.base_url = GITLAB_BASE_URL
        self.token = GITLAB_TOKEN
        self.headers = {
            'PRIVATE-TOKEN': GITLAB_TOKEN
        }