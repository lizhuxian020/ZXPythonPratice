# coding: utf-8

import linecache
import string
import time

fields = 'bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url'
fileName = 'twitter.txt'
bad_data_line_list = []

def makeObjectWithLine(line):
    line = line.replace('"', '')
    line = line.split(',')
    return line

def obj_count():
    c = open(fileName, 'r')
    content = c.read()
    c.close()
    return content.count('\n')

def get_props_list(props_name, uniq = False):
    # 解析fileds得到list
    props_list = fields.split(',')
    props_value_list = []
    for i in range(1, obj_count() + 1):
        data_list = makeObjectWithLine(linecache.getline(fileName, i))
        uni_dic = dict(zip(props_list, data_list))
        props_value_list.append(uni_dic[props_name])

    if not uniq:
        return props_value_list
    props_value_new_list = list(set(props_value_list))
    props_value_new_list.sort(key=props_value_list.index)
    return props_value_new_list

def init_bad_data():
    '''计算坏数据行数'''
    for i in range(1, obj_count() + 1):
        data_list = makeObjectWithLine(linecache.getline(fileName, i))
        if len(data_list) > 35:
            bad_data_line_list.append(str(i))
    print len(bad_data_line_list)

def delelte_line(ori_file, prd_file, delete_line_list):
    content_prd = ''
    file_ori = open(ori_file, 'r')
    a = file_ori.readlines()
    print a
    print len(a)
    file_ori.close()
    print content_prd


if __name__ == '__main__':

    # 0.多少个数据: 38118
    # print obj_count()

    # 1.多少用户 & 2.多少名字: 2077
    # print len(get_props_list('username', True))

    # date_list = get_props_list('time')
    # init_bad_data()
    delelte_line('content_ori.txt', 'content_prd.txt', [1, 3, 5])

    # 3.多少个在2012.11: 32846
    # print len([date for date in date_list if '2012-11' in date])

    # 4.一共有多少天: 223
    # print len(set([date.split(' ')[0] for date in date_list]))

    # 5.哪个小时发布的微博最多: (u'2012-11-04 11', 3907)
    # print date_list
    # hour_list = [date[:13] for date in date_list]
    # hour_uniq_list = list(set(hour_list))
    # count_list = []
    # for hour in hour_uniq_list:
    #     count = hour_list.count(hour)
    #     count_list.append((hour, count))
    # print sorted(count_list, key=lambda x: x[1], reverse=True)[0]

    # 6.时间段发布最多的用户
    # print date_list
    # temp_list = [date.split(' ')[0] for date in date_list]
    #
    # result_list = []
    # print temp_list
    # for x in temp_list:
    #     if '-' not in x:
    #         print '----->' + x


