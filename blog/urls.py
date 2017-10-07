from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.post_list,name= 'post_list'),
    url(r'^(?P<id>\d+)$',views.post_detail,name='post_detail'),
    url(r'^new/$',views.post_new,name='post_form'),
    url(r'^(?P<pk>\d+)/edit/$',views.post_edit),#pk로주면 디폴트값으로 pk인자받아서 굳이 구현하지않아도 된다,
    url(r'^(?P<pk>\d+)/delete/$',views.post_delete)
]