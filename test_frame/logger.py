import logging
import logging.handlers


def log_init():
    # 设置格式
    log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
    format = logging.Formatter(log_format_str)
    # 根据 log 标识获取 log
    root = logging.getLogger("my_log")
    # 加入文件句柄
    h = logging.handlers.RotatingFileHandler("./tmp.log", mode='a', encoding="utf-8")
    h.setFormatter(format)
    # 加入输出流句柄
    s = logging.StreamHandler()
    s.setFormatter(format)
    root.addHandler(h)
    root.addHandler(s)
    root.setLevel(logging.DEBUG)


log = logging.getLogger("my_log")
