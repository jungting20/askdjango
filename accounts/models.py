#account/models.py
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings


class Profile(models.Model):

    # user = models.OneToOneField(User) #그니까 이렇게하면 객체하나에 user하나만 들어가게 할수있음
    user = models.OneToOneField(settings.AUTH_USER_MODEL) #이렇게 하는 이유는 AbstractUser 이걸 상속받아서 나만의 유저모델을
    #만들고 싶으면 다 바꿔줘야함 하지만 저렇게 참조해주면 저 값만 나만의 유저모델값으로 바꿔주면됨!
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


#여기서 중요한 사실!
#언제 데이터베이스에 접속해서 갖고오냐
#보통 q  = Profile.objects.first() 이렇게 인스턴스를 갖고올때 연결되어있는 User모델에 있는 값을 가져오는줄알지만
#사실 그게아님 q.user 이렇게 접근할 이시점에 데이터베이스를 불러온다
