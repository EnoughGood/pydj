"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    //Django项目的URL声明
    匹配符含义
    r 字符串有前面加“ r ”是为了防止字符串中出现类似“\t”字符时被转义。
    ^ 匹配字符串开头；在多行模式中匹配每一行的开头。^abc abc
    $ 匹配字符串末尾；在多行模式中匹配每一行末尾。abc$ abc
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^accounts/login/$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^sreach_name/$', views.sreach_name),
    url(r'^guest_manage/$', views.guest_manage),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),
    url(r'^logout/$', views.logout),

]
