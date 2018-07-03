import jenkins

from jenkins_tool.config import JENKINS_URL, JENKINS_USER, JENKINS_PASSWORD

# 这里是通过Jenkins包对接
server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USER, password=JENKINS_PASSWORD)
user = server.get_whoami()
# 这里是Jenkins官方的一个示例,但是出现403访问bug,不知道是不是我Jenkins版本2.107.2太高的问题
# version = server.get_version()
# print('Hello %s from Jenkins %s' % (user['fullName'], version))

print(user)
print(server.build_job('test'))


# 以下是通过jenkinsapi包对接
from jenkinsapi.jenkins import Jenkins

def getSCMInfroFromLatestGoodBuild(url, jobName, username=None, password=None):
    J = Jenkins(url, username, password)
    print(J.version)
    print(J.has_job(jobName))
    job = J[jobName]
    lgb = job.get_last_good_build()
    return lgb.get_revision()

if __name__ == '__main__':
    print(getSCMInfroFromLatestGoodBuild(JENKINS_URL, 'test',JENKINS_USER,JENKINS_PASSWORD))