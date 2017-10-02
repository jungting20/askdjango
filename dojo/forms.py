from django import forms
from .models import Post,GameUser


#이건 그냥 장고 폼에서 쓸때 여기다 해주고
#모델폼을 쓰려면 모델 폼에 이걸 정의해 준다
def min_length_3_validator(value):
    if len(value) < 3 :
        raise forms.ValidationError('3글자 이상 입력해주세요')

# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])#함수 호출이아니고 그냥 함수를 넘겨주는거임
#     content = forms.CharField(widget=forms.Textarea)
#     #모델과 다른점은 모델은 제한이있는것과 없는걸 구분하는데 폼에서는 그냥 같은 케릭터필드
#     #요렇게 해주면 됨
#
#     #모델폼을 흉내내어 구현한거임
#     def save(self,commit = True):
#         post = Post(**self.cleaned_data)
#         if commit:
#             post.save()
#         return post
#     #모델폼을 사용하면 이걸 해줄 필요없이 알아서 구현이 되어있음 요렇게 되어있음
#   def save(self,commit=True):
#       self.instance = Post(**self.cleaned_data)
#       if commit:
#         self.instance.save()
#       return self.instance
#


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #ip 필드는 입력 받을게아니기 떄문에 필드에 정의 해주지 않음
        fields = ['title','content','user_agent']
        widgets = {
            'user_agent':forms.HiddenInput,#이러면 히든 필드로 들어감
            #값은 자바스크립트로 넣어줄거임
        }

class GameUserSignupForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['server_name','username']

    def clean_username(self):
        #클린후 이걸 또 호출하기 떄문에 결국 cleaned_data에는 이값이 들어가게 됨!
        #이게 필수
        return self.cleaned_data.get('username','').strip()

