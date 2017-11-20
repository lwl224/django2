# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/11/9'
"""

import sys
import urllib
import urllib2
import cookielib
import time
import datetime
import os

reload(sys)
sys.setdefaultencoding('utf8')

start = time.clock()
url_cell = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00805_dataList.action'  # 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00805_dataList.action?objectTypeId=L00805&_dc=1492048145390'
para_dict_cell = {
    'export': "true",
    'key': str,
    'isHighWay': "0",
    'collectType': "0",
    'provinceId': "110",
    'cityId': "11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014",
    'districtId': "",
    'vendorId': "",
    'sysType': "",
    'lcName': "",
    'btsId': "",
    'localcell': "",
    'date': "2017-04-12",
    'flag': "normal",
    'start': "0",
    'limit': "25",
    'page': "1"
}
url_rru = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00862_dataList.action'
para_dict_rru = {
    'export': 'true',
    'key': 'maintain_query_1492053585139',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'btsId': '',
    'flag': 'normal',
    'objectTypeId': 'L00862'
}
url_traffic1 = 'http://10.245.0.91:10101/wonop/wonop/perf/exportDirect.action'
para_dict_traffic1 = {
    'coutnerInfos': '[{"counterId":"LC0068050220376","lcName":"\u7a7a\u53e3\u4e0a\u884c\u4e1a\u52a1\u6d41\u91cf(MByte)","leaf":true,"checked":false,"statType":"\u516c\u5f0f"},{"counterId":"LC0068050220380","lcName":"\u7a7a\u53e3\u4e0b\u884c\u4e1a\u52a1\u6d41\u91cf(MByte)","leaf":true,"checked":false,"statType":"\u516c\u5f0f"}]',
    'levelId': 'L00805',
    'toLevelId': 'L00805',
    'netType': '4',
    'vendorId': '0',
    'timeRange': '{"period":"8","timeList":["2017-4-01 00:00:00","2017-4-02 00:00:00"]}',
    'toPeriod': '8',
    'neRange': '{"targetlevel":"cell","selecttype":"1","servicetype":"","neranges":[{"oids":"\'11001\'","lcnames":"\'\u5357\u5b81\'","level":"city","cityid":"11001"},{"oids":"\'11002\'","lcnames":"\'\u67f3\u5dde\'","level":"city","cityid":"11002"},{"oids":"\'11003\'","lcnames":"\'\u6842\u6797\'","level":"city","cityid":"11003"},{"oids":"\'11004\'","lcnames":"\'\u68a7\u5dde\'","level":"city","cityid":"11004"},{"oids":"\'11005\'","lcnames":"\'\u5317\u6d77\'","level":"city","cityid":"11005"},{"oids":"\'11006\'","lcnames":"\'\u9632\u57ce\u6e2f\'","level":"city","cityid":"11006"},{"oids":"\'11007\'","lcnames":"\'\u94a6\u5dde\'","level":"city","cityid":"11007"},{"oids":"\'11008\'","lcnames":"\'\u8d35\u6e2f\'","level":"city","cityid":"11008"},{"oids":"\'11009\'","lcnames":"\'\u7389\u6797\'","level":"city","cityid":"11009"},{"oids":"\'11010\'","lcnames":"\'\u767e\u8272\'","level":"city","cityid":"11010"},{"oids":"\'11011\'","lcnames":"\'\u8d3a\u5dde\'","level":"city","cityid":"11011"},{"oids":"\'11012\'","lcnames":"\'\u6cb3\u6c60\'","level":"city","cityid":"11012"},{"oids":"\'11013\'","lcnames":"\'\u6765\u5bbe\'","level":"city","cityid":"11013"},{"oids":"\'11014\'","lcnames":"\'\u5d07\u5de6\'","level":"city","cityid":"11014"},{"oids":"\'-1\'","lcnames":"\'\u5176\u5b83\'","level":"city","cityid":"-1"}],"checkedNodePaths":[["11001"],["11002"],["11003"],["11004"],["11005"],["11006"],["11007"],["11008"],["11009"],["11010"],["11011"],["11012"],["11013"],["11014"],["-1"]],"vendor":"0"}',
    'filterGroups': '[]',
    'sysTypes': '0',
    'provinceId': '110',
    'isBhFlag': '0',
    'busyFlag': '1',
    'selectType': '1',
    'sysType': '0'
}
url_enodeb = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00803_dataList.action'
para_dict_enodeb = {
    'export': 'true',
    'key': 'maintain_query_1510215114654',
    'collectType': '1',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'vendorId': '',
    'siteType': '',
    'btsName': '',
    'btsId': '',
    'flag': 'normal',
    'isHighWay': '0',
    'objectTypeId': 'L00803'
}
url_PhysicallStation = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00864_dataList.action'
para_dict_PhysicallStation = {
    'export': 'true',
    'key': 'maintain_query_1510216622957',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'lcName': '',
    'flag': 'normal',
    'objectTypeId': 'L00864'
}

url_antenna = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00863_dataList.action'
para_dict_antenna = {
    'export': 'true',
    'key': 'maintain_query_1510216914611',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'antManuId': '',
    'flag': 'normal',
}

url_bbu = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00861_dataList.action'
para_dict_bbu = {
    'export': 'true',
    'key': 'maintain_query_1510216914611',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'btsName': '',
    'flag': 'normal',
    'objectTypeId': 'L00861',
}
url_scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_L00903_dataList.action'
para_dict_scenes = {
    'export': 'true',
    'key': 'maintain_query_1510217419212',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'districtId': '',
    'sysType': 'null',
    'scene1': '01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18',
    'scene2': '0101,0102,0103,0104,0201,0202,0203,0204,0301,0302,0303,0304,0305,0401,0402,0403,0501,0502,0503,0504,0505,0601,0602,0603,0701,0702,0703,0704,0801,0802,0803,0804,0806,0807,0808,0809,0810,0901,0902,0903,0904,0905,0906,0907,0908,1001,1002,1003,1101,1102,1103,1201,1202,1301,1401,1501,1502,1503,1504,1505,1506,1507,1508,1509,1510,1511,1601,1602,1603,1701,1801',
    'sceneName': '',
    'sceneID': '',
    'flag': 'normal',
    'objectTypeId': 'L00903',

}
url_cell2scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_CON02_dataListCon2.action'
para_dict_cell2scenes = {
    'export': 'true',
    'key': 'maintain_query_1510218017331',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'netType': '',
    'scene1': '',
    'scene2': '',
    'sysType': 'null',
    'SCENE_ID': '',
    'sceneID': '',
    'CELL_ID': '',
    'CELL_NAME': '',
    'flag': 'normal',
    'queryType': '0',
    'objectTypeId': 'CON02',
}
url_construction2scenes = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_query_CON01_dataList.action'

url_delete = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/query/config_maintain_property_delete_nocheck.action'
para_dict_delete = {
    'objectTypeId': 'L00805',
    'objectIds': '110.703882.5',
    'selectedDelTypes': 'L00863,L00862,CON02'
    # selectedDelTypes: antenna->L00863,bbu->L00861,rru->L00862,PhysicallStation->L00864,cell2scenes->CON02,construction2scenes->CON03,

}

para_dict_construction2scenes = {
    'export': 'true',
    'key': 'maintain_query_1510218386472',
    'provinceId': '110',
    'cityId': '11001,11002,11003,11004,11005,11006,11007,11008,11009,11010,11011,11012,11013,11014',
    'scene1': '',
    'scene2': '',
    'sysType': 'null',
    'SCENE_ID': '',
    'sceneID': '',
    'CONSTRUCT_SCENE': '',
    'CONSTRUCT_GRIDTYPE': '',
    'CONTRUCT_GRIDNAME': '',
    'flag': 'normal',
    'queryType': '0',
    'objectTypeId': 'CON01',
}


def loading():
    url = 'http://10.245.0.91:10101/wonop/login_check.action'
    cookie = cookielib.MozillaCookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
    urllib2.install_opener(opener)
    para_dict = {'userId': "chenhb35", 'password': "123"}
    para_data = urllib.urlencode(para_dict)
    req = urllib2.Request(url, para_data)
    res = urllib2.urlopen(req)
    cookie.save('cookie.txt', ignore_discard=True, ignore_expires=True)


def getexcel(url, para_dict, name):
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
    urllib2.install_opener(opener)
    timeflag = time.time()
    timeflag1 = str(timeflag).split('.')[0]
    str1 = 'maintain_query_' + timeflag1
    if name != 'traffic':
        para_dict['key'] = str1
    para_data = urllib.urlencode(para_dict)
    req = urllib2.Request(url, para_data)
    res = urllib2.urlopen(req)
    if os.path.exists('./' + name[:5]) == False:
        # print os.getcwd()
        os.makedirs('./' + name[:5])
    if ('traffic1' in name) == False:
        with open(name[1:] + '.xlsx', 'wb') as w_fh:
            w_fh.write(res.read())
    else:
        with open(name[1:] + '.csv', 'wb') as w_fh:
            w_fh.write(res.read())


def delete_data_cell(url, para_dict):
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
    urllib2.install_opener(opener)
    timeflag = time.time()
    timeflag = str(timeflag).split('.')[0]
    str1 = 'maintain_query_' + timeflag
    para_dict['key'] = str1
    para_data = urllib.urlencode(para_dict)
    req = urllib2.Request(url, para_data)
    res = urllib2.urlopen(req)
    print res.msg


def modify_nocheck(para_dict):
    url = 'http://10.245.0.91:10101/wonop/wonop/config/maintain/detail/config_maintain_property_modify_nocheck.action'
    cookie = cookielib.MozillaCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0")]
    urllib2.install_opener(opener)
    timeflag = time.time()
    timeflag = str(timeflag).split('.')[0]
    str1 = 'maintain_query_' + timeflag+'000'
    para_dict['key'] = str1
    para_data = urllib.urlencode(para_dict)
    req = urllib2.Request(url, para_data)
    res = urllib2.urlopen(req)


def loop():
    date1 = '2017-11-14'
    str1 = '{"period":"8","timeList":["%s 00:00:00"]}' % (date1)
    print  str1
    # str2 = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    para_dict_traffic1['timeRange'] = str1
    # para_dict['date'] = yesterday
    para_dict_cell['date'] = date1
    # print  date1
    datestr = 'data'
    loading()
    getexcel(url_rru, para_dict_rru, '/%s/rru' % (datestr))
    getexcel(url_cell, para_dict_cell, '/%s/cell' % (datestr))
    getexcel(url_enodeb, para_dict_enodeb, '/%s/enodeb' % (datestr))
    getexcel(url_PhysicallStation, para_dict_PhysicallStation, '/%s/physicalstation' % (datestr))
    getexcel(url_antenna, para_dict_antenna, '/%s/antenna' % (datestr))
    getexcel(url_bbu, para_dict_bbu, '/%s/bbu' % (datestr))
    getexcel(url_scenes, para_dict_scenes, '/%s/scenes' % (datestr))
    getexcel(url_cell2scenes, para_dict_cell2scenes, '/%s/cell2scenes' % (datestr))

    # getexcel(url_construction2scenes, para_dict_construction2scenes, '/%s/construction2scenes' % (datestr))

    # getexcel(url_traffic1, para_dict_traffic1, '/%s/traffic1' % (datestr))
    end = time.clock()
    print str((end - start) / 60) + 'mins'


# loop()
# delete_data_cell(url_delete, para_dict_delete)
