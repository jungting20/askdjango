from django.db import models
from django.forms import ValidationError
import re
from django.conf import settings
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import Thumbnail
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
# queryset = model.objectes.all().update(tags = 'python,django')라는 한번에 보내주는 훌륭한함수가있음
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
    title = models.CharField(max_length=100
    ) #html select 를 만들어줌 choices 옵션의 힘
    content = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True,upload_to='blog/post/%Y/%m/%d')#업로드시 저장경로 결정
    #photo를 ProcessedImageField 이걸로 만듬
    #ProcessedImageField(blank=True,upload_to='blog/post/%Y/%m/%d',processors=[Thumbnail(300,300)],format='JPEG',options={'quality':60}# )
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[Thumbnail(300,300)],
                                     format = 'JPEG',
                                     options={'quality':60}) #원본 유지하면서 썸네일까지 같이 만듬
    #원본유지하기 싫으면 ProcessedImageField

    lnglat = models.CharField(max_length=50,blank=True,validators=[lnglat_validator],null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL) #외래키를 추가하고 makemigration 하려하면 당연히 
    #디폴트값 뭐로할거냐 이렇게 나옴 이상태에서는 int 로 적어줘야함 왜냐하면 외래키로 필드만들면 필드명_id 로 만들어지기 때문이다!!!!!!!!
    #지금 user로 마이그레이션 했으니 user_id 로 만들어진다!
    #사실상 외래키필드는 int임 ㅋ
    status = models.CharField(max_length=1,choices=STATUS_CHOICES) #이러고 내가 makemigrations 하니까 나머지 값들에 status 필드에 뭘 넣어줄지 정하라해서
    #'d' 로했더니 'Draft'가 들어갔음!
    tag_set = models.ManyToManyField('Tag',blank=True) #문자열로 지정해주자 웬만하면 대부분의 관계 필드정해줄때는 문자열로 ㄱㄱ
    #같은 앱이 아닐경우 'auth.Tag' 이런식으로 앱이름을 써주면됨
    #manytomany 필드는 블랭크옵션 주는게 낫다
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


    #필히 사용하자
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.id])#리턴값은 문자열 /blog/10 이런식으로 만들어줌
        #get_absolute_url 이함수명에 리턴값은 url 형식의 문자열로 리턴만 해주면 그리로 리다이렉트 침
        #이걸 해주게되면 resolve_url(post) 이런식으로 사용할수있게됨
    #resolve_url 함수는 가장먼저 저거 부터 찾음 get_absolute_url 부터 찾음
    #redirect는 내부적으로 resolve_url을 사용 하므로 redirect(post) 이렇게 쓰면됨 그럼 /blog/10/ 으로 이동
    #여기에 등록이 되어있으니까 저렇게 쓸수있는거임 안그러면 어딘지 어떻게알고감

    #이것의 엄청난 활용은 나중에 배울 CreateView,UpdateVIew등에서 내용 수정시 success_url 을 사용해서 이동시켜줘야하는데
    #이게 있으면 그냥 알아서 이동함 유알엘 찾아서 ㅋ

class Comment(models.Model):
    #intger 필드 Post의 id 값이 저장
    #필수 필드지 이렇게 해주면
    #Post 객체를 post로 지정해주면 알아서 id 값으로 저장이됨 save시에
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#manytomanyto 관계는 생성을하게되면 rdbms특성상 가운데 연결하는 다리역할을하는 데이터베이스를 하나 생성해야한다
#그게 _set이라는 테이블로생성됨
#이걸 접근할때 Post.objects.filter(필드명__컬럼명 = 'django')
#이걸 접근할때 Post.objects.filter(필드명__컬럼명__in = ['django','askdjango'])
#이걸 접근할때 Post.objects.filter(tag_set__컬럼명__in = ['django','askdjango'])
#이런식으로 __in 으로도 접근가능하다
class Tag(models.Model):
    names = models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.names

#아하 기본으로 user모델을 제공함 이걸 내가 바꿀수는없어
#그래서 이거랑 1:1로 대응되는 모델을 하나 생성하는거지
#related_name의 중요성!
#post = Post.objects.first() 하나얻어와서
#Comment.objects.filter(post = post) <방법1
#post.comment_set.all() << 이것이 방법2

#방법2를 설명하자면 1:N의 관계에서 1측.참조할모델소문자_set.all() 하면 전부가져옴 이게포인트
#그냥 쉽게 생각 1측에 셋되어있는 코멘트모델을 가져와라 뭐 이런거임 사실상

#외래키 지정시 속성에 related_name을 지정해주면 접근할때 이름을 바꿀 수있음 post.comment_set.all()
#comment_set 이부분을 지정해준다 이거지 ㅇㅋ? 지정해주지 않으면 디폴트는 저거임



#manyTomanyfield
#post = Post.objects.first()
#tag1 = Tag.objects.all()[0]
#tag2 = Tag.objects.all()[1]
#tag3 = Tag.objects.all()[2]
#tag_qs = Tag.objects.filter(name__endswith('django'))



#추가하는법
#post.tag_set.add(tag1) 이런식이거나
#post.tag_set.add(*tag_qs) 쿼리셋은 이런식으로 해줘야함! <이것이 가장 유용하다 크큭


#갯수 카운트하는 2가지 방법
#len(Post.objects.all()) 이방법과
#Post.objects.all().count()) 이방법이있음 성능차이는 count() 이게 더 월등함!!! 이건 쿼리에서 끊고 위에는 다 받아와서 또 읽음



#datetime 인스턴스는 strftime()함수로 포맷할수있음











