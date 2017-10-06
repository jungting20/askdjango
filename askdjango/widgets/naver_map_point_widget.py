from django import forms
from django.template.loader import render_to_string
from django.conf import settings #항상 이렇게 불러와야함
import re
class NaverMapPointWidget(forms.TextInput):

    BASE_LAT,BASE_LNG = '37.497921','127.027636'


    #인자로 넘겨줘서 각자에 맞게 커스터마이징함
    def render(self, name, value, attrs): #TextInput 에 있는 html을 만들어주는 함수인 render을 오버라이드

        width = str(self.attrs.get('width',800)) #겟함수로 있으면 가져오고 없으면 디폴트 800 이거
        height = str(self.attrs.get('height',600))
        if width.isdigit():width += 'px' #isdigit는 문자열이 숫자로만 구성되어있느냐 이걸 알려주는 함수
        if height.isdigit(): height += 'px'

        context = {
            'naver_client_id' : settings.NAVER_CLIENT_ID,
            'id' :attrs['id'], #현재 formfield의 html id 그니까 forms.py에 지정한 필드명이 id_필드명으로 들어감
            'width':width,
            'height':height,
            'base_lat':self.BASE_LAT,
            'base_lng':self.BASE_LNG,
        }
        #수정시에 맵에 찍히는 부분 수정하게끔
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+',value)
                context.update({'base_lat':lat,'base_lng':lng})
            except (IndexError,ValueError):
                pass


        html = render_to_string('widgets/naver_map_widget.html',context
       )
        attrs['readonly']='readonly'
        parent_html = super().render(name,value,attrs)

        return parent_html + html
        #렌더투스트링이나 렌더나 savetext를 반환함 이걸 이용해서 만드는듯
        #숏컷에있는 render과는 다른거임 거기는 httpresponse 리턴이고 여기는 문자열 리턴
        #이걸 이용해서 템플릿 만듬