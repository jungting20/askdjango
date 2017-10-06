from django import forms
from .models import Post
from askdjango.widgets.naver_map_point_widget import NaverMapPointWidget

class PostForm(forms.ModelForm):


    #위젯이란건 결국 html 코드인듯
    #난 저걸 클래스로 만들었고 그 클래스 안에서 render함수가 html 을 만들어줌
    #그래서 그 클래스를 호출하면 __str__ 처럼 render 이 실행되며 html 뿌려줌 ㅋㅋㅋ
    #장고가 기본으로 주는 필드가 아닌 내가만든 html로 주겠다 할때 widget를 사용
    #역서 render로 리턴되는 건 기본 textinput 필드하고 거기에 추가로 지도그려주는 html코드 부분을 더해서 리턴하게
    #오버라이드 했음 그래서 이렇게 지정해주면 그 부분이 나오게 되는거임
    dummy = forms.CharField(widget=NaverMapPointWidget(attrs={
        'width':"100%",'height':200
    }))

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat': NaverMapPointWidget(attrs={
               'width':600,'height':300
            }),


        }

