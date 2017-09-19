from django.http.response import JsonResponse
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
#View를 상속받고
#get 함수를 만들어 준다음 그걸 as_view()로 받는거임
#get 을 as_view()로 받음 아마 저함수는 View 여기안에 있는듯
#View 사실 이건 상속받아서 잘 쓰지는 않고 다른게있음 updateview deleteview 이런거
#View는 걍 깡 코딩 그래도 알아두면 좋음
class PostListView1(View):
    def get(self,request):
        name = '공유'
        html = self.get_template_string().format(name = name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬장고 ㅋㅋ</p>
        '''
post_list1 = PostListView1.as_view()

#이렇게하면 템플릿만뜸!!
#인자 넘기는법! 꼭 저함수여야만함!
class PostListView2(TemplateView):
      template_name = 'dojo/post_list.html'

      def get_context_data(self, **kwargs):
          context = super().get_context_data()
          context['name']='공유'
          return context


post_list2 = PostListView2.as_view()


class PostListView3(View):
    def get(self,request):
        return JsonResponse(self.get_data(),json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {
            'message':'안녕 파이썬장고',
            'items':['파이썬','장고','Celery'],
        }
post_list3 = PostListView3.as_view()


class ExcelDownloadView(object):
    pass