# -*- coding: utf-8 -*-
"""
__author__ = 'lwl224'
__mtime__ = '2017/11/8'
"""
import sys

import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404


reload(sys)
sys.setdefaultencoding('utf8')

def hello(request):
    return HttpResponse("Hello world")


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
