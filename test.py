# 装饰器和回掉函数区别:作用差不多，但是回调函数调用会直接执行，而装饰器会在调用时返回一个新的函数

import time
def count_time(func):
    def wrapper():
        s = time.time()
        res = func()
        e = time.time()
        print(e-s)
        return res
    return wrapper

@count_time
def test():
    for i in range(1000000):
        a = 1
        pass
    return 1

# count_time(test)()
a = test()
print(a)
import test_bag

test_bag.hello2()