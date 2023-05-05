# 1.导包
import requests

import app


# 2.封装接口类
class OrderApi(object):
    # 定义初始化方法
    def __init__(self):
        self.order_list_url = app.URL + "/api/v1/order/by_user"  # url中查询参数删除
        self.creat_order_url = app.URL + "/api/v1/order"
        self.show_order_url = app.URL + "/api/v1/order/{}"  # 路径参数可以格式化输出

    # 定义接口方法
    # 获取订单列表
    def get_order_list(self, page):
        # ?page=1 转换为JSON格式数据
        data = {"page": page}
        return requests.get(self.order_list_url, headers=app.header, params=data)

    # 创建订单接口
    def creat_order(self, pid, count):
        """
        :param pid: 商品编号
        :param count: 商品数量
        :return: 订单信息
        """
        data = {"products": [{"product_id": pid, "count": count}]}
        return requests.post(self.creat_order_url, headers=app.header, json=data)

    # 查看订单详情
    def show_order(self, order_id):
        new_url = self.show_order_url.format(order_id)
        return requests.get(new_url, headers=app.header)
