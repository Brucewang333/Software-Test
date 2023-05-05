import requests

# 发送get请求，指定url，获取 响应结果
resp = requests.get(url="http://127.0.0.1/Home/Goods/search.html?q=iphone")

# 查询相应结果
print(resp.text)