from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^$',views.post_list),
    url(r'^(?P<id>\d+)$',views.post_detail),

]