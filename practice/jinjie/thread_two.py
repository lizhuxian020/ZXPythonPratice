# coding: utf-8
# Author: lee_zix


# 习题：
#
# 有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500
import threading
import time

account = 500


def fuc():
    global account
    for i in range(0, 100):
        account += 1
    pass

# th_list = []

# for i in range(0, 10):
#     th = threading.Thread(target=fuc)
#     th_list.append(th)
#
# before_time = time.time()
# for th in th_list:
#     th.start()
#
# for th in th_list:
#     th.join()
#
# print time.time() - before_time
#
# print

before_time = time.time()
for x in range(10):
    fuc()


print time.time() - before_time
print account
#
# 用多线程的方式来解决，提示需要用到这节课的内容
#
