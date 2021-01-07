# 封装，继承，多态，抽象 <-> 面向过程

def b(fun):
    # fun = a
    def run1234(*args, **kwargs):
        print("a1")
        fun(*args, **kwargs)
        print("a2")

    return run1234


# def b(a):
#     print('a1')
#     a()
#     print('a2')

@b
def a():
    print('a')


# def a():
#     print('a1')
#     print('a')
#     print('a2')


def test():
    a()
