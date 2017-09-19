from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
# Create your views here.
from askdjango import settings

#django.views.generic
#뷰 사용패턴을 일반화시켜놓은 뷰의 모음
#.as_view()클래스함수를 통해 FBV를 생성해줌!!!
#아 기본 샘플구조는
#이런식으로 되어있음
#class SampleTemplateVIew(object):
 #   @classmethod
  #  def as_view(cls,template_name):
   #     def view_fn(request):
    #        return render(request,template_name)
     #   return view_fn


def mysum(request,number):
    # request:HttpRequest
    #int('')이건 오류가 남 이걸 해결위해 저걸해준거임 저게 거짓이면 0으로
    result = sum(map(lambda s : int(s or 0),number.split("/")))
    return HttpResponse(result)

def hello(request,name,age):

    return HttpResponse('hello'+name+age)


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>장고의 왕</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request,'dojo/post_list.html',{'name':name})


def post_list3(request):
    name = '공유'
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items':['파이선','장고'],
    },json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    'FBV:엑셀 다운로드 응답하기'
    filepath = 'c:/testman/aaaa.xlsx'
    #경로는재끼고 파일만 뽑아주는 거임
    #만약 같은경로에 있다면
    #filepath = os.path.join(settings.BASE_DIR,'aaaa.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath,'rb') as f:
        response = HttpResponse(f,content_type='application/vnd.ms-excel')

        response['Content-Disposition']='attachment; filename="{}"'\
            .format(filename)
        return response






