"""dustmq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
"""
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(
        r'^login/$',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'blog/login.html'
        }
    ),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^list/$', views.post_list_view, name='list'),
    url(r'^write/$', views.write_post_view, name='write_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail_view, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete_view, name='post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/update/$', views.post_update_view, name='post_update'),
    url(r'^post/(?P<pk>[0-9]+)/newcomment/$', views.new_comment_view, name='new_comment'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove_view, name='comment_remove'),
    url(r'^mypage/$', views.mypage_view, name='mypage'),
    url(r'^mypage/changeavatar/$', views.change_avatar_view, name='change_avatar'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^signout/$', views.signout_view, name='signout')

]

app_name= 'blog'