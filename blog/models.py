from django.db import models
from django.forms import ValidationError
import re
# Create your models here.
from django.utils.datetime_safe import datetime


def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)$',value):
        raise ValidationError("Invalid LngLat Type")

#프로젝트를 만들자마자 migrate 하면 어드민과 유저모델이 디폴트로 생성
#migrate appname zero 이렇게 하게되면 모든 마이그레이션을 취소함!!
#showmigrations blog 로 적용 미적용 알수있다
#블랭크옵션,널옵션을 주지않으면 이건 필수필드이므로 디폴트값을 정해줘야함
#마이그레이트를 수행하면 디폴트값 정해달라고 나옴 이미 들어있는 값들에 넣어줄 값들
#그걸 말하는 거지

class Post(models.Model):
    authon = models.CharField(max_length=20,default='test')
    title = models.CharField(max_length=100
    ) #html select 를 만들어줌 choices 옵션의 힘
    content = models.TextField(blank=True,null=True)
    lnglat = models.CharField(max_length=50,blank=True,validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

