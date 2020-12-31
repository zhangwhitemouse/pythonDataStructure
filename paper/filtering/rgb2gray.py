from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('E:\Masters\pic\\railpic2\IMG_4519.JPG')

gray=img.convert('L')

plt.figure('pokemon')

# plt.imsave('gray2',gray)
plt.imshow(gray,cmap ='gray')

plt.axis('off')

plt.show()