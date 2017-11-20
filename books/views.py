# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
# Create your views here.
from books.models import Book
from django.contrib import auth
from django.contrib.auth.models import User
from books.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tilt import loaddata


def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return render_to_response('search_form.html', {'error': True})

def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/index.html', content)
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/login.html', content)

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/signup.html', content)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))



def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/set_password.html', content)


def view_cell(request):
    user = request.user if request.user.is_authenticated() else None
    # category_list = Book.objects.values_list('category', flat=True).distinct()
    cell_list = Ltecell.objects.all()
    # cell_list =Physicalstation.objects.all()
    # test1 = cell_list[1]
    # print test1.bbuid
    # print test1.bbuname
    # print test1.bbuid
    query_category = 'all'
    paginator = Paginator(cell_list, 5)
    page = request.GET.get('page')
    try:
        cell_list = paginator.page(page)
    except PageNotAnInteger:
        cell_list = paginator.page(1)
    except EmptyPage:
        cell_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_book',
        # 'category_list': category_list,
        'query_category': query_category,
        'cell_list': cell_list,
    }
    return render(request, 'management/view_cell_list.html', content)


def initialization(request):
    loaddata.initialization()
    return HttpResponseRedirect(reverse('homepage'))