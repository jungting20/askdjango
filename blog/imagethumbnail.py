image_url = "https://static.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg"

import requests

image_binary = requests.get(image_url).content

with open("flower.jpeg","wb") as f:
    f.write(image_binary)

#requests << pip 로 설치할수있음 이걸 이용하여 이미지를 다운 받음

from PIL import Image

flower_image = Image.open("flower.jpeg")

#pip로 설치함 pillow,pilkit 설치

from pilkit.processors import Thumbnail

processor = Thumbnail(width =300 , height = 300) #이미지 사이즈 고정

thumb_image = processor.process(flower_image) #위에 설정해둔 사이즈로 이미지 크기 조정 바이너리 파일이 이때 생성
thumb_image.save("thumb-300x300.png") #png로 저장

#이미지 서비승는 80%나 60%가 좋음 다만 인쇄시에는 원본이 좋을 수도

for quality in [100,80,60,40,20]:
    thumb_image.save("thumb-300x300-{}.jpg".format(quality),quality = quality)#100 80 60 40 20 사이즈 별로 압축


