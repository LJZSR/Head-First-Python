import requests

urls = ('http://www.baidu.com', 'http://www.163.com', 'http://www.sina.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, resp.url)
print()

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, resp.url)
