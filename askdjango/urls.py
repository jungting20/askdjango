"""askdjango URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.shortcuts import redirect
from askdjango import settings

#def root(request):
 #   return redirect('blog:post_list')


urlpatterns = [
    #url(r'^$',root,name='root'), 이거보다 세련된 방법은 강력한힘 람다!
    url(r'^$',lambda r:redirect('blog:post_list'),name='root'),
    url(r'^admin/', admin.site.urls),
    #여기의 네임스페이스들은 url reverse에 사용됨 그리고 이걸 사용하는순간 url reverse를 사용하는 곳에는 항상
    #네임 스페이스를 저ㅜ야한다 {% url 'blog:post_list' 뭐 이런식으로 %} 그전에는 post_list 만 사용했음
    #url reverse 란함수는 문자열을 리턴해줌 그니까 url형식으로 바꿔준다보면됨
    #그냥 django.shortcut에 있는 reverse_url 이걸 쓰자 이게 더 업그레이드된 함수임
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^dojo/',include('dojo.urls',namespace='dojo')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),


]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/',include(debug_toolbar.urls)),
    ]
