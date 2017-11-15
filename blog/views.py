# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    blog_list = BlogsPost.objects.order_by('title')
    return render_to_response('management/index.html', {'blog_list': blog_list})
