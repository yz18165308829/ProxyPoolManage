"""
Date: 2019--14 16:37
User: yz
Email: 1147570523@qq.com
Desc:

"""
class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')