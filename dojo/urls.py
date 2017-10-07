from django.conf.urls import url,include
from django.contrib import admin
from . import views,views_cbv
urlpatterns = [
    #하나에서 여러개의 값을 받고 싶으면 음
    #이렇게하면 슬러쉬를 두번쓸 가능성도 있음
    #해결법은 람다임
    url(r'^new/$',views.post_new),
    url(r'^(?P<id>\d+)/edit/$',views.post_edit),
    url(r'^(?P<pk>\d)/$',views.post_detail),#클래스(DetailView) 뷰를 쓰기위해 pk로바꿔줌 이러면 인자 지정해주지 않아도 된다
    url(r'^sum/(?P<number>[\d/]+)/$',views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>\d{1,2})/$',views.hello),
    url(r'^list1/$',views.post_list1),
    url(r'^list2/$',views.post_list2),
    url(r'^list3/$',views.post_list3),
    url(r'^excel/$',views.excel_download),

    url(r'^cbv/list1/$',views_cbv.post_list1),
    url(r'^cbv/list2/$',views_cbv.post_list2),
    #url(r'^cbv/list3/$',views_cbv.post_list3),
    #url(r'^cbv/excel/$',views_cbv.excel_download)
]
