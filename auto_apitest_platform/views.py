from django.http import HttpResponse
from django.shortcuts import render
import datetime
def hello(request):
    return HttpResponse("Hello world!")

def index1(request):
    views_dict = {'views_dict':'Test DJango'}
    context = {}
    context['name'] = views_dict
    return render(request,'index1.html',context)

def index2(request):
    views_list = ['测试1','测试2','测试3']
    context = {}
    context['views_list'] = views_list
    return render(request,'index2.html',context)

def time(request):
    now = datetime.datetime.now()
    return render(request,'time.html',{"time":now})

def jump(request):
    views_str = "<a href= 'https://hongcyu.cn'>点击跳转</a>"
    return render(request,'jump.html',{"views_str":views_str})