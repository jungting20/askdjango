
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post,Comment,Tag


#단 한번만 등록 언레지스터도있음
#등록법 1
#기본모든 컬럼을 줌

#admin.site.register(Post)

#등록법2 커스터마이징하는법
#admin.ModelAdmin 상속받으면됨
#이거하면 진짜 게시판처럼나옴 admin 사이트페이지가 ㅋㅋㅋ
#이게좀더 세련됨!
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','status','created_at','updated_at']

    #이걸해주게되면 post에 포스팅들에 대해 체크박스 체크한다음 액션으로 액션 취하게할수있음
    #그니까 속성을 바꿔준다 이거지
    actions = ['make_published','make_draft']

    #컬럼을 추가하고 보여주고 싶은 컬럼명을 함수로한다음
    #그것을 추가해줌
    #적용후 함수의 이름을 list_display에 적용해줘야함
    #두번쨰인자는 그 모델의 인스턴스임!
    def content_size(self,post):
        #post 인스턴스에 content 필드 접근1
        #html 태그넣고 싶으면 maek_safe 함수 쓰면됨
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    #와 이러면 변경도됨 ㅋㅋㅋㅋ
    content_size.short_description = '내용글자수'
    #이건 액션임 모든 액션의 첫번쨰인자는 request 두번쨰인자는 쿼리셋임
    def make_published(self,request,queryset):
        updated_count = queryset.update(status = 'p') #이건 queryset에 update 함수를 썻음 그니까 데이터베이스에 업데이트
        self.message_user(request,'{}의 포스팅을 Published상태로 변경'.format(updated_count)) #장고의 기본은 메세지 프레임웍을 쓴거임
    make_published.short_description = 'Published status 를 이걸로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')  # 이건 queryset에 update 함수를 썻음 그니까 데이터베이스에 업데이트
        self.message_user(request, '{}의 포스팅을 draft상태로 변경'.format(updated_count))
#admin.site.register(Post,PostAdmin)
#이렇게도하고

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['names',]



