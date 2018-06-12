from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = [
#     url(r'^$', views.snippet_list),
#     url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    url(r'^$',views.SnippetList.as_view()),
    url(r'(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)