from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




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



