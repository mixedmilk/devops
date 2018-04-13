from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'login',views.login),
    url(r'welcome',views.welcome),
    url(r'logout',views.logout_view),
]