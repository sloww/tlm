from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^rebuild/(?P<che_jian_num>\d+)/$', views.rebuild, name='rebuild'),
    url(r'^(?P<che_jian_num>\d+)/(?P<gong_qu_num>\d+)/$', views.get_gongju_list, name='get_gongju_list'),
]
