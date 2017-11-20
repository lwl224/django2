# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/11/9'
"""
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import django
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django1.settings")
    django.setup()
from books.models import Ltecell
import xlrd
import time


def foreachadd(list1, row):
    for nn in list1:
        if row[nn].strip() == '':
            row[nn] = 0.0
    return row


def loaddata(classname='Ltecell', filename='cell.xlsx', list1=[14, 15]):
    mm = sys.modules['books.models']  # 得到这个模块
    attstr = dir(mm)  # 得到属性的列表
    for str1 in attstr:  # 迭代之
        att = getattr(mm, str1)
        if str1 == classname:
            theObj = att
    time1 = time.time()
    with xlrd.open_workbook(filename) as data:
        print u"读取文件结束,开始导入!"
        time2 = time.time()
        table = data.sheet_by_index(0)  # 获取工作表
        time3 = time.time()
        n = 1
        x = y = z = 0
        WorkList = []
        for line in range(n,
                          table.nrows):  # nrows = table.nrows #行数 ncols = table.ncols #列数 print sh.row_values(rownum)
            row = table.row_values(line)
            if row:  # 查看行值是否为空
                # if (row[14] and row[15]).strip() == '':  # 判断该行值是否在数据库中重复
                #     if row[14].strip() == '':
                #         row[14] = 0.0
                #     if row[15].strip() == '':
                #         row[15] = 0.0
                row = foreachadd(list1, row)
                aa=theObj()
                WorkList.append(theObj().init1(row))
                y = y + 1  # 非重复计数
            else:
                z = z + 1  # 空行值计数
            n = n + 1
            if n % 999 == 0:
                theObj.objects.bulk_create(WorkList)
                WorkList = []
                # time.sleep(random.random())  # 让Cpu随机休息0 <= n < 1.0 s
                # print "导入成功一次!"
                # print '数据导入成功,导入' + str(y) + '条,重复' + str(x) + '条,有' + str(z) + '行为空!'
                # time4 = time.time()
                # print "读取文件耗时" + str(time2 - time1) + "秒,导入数据耗时" + str(time4 - time3) + "秒!"
        print n
        theObj.objects.bulk_create(WorkList)

def initialization():
    time1 = time.time()
    loaddata('Bbu', 'data/bbu.xlsx', [6, 7])
    loaddata('Enodeb', 'tilt/data/enodeb.xlsx', [33, 34])
    loaddata('Ltecell','tilt/data/cell.xlsx',[14,15])
    loaddata('Antenna', 'tilt/data/antenna.xlsx', [5, 6, 10, 11])
    loaddata('Cell2scenes', 'tilt/data/cell2scenes.xlsx', [0])
    loaddata('Scenes', 'tilt/data/scenes.xlsx', [8, 9, 14, 15])
    loaddata('Rru', 'tilt/data/rru.xlsx', [5, 6])
    loaddata('Physicalstation', 'tilt/data/physicalstation.xlsx', [6, 7])
    time2 = time.time()
    print "导入数据耗时" + str(time2 - time1) + "秒,"

initialization()