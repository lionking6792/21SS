# Week 5
# C.S. major 2015722089 김태환

import numpy as np
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt

# 이미지 로드 및 원본 이미지 출력
image = Image.open("./Lenna.png")

plt.imshow(image)
plt.show()
#

# 좌우 반전된 이미지 출력
image_trans=image.transpose(Image.FLIP_LEFT_RIGHT)

plt.imshow(image_trans)
plt.show()
#

# 180도 회전된 이미지 출력
image_rotate=image.transpose(Image.ROTATE_180)

plt.imshow(image_rotate)
plt.show()
#


# 가로, 세로의 길이가 각각 2배 축소된 이미지 출력
image_small=image.resize((int(image.width / 2), int(image.height / 2)))

plt.imshow(image_small)
plt.show()

print(image_small.size)

image_small.save("./Image_small.png")
#


# 번외(수업)
# (32, 32) resize
# image2 = image.resize((32, 32))

# plt.imshow(image2)
# plt.show()

# print(image2)

# print(type(image2))

# print(image2.size)

# print(image2.mode)

# print(image2.getpixel((0,0)))


# blur 이미지
# blurred_image = image.filter(ImageFilter.BLUR)

# plt.imshow(blurred_image)
# plt.show()

# blurred_image.save("./blurred_Lenna.png")
#
