import logging

import allure
logging.basicConfig(level=logging.INFO)
# error > info > debug

def black_wrapper(fun):
    """
    python cookbook
    :param fun:
    :return:
    """
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            logging.info("start find: \nargs: " + str(args) + " kwargs: " + str(kwargs))
            return fun(*args, **kwargs)
        # 捕获元素没找到异常
        except Exception as e:
            basepage.screenshot("tmp.png")
            with open("./tmp.png", 'rb') as f:
                picture_data = f.read()
            allure.attach(picture_data, attachment_type=allure.attachment_type.PNG)
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
