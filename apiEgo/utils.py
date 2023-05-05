# 封装初始化日志函数

# 导包
import logging
from logging import handlers
import app


# 定义初始化日志函数
def init_log():
    # 创建日志器
    logger = logging.getLogger()  # 创建日志器对象
    logger.setLevel(logging.INFO)  # 设置日志器对应日志的格式

    # 定义处理器
    sh = logging.StreamHandler()  # 创建控制台处理器对象
    log_file = app.BASE_DIR + '/log/Ego.log'
    fh = logging.handlers.TimedRotatingFileHandler(log_file,  # 定义日志文件
                                                   when='midnight',  # 记录日志时间
                                                   interval=1,  # 记录日志频率
                                                   backupCount=3,  # 保存日志的时间
                                                   encoding='utf-8'  # 日志编码方式
                                                   )  # 文件处理器对象


# 定义格式化器

    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"  # 创建格式化器
    formatter = logging.Formatter(fmt)  # 创建格式化对象
    # 设置处理器的格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
