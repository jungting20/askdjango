from django.db import models
from django.forms import ValidationError
import re
# Create your models here.

def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)$',value):
        raise ValidationError("Invalid LngLat Type")


class Post(models.Model):
    title = models.CharField(max_length=100,choices=(
        ('제목1','제목1 레이블'),
        ('제목2','제목2 레이블'),
        ('제목3','제목3 레이블'),
    )) #html select 를 만들어줌 choices 옵션의 힘
    content = models.TextField()
    lnglat = models.CharField(max_length=50,blank=True,validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

