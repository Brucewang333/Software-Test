'''
因为日志需要在接口被调用时首先打印出来
而_init_.py在接口被调用时会最先执行
所以在这里调用日志函数
'''
# 1. 导包
import utils
import logging

# 2. 调用初始化函数
utils.init_log()
# 打印测试信息
logging.info('这是一条日志信息')
