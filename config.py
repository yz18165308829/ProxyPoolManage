"""
Date: 2019--14 16:37
User: yz
Email: 1147570523@qq.com
Desc:

"""
# Redis数据库地址
REDIS_HOST = '127.0.0.1'
# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 3
MIN_SCORE = 0
INITIAL_SCORE = 1

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 200
#线程
ThreadCount=100
FilterThreadCount = 100
# 检查周期
TESTER_CYCLE = 10
# 获取周期
GETTER_CYCLE = 20

# # 测试API，建议抓哪个网站测哪个
# TEST_URL = 'http://www.baidu.com'
# # API配置
API_HOST = '172.25.254.39'
API_PORT = 9999
#
# # 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
# # 最大批测试量
# BATCH_TEST_SIZE = 10