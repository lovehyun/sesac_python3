# pip install pillow
from PIL import Image, ImageFilter

# 이미지 열기
image = Image.open("cats.jpg")

# 이미지 크기를 줄이고 싶음
resized_image = image.resize((80,60))
resized_image.save("small_cats.jpg")

# 이미지 블러
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("blur_cats.jpg")
