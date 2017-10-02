from django.contrib import admin

#어드민에 등록하게 되면 모델폼으로서 동작함
from .models import Post,GameUser
# Register your models here.

admin.site.register(Post)

admin.site.register(GameUser)