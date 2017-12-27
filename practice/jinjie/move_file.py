# coding: utf-8
# Author: lee_zix


import os

if __name__ == '__main__':

    pre_path = '/Users/forzqy/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1e97bc759d3ad03102ba787e1e1d1edb/Message/MessageTemp/9e20f478899dc29eb19741386f9343c8/Image'

    amount = 4

    # for x in os.listdir(pre_path):
    #     son_path = os.path.join(pre_path, x)
    #     if os.path.isfile(son_path):
    #         print son_path

    filelist = [x for x in os.listdir(pre_path) if os.path.isfile(os.path.join(pre_path, x)) and '_thumb.' not in x]

    filelist.sort()

    print filelist

    length = len(filelist)

    if length % amount == 0:
        for i in range(length/amount):
            print filelist[i*amount:(i+1)*amount]
    else:
        print 'can\'t move'