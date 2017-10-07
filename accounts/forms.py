from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()#요건 usercreationform 과 user 모델에 기본적으로 적용이 되어있지 않기 때문에
    #혜택을 받을 수 없다 그래서 이렇게 새로 재정의 해주고 save 함수를 재정의 해야함
    #아무것도 하지 않은 usercreationform 은 아이디 비번 비번확인 뿐
    #음 근데 이러면 모델폼의 유효성검사 혜택을 받을수없는데..
    #모델에 USER 을 재정의 하자 상속은 AbsUsermodel 인가 뭐 있음
    #이거 상속받아서 모델에 추가할 필드 넣고
    #여기에 굳이 해줄 필요없이 나머지는 모델폼이 알아서 해줌
    #내가 예전에 해둔 Customboard 참조하면 모든걸 할 수 있음
    #이걸 해결해야함
    address = forms.CharField()
    class Meta(UserCreationForm.Meta):#상속기법 이걸하지않으면 그냥 Meta를 싹다날리고 재정의 해버림
        fields = UserCreationForm.Meta.fields + ('email',) #email 은 디폴트로 User 모델에 정의 되어있기 때문에
        #내가 필드로 추가 할 수 있는거임 다른걸로 하려면 또 다른걸 해야하는듯(폼이니까 새로 적용해야함)

    def save(self, commit=True):
        user = super().save()#모델에 onetoone로 연결되어있음
        print('유저',user)
        profile = Profile.objects.create(user=user,phone_number = self.cleaned_data['phone_number'],
                               address = self.cleaned_data['address'])
        return user

class LoginForm(AuthenticationForm):#기본 로그인 폼을 상속받음
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer',None)
        if answer != 6:
            raise forms.ValidationError('missmatched!')
        return answer