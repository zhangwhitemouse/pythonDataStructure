from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('E:\Masters\pic\\railpic\IMG_4318.JPG')

gray=img.convert('L')

plt.figure('pokemon')

plt.imshow(gray,cmap ='gray')

plt.axis('off')

plt.show()