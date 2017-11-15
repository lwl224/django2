# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/11/14'
"""
import os

import MySQLdb
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django1.settings")
django.setup()
import sys
import re
from books.models import *
from math import pi, sin, sqrt, cos, asin

reload(sys)
sys.setdefaultencoding('utf8')


def layuan():
    # 将正则表达式编译成Pattern对象
    pattern1 = re.compile(ur"\(([\u4e00-\u9fa5]*.*RRU.*)\)")
    pattern2 = re.compile(ur"（([\u4e00-\u9fa5]*.*RRU.*)\)")
    pattern3 = re.compile(ur"\(([\u4e00-\u9fa5]*.*RRU.*)）")
    pattern4 = re.compile(ur"（([\u4e00-\u9fa5]*.*RRU.*)）")
    celllist = Ltecell.objects.all()

    for cell in celllist:
        cellname = cell.cellomcname
        cellname = cellname.decode('utf8')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match1 = pattern1.findall(cellname)
        match2 = pattern2.findall(cellname)
        match3 = pattern3.findall(cellname)
        match4 = pattern4.findall(cellname)
        if match1:
            # 使用Match获得分组信息
            cell.customize9 = u'这是拉远小区'
            cell.save()
        if match2:
            # 使用Match获得分组信息
            cell.customize9 = u'这是拉远小区'
            cell.save()
        if match3:
            # 使用Match获得分组信息
            cell.customize9 = u'这是拉远小区'
            cell.save()
        if match4:
            # 使用Match获得分组信息
            cell.customize9 = u'这是拉远小区'
            cell.save()


def guifan():
    celllist = Ltecell.objects.all()

    for cell in celllist:
        cellname = cell.cellomcname
        cellname = cellname.decode('utf8')
        cellnamelist = cellname.split('_')
        if len(cellnamelist) > 3:
            enodebname = cellnamelist[0:2]
            isindoor = cellnamelist[2]
            cellinfo = cellnamelist[3:]
            s = ''.join([str(x) for x in enodebname])
            pattern = re.compile(ur"FLTE1800|FLTE2100|FLTE900|TLTE")
            match1 = pattern.findall(s)
            if match1:
                cell.customize7 = cell.customize7 + '_' + '包含需要字眼'
                if match1[0] == 'FLTE1800':
                    fpoint = int(cell.downfpoint)
                    if fpoint > 1450 and fpoint < 1750:
                        cell.customize7 = cell.customize7 + '_' + '双工模式与名称一致'
                    else:
                        cell.customize7 = cell.customize7 + '_' + '填错双工模式'
                if match1[0] == 'FLTE2100':
                    fpoint = int(cell.downfpoint)
                    if fpoint > 199 and fpoint < 555:
                        cell.customize7 = cell.customize7 + '_' + '双工模式与名称一致'
                    else:
                        cell.customize7 = cell.customize7 + '_' + '填错双工模式'
                if match1[0] == 'FLTE900':
                    fpoint = int(cell.downfpoint)
                    if fpoint > 3739 and fpoint < 3800:
                        cell.customize7 = cell.customize7 + '_' + '双工模式与名称一致'
                    else:
                        cell.customize7 = cell.customize7 + '_' + '填错双工模式'
                if match1[0] == 'TLTE':
                    fpoint = int(cell.downfpoint)
                    if fpoint > 40240 and fpoint < 40440:
                        cell.customize7 = cell.customize7 + '_' + '双工模式与名称一致'
                    else:
                        cell.customize7 = cell.customize7 + '_' + '填错双工模式'
            else:
                cell.customize7 = cell.customize7 + '_' + '不符合命名规范'
            pattern1 = re.compile(ur"H|F|W|Hin|Fin|Win|RRU")
            match2 = pattern1.findall(isindoor)
            if match2:
                cell.customize7 = cell.customize7 + '_' + '设备类型一致'
            else:
                cell.customize7 = cell.customize7 + '_' + '设备类型不一致'
            if len(cellinfo) > 1:
                cell.customize7 = cell.customize7 + '_' + '双载波'

            cell.save()
        else:
            cell.customize7 = cell.customize7 + '_' + '不符合命名规范'
            cell.save()


def juli(clat, clon, rlat, rlon):
    juli1 = 6378.138 * 2 * asin(sqrt(
        pow(sin((clat * pi / 180 - rlat * pi / 180) / 2), 2) + cos(clat * pi / 180) * cos(rlat * pi / 180) * pow(
            sin((clon * pi / 180 - rlon * pi / 180) / 2), 2))) * 1000
    return juli1


def makedata():
    connect_dict = {
        'host': '127.0.0.1',
        'user': 'lwl224',
        'passwd': '123456',
        'port': 3306,
        'db': 'lwl224',
        'use_unicode': 'True',
        'charset': 'utf8'
    }
    conn = MySQLdb.connect(**connect_dict)
    cursor = conn.cursor()
    sql = "SELECT * FROM cell_pyh_view WHERE  customize9 != '这是拉远小区' ORDER BY physicalstationid DESC"
    n = cursor.execute(sql)
    map1 = {}
    for row in cursor.fetchall():
        if not map1.has_key(row[4]):
            map1[row[4]] = [row[0]]
        else:
            key1 = row[4]
            vel1 = row[0]
            list1 = map1[key1]
            list1.append(vel1)
            map1[row[4]] = list1
    map2 = map1


makedata()
