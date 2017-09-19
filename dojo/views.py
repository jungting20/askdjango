from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mysum(request,number):
    # request:HttpRequest
    #int('')이건 오류가 남 이걸 해결위해 저걸해준거임 저게 거짓이면 0으로
    result = sum(map(lambda s : int(s or 0),number.split("/")))
    return HttpResponse(result)

def hello(request,name,age):

    return HttpResponse('hello'+name+age)


