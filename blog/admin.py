from django.contrib import admin

from .models import Post

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
    list_display = ['id','title','created_at','updated_at']
#admin.site.register(Post,PostAdmin)
#이렇게도하고

