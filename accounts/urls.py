from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .forms import LoginForm
urlpatterns = [
    url(r'profile/$',views.profile,name = 'profile'),
    url(r'signup/$',views.signup,name='signup'),
    url(r'login/$',auth_views.login,kwargs={
        'template_name':'accounts/login_form.html',
        'authentication_form':LoginForm,#클래스 넘겨줘도 됨
    }),#디폴트 넥스트페이지는 accounts/profile로 감
    #html에서 요청 줄때 ?{% url 'logout' %}?next = {{ request.path }} 하게되면 현재 경로로 이동
    url(r'logout/$',auth_views.logout,kwargs={
        'next_page':settings.LOGIN_URL
    },name='logout')
]