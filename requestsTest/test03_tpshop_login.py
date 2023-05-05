import requests

# 发送post请求，指定url、请求头、请求体、获取相应的结果
resp = requests.post(url="http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.5065210743700985",
                     headers={"Content-Type": "application/x-www-form-urlencoded"},
                     data={"username": "16656004444", "password": "1111111", "verify_code": "8888"}
                     )
# 打印响应结果
print(resp.text)  # text
print(resp.json())  # json
