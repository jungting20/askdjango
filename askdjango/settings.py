"""
Django settings for askdjango project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r@5p8b%5u&9-_y@bftlhc$qlube33qe!1bkx55l$94u*vumyn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# 이걸로 도메인 지정할 수 있음
# 이렇게 별로 두면 다 접속 하게 할 수 있음
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar', #디버그툴바
    'blog',
    'dojo',
    'accounts',
    'bootstrap3', #pip install django-bootstrap3 해서 설치
    'imagekit' #pip install django-imagekit 썸네일 도와줌

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', #디버그툴바
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'askdjango.urls'



#Django Template Loader
#여러가지가 있지만 가장 중요한건 app_directories.Loader 과 filesystem.Loader 존재
#템플릿 디렉토리가 있을 후보 디렉토리 리스트를 작성 장고 서버 초기 시작시에만 1회 작성됨





TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #여기가 읽는게 filesystem.Loader 이거로 읽음
        'DIRS': [os.path.join(BASE_DIR,'askdjango','templates'),]
        #앱 아래 templates파일들은 APP_DIRS True로 줬기때문에
        #템플릿 리스트별로 다들어감 그러나 내가 만든 최상위 레이아웃은 프로젝트 앱 아래있는게 아니니 따로 지정해 줘야한다
        #템플릿이름들은 중복되면 안됨 리스트만들어서 위부터 찾아서 내려오므로 겹치면 다른 템플릿이 나올 수도 있음
        #그래서 앱/templates/앱/*.html 이런식으로 만들어주는거임 앱은 유일해야함
        #스태틱도 보통 같은경로를씀
        ,
        #app_directories.Loader 을 사용하겠단소리임 True가
        #앱아래 templates를 두고 거기다 html을 넣겠다 이거
        'APP_DIRS': True,#이걸 True 로 주게되면 앱아래 templates 경로까지는 무조건 찾음
        'OPTIONS': {
            #요것이 메세지를 내보내 주는거임 'messages':message 뭐 이런식으로 보내줌 템플릿에
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'askdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/



#템플릿과 같음 static가 들어가있는 모든 경로를 조사해서 리스트를 작성함
#askdjango/static와 blog/static이 리스트에 작성되겠지
#http://localhost:8000/static/style.css 여기로 요청 떄리면 askdjango/static/style.css
#http://localhost:8000/static/blog/style.css 여기로 요청 때리면 askdjango/static/blog/style.css 로 왔다가
#없으면 그 다음 후보인 blog/static/blog/style.css 여기를 확인함
#이제 이해갔다
#결론 static 가 들어가는 모든 후보 리스트를 작성함 서버 시작시에
#1.askdjango/static 2.blog/static 이렇게 여기서 앞 askdjango는 프로젝트 askdjango/askdjango 임
#그러니 blog와 루트레벨이 같음
#저렇게 후보가 두개 작성되면 /static/를 제외한 뒷 주소를 모두 후보 리스트에 붙여보면서 있을때 까지 찾는다
#이것이 장고의 클라스 템플릿도 마찬가지임
#/static/ 이건 static_url 이부분 여길바꾸면 다르게 로딩해줘야함 하지만 {% load static %} 로 임포트하고
#{% static 로쓰면 항상 setting.py에 있는 값으로 해줌 ㅋ
#이제 이해가 갔네 이게 정답
#이 모든것은 개발서버에서만 작동 실서비스에서의 웹서버는 정적파일들의 경로를 전혀 알지 못함
#그래서 모아주는 거임 영혼까지

#manage.py runserver 이건 개발서버임
#지금 이 static 이 설정들은 다 개발서버에서만 사용함 static는 사실 아파치나 엔진엑스로 옮겨야함 ㅋ
#배포서버는 또 다름 uwsgi 뭐 이런거쓰는듯

#배포시에 collectstatic 로 모아진 파일을 서버에 두고
#static_url을 그 서버의 경로로 바꿔줌
#그러면 나는 개발시에 이미 {% load static %}
#{% static blog/style.css 뭐 이런식으로 다 해뒀으니 여기만 바꾸면 자동 적용됨 ㅋ
#멋있구만 django
#static pdf 에 nginx 설정 간단하게 예시 나와있음
STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'askdjango','static')
    #최상위 밑에 static 를 두는게 좋긴함
    #BASE_DIR = askdjango까지
    #조인으로 /askdjango/static/
    #이걸 해주는 이유 디폴트로 앱 아래에있는 static는 다 찾지만 설정 파일들이있는 askdjango는 찾지 않기때문에 요걸로 등록
    #해주는 거임 템플릿도 마찬가지
]
#STATIC_ROOT는 개발당시에는 무의미함
#이건 collectstatic 명령어를 사용할 시 모아주는 그 경로임 ㅋ 이걸 nginx 나 아파치에 알려주는 거지
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'mediafiles') #파일은 여기에 저장함
#디비에는 경로를 저장
#static fildes와 다르게 개발서버에서 서빙 미지원함
#static 는 별도 설정없이 해도됨
#그래서 보통 룰을 추가해서 개발함 편하게 하려고



INTERNAL_IPS = ['127.0.0.1'] #디버그툴바용

#디버그 툴바는 해당 템플릿에 <body>태그가 있어야만 주입이된다

from django.contrib.messages import constants

MESSAGE_LEVEL = constants.DEBUG #지금부터 debug 레벨의 messages를 남길 수 있음 디폴트는 나오지 않게 설정 되어있음
MESSAGE_TAGS = {constants.ERROR:'danger'} #message.error 이걸 danger로 바꾼거임


