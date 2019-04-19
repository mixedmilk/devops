# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import urls
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',)),
    # url(r'^snippets/$', views.snippet_view),
    # url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/$', views.SnippetList.as_view()),
    # url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail),
    # url(r'^snippets/(?P<pk>\d+)/$', views.snippet_detail2),
    url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)