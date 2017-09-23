from django.db import models
from django.forms import ValidationError
import re
# Create your models here.
from django.utils.datetime_safe import datetime



#주피터 노트북 설치법 알아야함!이게 쉘 편하게 쓸수있게해줌
#주피터 노트북으로 장고쉘 띄울수있다
#settiongs.py에 인스톨앱스에 django_extensions 추가
#아나콘다 파이선으로 했으면 주피터노트북 자동설치
#manage.py shell_plus --notebook


def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)$',value):
        raise ValidationError("Invalid LngLat Type")

#프로젝트를 만들자마자 migrate 하면 어드민과 유저모델이 디폴트로 생성
#migrate appname zero 이렇게 하게되면 모든 마이그레이션을 취소함!!
#showmigrations blog 로 적용 미적용 알수있다
#블랭크옵션,널옵션을 주지않으면 이건 필수필드이므로 디폴트값을 정해줘야함
#마이그레이트를 수행하면 디폴트값 정해달라고 나옴 이미 들어있는 값들에 넣어줄 값들
#그걸 말하는 거지

#Post.objects.filter(title__icontains='1',title__endswith = '3')
#Post.objects.filter(title__icontains='1').filter(title__endswith='3') 이 두개는 같은거임
#exclude(title__endswith='3')하면 됨
#그리고 이 모든것은 and 조건임 or 조건을 하고싶으면
#Q임포트 받고 Post.objects.filter(Q(title__icontains='1') | Q(title__endswith='3')) << or 조건
#쿼리셋.get()문법은 무조건 1개만 갖고옴 2개이상이면 에러발생 없어도 에러발생

#insert!!
#저장방법은 두가지가있음 model.objetes.create 이것과 model_instance.save()함수 둘다 insert 임
#update!!
#save()함수로 한번씩 요청보내는 쓰레기같은 방법과
#가급적이면 update로 사용
# queryset = model.objects.all()
# queryset = model.objectes.update(tags = 'python,django')라는 한번에 보내주는 훌륭한함수가있음
#delete!!
#이거도 같음 대신 이건 인스턴스도 delete고 opjects.delete() 이것도 같음
#웹의 속도는 결국 데이터베이스가 결정 그러니 opjects.delete() 추천 언어의종류는 사실상 거의 상관없음
#django-debug-toolbar 을 사용하자




#Meta 정보로 기본 정렬 지정가능
class Post(models.Model):
    #이런식으로해주면 두번쨰 인자값이 들어감 앞에는 그 매핑인듯하다
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
        ('w','Withdrawn')
    )
    authon = models.CharField(max_length=20,default='test')
    title = models.CharField(max_length=100
    ) #html select 를 만들어줌 choices 옵션의 힘
    content = models.TextField(blank=True,null=True)
    lnglat = models.CharField(max_length=50,blank=True,validators=[lnglat_validator])
    #이러고 내가 makemigrations 하니까 나머지 값들에 status 필드에 뭘 넣어줄지 정하라해서
    #'d' 로했더니 'Draft'가 들어갔음!
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title



