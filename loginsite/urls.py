from django.conf.urls import url
from . import views
app_name = 'loginsite'


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url('^refresh/', views.captcha_refresh, name='captcha_refresh'),
]