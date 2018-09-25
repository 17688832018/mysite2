"""mysite2 URL Configuration
 URL路由文件
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from cmdb import views  # 导入app cmdb的view文件


urlpatterns = [
    # url!!!!!!!!不用path
    # 路径都是方法不是文件
    url(r'^def_search_form/$', views.def_search_form),  # 即声明response路径
    url(r'^def_search_get/$', views.def_search_get),  # 即声明doGet路径
    url(r'^def_search_post/$', views.def_search_post),  # 即声明doPost路径
    # 激活自带的管理工具
    url(r'^admin/', admin.site.urls),
]