
from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
def min_length_3_validator(value):
    if len(value) < 3 :
        raise forms.ValidationError('3글자 이상 입력해주세요')



class Post(models.Model):
    title = models.CharField(max_length=100,validators=[min_length_3_validator]) #이렇게 해주는거임
    content = models.TextField()
    user_agent = models.CharField(max_length=200)#브라우저 종류를 넣을거임
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updatedd_at = models.DateTimeField(auto_now=True)




class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A','A서버'),
                                       ('B','B서버'),
                                       ('C','C서버'),
                                   ))
    #디폴트 밸리데이터
    username = models.CharField(max_length=20,validators=[MinLengthValidator(3)])

    class Meta:
        #어떤필드가 같이 유니크해야하는지
        #이건 밸리데이터를 내부적으로 사용함
        #테스트하면 Game user의 Server name 또한 Username 은/는 이미 존재합니다. 이렇게 에러메세지가 뜬다
        unique_together = [
            ('server_name','username')
        ]

