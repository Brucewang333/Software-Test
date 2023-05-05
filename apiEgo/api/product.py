# 导包
import requests
import app


# 商品分类接口
class ProductApi(object):

    # 初始化
    def __init__(self):
        self.all_category_url = app.URL + '/api/v1/category/all'
        self.product_items_url = app.URL + '/api/v1/product/by_category'
        self.product_info_url = app.URL + '/api/v1/product/{}'

    # 获取商品分类
    def get_all_category(self):
        return requests.get(self.all_category_url)

    # 获取商品分类下商品
    # ?id=2
    def get_product_items(self, pid):
        param = {"id": pid}
        return requests.get(self.product_items_url, params=param)

    # 获取商品信息
    def get_product_info(self, ids):
        url = self.product_info_url.format(ids)
        return requests.get(url)
