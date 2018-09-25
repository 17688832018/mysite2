from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse
from cmdb import models
from cmdb.models import Test
import sys
# Create your views here.
"""
业务逻辑模块：响应和请求
将应用mysite2的URL index指向了应用cmdb的views中的index()函数，
他能接受用户请求，并返回一个字符串
"""

# sys.setdefaultencoding('utf8')
# 自定义列表，用来返回给页面
# user_list=[
#     {"user":"jack","pwd":"123456"},
#     {"user":"tom","pwd":"1234"},
# ]
# def index(request):  # 必须有，他封装了用户请求的所有内容
#     if request.method=="post":
#         # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
#         test1 = Test.objects.get(id=1)
#         # 删除id=1的数据
#         # test1.delete()
#         test1.name ='google'
#         test1.save()

        # 另外一种方式
        # Test.objects.filter(id=1).update(name='Google')
        # 修改所有的列
        # Test.objects.all().update(name='Google')
        # 另外一种方式
        # Test.objects.filter(id=1).delete()
        # 删除所有数据
        # Test.objects.all().delete()
        # return HttpResponse("<p>修改成功</p>")

        # username=request.POST.get("userName",None)
        # password=request.POST.get("passWord",None)
        # 添加数据到数据库
        # models.UserInfo.objects.create(user_name=username,user_pwd=password)
        # 从数据库中读取所有数据
        # user_list=models.UserInfo.objects.all()

        # temp={"user":username,"pwd":password}
        # user_list.append(temp)
        # print(username,password)

        # context = {}
        # context['hello'] = 'Hello World!'
        # return render(request, 'hello.html', context)
    # request.GET
    # return HttpResponse("Hello World!")
    # 不能直接返回字符串，必须用HttpResponse()包裹，这是django的规则
    # return render(request,"index.html",{"data":user_list})  # 返回一个页面时用render(),返回一个字典会被对应的html使用

# 返回给表单 （就是response方法）
def def_search_form(request):
    return render_to_response('index_get.html')  # 将响应返回给页面
# 处理请求数据 （就是doGet方法）
def def_search_get(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message ='你搜索的内容为;'+request.GET['q']
    else:
        message='你提交了空表单'
    return HttpResponse(message)
def def_search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,"index_post.html",ctx)

