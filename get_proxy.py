"""
Date: 2019--15 11:40
User: yz
Email: 1147570523@qq.com
Desc:

"""
import requests

url = 'http://172.25.254.197:7777/get_proxy/'
proxy = requests.get(url).text
print(proxy)