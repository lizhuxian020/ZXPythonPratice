
# coding: utf-8
# Author: lee_zix

'''
1. mashup
2. firebug
'''

import urllib
import re

# link = 'http://money.163.com/special/pinglun/'
#
# open_obj = urllib.urlopen(link)
# read_content = open_obj.read().decode('gbk').encode('utf-8')
# print read_content
#
# pattern_title = re.compile(r'<div class="item_top".*>\n.*<h2><a.*">(.*)</a>')
# name_list = pattern_title.findall(read_content)
# # print name_list[0]
#
# pattern_url = re.compile(r'<div class="item_top".*>\n.*<h2><a href="(.*)">.*</a>')
# url_list = pattern_url.findall(read_content)
# # print url_list[0]
#
# pattern_desc = re.compile(r'<p>\n?(.*)<br')
# desc_list = pattern_desc.findall(read_content)
# print desc_list[0]
# print len(desc_list)
#
# pattern_time = re.compile(r'<span class="time">([^>]*)</span>')
# time_list = pattern_time.findall(read_content)
# print time_list[0]
#
# result = []
# if len(name_list) == len(url_list) == len(time_list):
#     for i in xrange(len(name_list)):
#         result.append({"title": name_list[i], "url": url_list[i], "time": time_list[i]})
# else:
#     print len(name_list), len(url_list), len(time_list)

# for i in result:
    # print i
# for i in range(len(desc_list)):
#     print name_list[i]
#     print desc_list[i]

content = '''<p>[摘要：乐视总想把软件的价值置于硬件之上，让软件独立于硬件而存在。这是反逻辑的。将硬件制造（实体经济）置于软件价值之下，是对制造业的公然蔑视，此观念显然与世界主流乃至“中国制造2025”国家战略背道而驰。一旦“硬件应当免费”观念泛滥成灾，必将导致中国实体经济遭遇重  ...<br />
                    <span class="time">2016-04-25 14:28:18</span>
                </p>
            </div>
            <div class="item_bottom">
            <a href="http://money.163.com/15/1219/12/BB6SGNBI002551G6.html" title="宝能作为门口野蛮人是坏人吗" class="newsimg" lang="http://img1.cache.netease.com/stock/2015/12/19/20151219123414d634a_550.jpg"><img src="http://s.cimg.163.com/stock/2015/12/19/20151219123414d634a_550.jpg.119x83.jpg" alt="宝能作为门口野蛮人是坏人吗" /></a>                                <p>
[摘要：目前来说，宝能系只不过玩了发达国家几十年来一直在玩的游戏，也就是”恶意”+”杠杆”的并购。宝能系如此看重“控制”万科，是否在打万科现金的主意？]
原标题：[亦观察] No.671&nbsp;宝能作为门口的野蛮人，是坏人吗?
“谁的万科”，这几天不知道有多少新闻写过这个  ...<br />'''

pattern = re.compile(r'<p>\n(.*)\n(.*)')
d_list = pattern.findall(content)
print d_list[0][1]