from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


#포스팅에대한 내용을 볼건데 그 포스팅이 없는 것에 접근할때는 무조건 404로 리턴해줘야함
#500에러가아님 하지만 처리해주지 않으면 500에러 발생
#그래서 get_object_or_404 를 쓰거나 예외처리해줘야한다


def post_list(request):
    qs = Post.objects.all() #<<이시점에는 데이터베이스 접속이 이루어지는게아님
    #이것의 매핑은 blog/templates/blog/post_list.html

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request,'blog/post_list.html',{
        'post_list':qs,
        'q':q
    }) #<< 이시점에 접속이 이루어짐


#무조건 get_object_or_404 ㄱㄱㄱ
def post_detail(request,id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post,id=id)
    return render(request,'blog/post_detail.html',{
        'post':post
    })


