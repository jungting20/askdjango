from django.http.response import Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse,reverse_lazy
#포스팅에대한 내용을 볼건데 그 포스팅이 없는 것에 접근할때는 무조건 404로 리턴해줘야함
#500에러가아님 하지만 처리해주지 않으면 500에러 발생
#그래서 get_object_or_404 를 쓰거나 예외처리해줘야한다





#http://localhost:8000/blog/?page=2 이런식으로 페이지 넘어갈 수 있음!!
#모델명소문자_list 로 리스트로 접근가능
#디폴트 템플릿은 앱이름/모델명소문자_list.html ㅋ
# post_list = ListView.as_view(model=Post,paginate_by=10)


def post_list(request):
    qs = Post.objects.all() #<<이시점에는 데이터베이스 접속이 이루어지는게아님
    #이것의 매핑은 blog/templates/blog/post_list.html
    print(request.user)
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request,'blog/post_list.html',{
        'post_list':qs,
        'q':q
    }) #<< 이시점에 접속이 이루어짐





#무조건 get_object_or_404 ㄱㄱㄱ
# def post_detail(request,id):
#     # try:
#     #     post = Post.objects.get(id=id)
#     # except Post.DoesNotExist:
#     #     raise Http404
#
#     post = get_object_or_404(Post,id=id)
#     return render(request,'blog/post_detail.html',{
#         'post':post
#     })

post_detail = DetailView.as_view(model=Post,pk_url_kwarg='id')


#장고의 필터기능 {{post | filter}} 이게 필터였음
#ㅋㅋㅋ date 포맷의 경우 글로벌세팅스에 있는 date_format를 사용하게됨
#datetime 인스턴스는 타임존정보가있는 객체가있고 없는객체가있음
#비교시는 같은상태에서만 해야함
#장고에서는 무조건 현재시간은 timezone.now()로 시간을 구하는게 좋다


#urllib.parse import urlencode 이거 유용함
#dict 타입을 겟방식형태의 유알엘 모양으로 바꿔줌


#겟방식으로 넘길때 name="1212"&name="1232" 이렇게 같은 네임으로 들어오는 떄가있다
#이럴때 장고는 dict로 받는데 dict 는 애초에 같은 키를 지원하지않는것은 나도 이미 알고있다
#그래서 이럴때는 name:[] 리스트로 저장이된다
#그러나 파이선에서 접근하듯이 d['name'] 이렇게 접근하면 둘중에 하나만 나오게된다
#이럴때를 위해 함수로 접근할수있음 d.getlist('name') 이렇게하면 리스트로 나옴



post_new = CreateView.as_view(model=Post)#success_url이 지정되어 있지 않으면 알아서 redirect(post)해서 겟앱솔루트유알엘로 넘어감
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save() #save() 메서드는 자동으로 인스턴스를 리턴함
#             messages.success(request,'새 포스팅을 저장했습니다.')#리다이렉트 전에 저장해주는 거임
#             #messages로 저장됨 이걸 html에서 순회돌아서 tag와 message를 뽑으면됨!
#             return redirect(post) #겟앱솔루트 유알엘
#
#     else:
#         form  = PostForm()
#     return render(request,'blog/post_form.html',{
#         'form':form
#     })



#이런 제네릭 뷰들은 다들 디폴트 템플릿 경로가있음
#앱이름/모델명소문자_detail,_form,_list
#디폴트 템플릿경로 앱이름/모델명소문자_form.html 그래서 나오는군
#템플릿에서 접근시 모델명소문자.title 이런식으로 접근하면됨
post_edit = UpdateView.as_view(model=Post,fields='__all__')
#디폴트 템플릿 blog/post_confirm_delete.html
# post_delete =DeleteView.as_view(model=Post,success_url='/blog/')#삭제는 success_url 지정 필수(문자열 지정해줘야함)
post_delete =DeleteView.as_view(model=Post,success_url=reverse_lazy('blog:post_list'))#reverse를쓰면 에러남
#이유는 이건 reverse_laze를 사용해야함 같은 기능임
#이건 전역변수지정시에 씀 자바에 인스턴스와 static 변수 차이같은 느낌인듯
#클래스 변수에 씀
#success_url이 필요할때까지 리버스를 지연시키는거라는데 사실 무슨말인지 모르겠음 ㅋㅋ
#그냥 url 지정은 reverse,reverse_laze 이걸 써서 문자열로 만들면 나중에 바꿀때 힘듬
#그냥 저렇게 해서 그 url 이름을 지정해주는게 나음






