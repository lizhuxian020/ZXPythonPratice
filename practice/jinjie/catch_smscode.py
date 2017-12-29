# coding: utf-8
# Author: lee_zix

import urllib

import random


url = 'http://218.19.164.168/DemoSpring/?nsukey=lhGpBTMo%2BZRThfa%2BMf2PHZFv8izPsLceu5UmybGQSwTadpOZYYt%2FWyTC5YQOFVEZvvKupOUW8HKrtnowI3iRBYso5Xl6Haez%2FGOTVtiupnWMA%2ByJMa60OQ0orVX%2F9YDg%2FELq2ono7C8SgdCCyQxDMM%2BlP23tjP3fjPErpAGEY0p6xRO%2B5fEO4ttwaek%2B1EXp#'

request_url = 'http://218.19.164.168/DemoSpring/list?brchno=13500000001&%s' % random.random() + ''
print 'http://218.19.164.168/DemoSpring/list?brchno=13500000001&0.998463784434632'

print request_url
#
# urlobj = urllib.urlopen(request_url)
# content = urlobj.read()
#
# print content