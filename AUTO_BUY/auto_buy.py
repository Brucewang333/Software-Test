import requests
import json
import time

# 设置抢票时间
buy_time = '2023-05-05 12:00:00'
# 设置演出ID和场次ID
project_id = '123456'
schedule_id = '789012'

# 获取Cookie和Header
url = 'https://api5.tickets.mypaas.com.cn/user/loginByCookie?companyId=1'
cookie = '这里填写您的Cookie'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Referer': 'https://www.damai.cn/'
}

# 登录大麦网
session = requests.session()
session.headers.update(headers)
session.cookies.update(requests.utils.cookiejar_from_dict(requests.utils.dict_from_cookiejar(session.cookies)))
session.cookies.set('Cookie', cookie)

# 访问选座购买页面
url = 'https://piao.damai.cn/mpp_seatSelection/index.html?projectId={}&spm=a2oeg.home.card_0.ditem_3_78a5233b3WNGkt&tkFlag=1&damai=1'.format(project_id)
res = session.get(url)

# 提交选座信息
url = 'https://piao.damai.cn/mpp_seatSelection/selectSeat.html'
headers.update({'Content-Type': 'application/json;charset=UTF-8'})
payload = {
    'projectId': project_id,
    'scheduleId': schedule_id,
    'seatTicketList': [{
        'seatId': '123456',
        'ticketNum': 1,
        'realPrice': 0,
        'ticketPrice': 0,
        'serviceFee': 0,
        'exchangeFee': 0
    }],
    'buyNum': 1
}
res = session.post(url, headers=headers, data=json.dumps(payload))

# 获取订单信息
url = 'https://buy.damai.cn/orderConfirm?buy=1'
res = session.get(url)
orderId = json.loads(res.text)['Data']['OrderConfirmModel']['OrderId']

# 确认订单
url = 'https://buy.damai.cn/confirmOrder.html'
payload = {
    'OrderIds': orderId
}
res = session.post(url, headers=headers, data=payload)

# 轮询判断订单是否成功
order_status = ''
while order_status != 'success':
    url = 'https://buy.damai.cn/queryOrderStatus.json?orderIds={}'.format(orderId)
    res = session.get(url)
    order_status = json.loads(res.text)['orderConfirm']['orderStatus']
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '当前订单状态：', order_status)
    time.sleep(1)
