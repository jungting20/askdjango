from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    #하나에서 여러개의 값을 받고 싶으면 음
    #이렇게하면 슬러쉬를 두번쓸 가능성도 있음
    #해결법은 람다임
    url(r'^sum/(?P<number>[\d/]+)/$',views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>\d{1,2})/$',views.hello),
]
