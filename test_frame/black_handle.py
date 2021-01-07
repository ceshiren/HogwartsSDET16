def black_wrapper(fun):
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        # 捕获元素没找到异常
        except Exception as e:
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                # 黑名单被找到
                if len(eles) > 0:
                    # 对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run
