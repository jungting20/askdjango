
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
import os
from django.shortcuts import redirect
from dojo.models import Post
from dojo.forms import PostForm
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
from dojo.forms import PostForm




#유효성 검사 호출 로직
#is.valid()호출
#full_clean() 호출
#필드별 유효성 검사 수행하여 , 필드별 에러 체크
#특정필드.clean() 를 통해 Form/Model Field validators 수행
#form.clean_특정필드() 이거도 호출 둘다 호출 하는거임 그래서 이걸 오버라이드 하는구나 ㅋㅋ
#form.clean() 호출하여 , 다수 필드에 대한 에러 체크
#밸리데이션 에러가 발생되면 form.add_error을 통해 에러가 기록된다
#그러니까 이거의 핵심은 validationError로 에러를 발생 시켜도 되고, add_error로 에러를 내가 직접 등록해도됨
#같은 효과임 보통은 validationError 이걸로 많이함
#에러가 있으면 FALSE 리턴 없으면 True 리턴


#clean_필드명은 필드별 유효성검사
#clean 은 다수의 필드 검사 non 필드 에러로 분류
# 하지만 add.error함수를 통해 error 기록가능


#가급적이면 모든 validators 는 모델에 정의하고
#모델폼으로 가져 오자
#clean 을 쓰는 경우
#다수 필드값을 묶어서 유효성 검사가 필요할 때





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
    with open(filepath,'rb') as f: #with는 닫기까지 해줌 close 이거
        response = HttpResponse(f,content_type='application/vnd.ms-excel')

        response['Content-Disposition']='attachment; filename="{}"'\
            .format(filename)
        return response


#장고스타일 포스트쪽을 검사하고 나머지는 엘스로
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        #is_valid() 성공하면 True 리턴하면서 cleaned_data 딕셔너리에 정보들이 담김
        #실패하면 form.errors와 form.각필드.errors에 오류 정보를 저장
        if form.is_valid():
            #방법 1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # #방법 2
            # post = Post(title = form.cleaned_data['title'],content=form.cleaned_data['content'])
            # post.save()
            #
            # #방법 3
            # post = Post.objects.create(title = form.cleaned_data['title'],
            #                            content = form.cleaned_data['content'])

            #방법 4
            # post = Post.objects.create(**form.cleaned_data) #cleaned_data 라는 딕셔너리에 들어가니까


            #방법 5 거의 피니쉬 방법
            #폼에서 제공해주는 save() 함수를 오버라이드 해준다
            #이런게 가능한 이유는 is_valid() 를해주면 post.cleaned_data 딕셔너리가 생성되면서 값들이 담긴다
            #이걸 self.cleaned_data로 접근 가능하기 때문에 이걸 언팩해서 모델에 그냥 넣어주는거임
            #그럼 Post 에서는 언팩된거니까 title,content에 알아서 들어가게 된다
            #forms.py 오버라이드 좋음 ㅋㅋ 상당히 간결
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR'] #아이피 얻어오는 법
            post.save()
            return redirect('/dojo/')#그냥 네임스페이스쓰셈

    else:
        form = PostForm()
    return render(request,'dojo/post_form.html',{
        'form':form,
    })


def post_edit(request,id):
    post = get_object_or_404(Post,id=id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.ip =request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request,'dojo/post_form.html',{
        'form':form
    })