from PIL import Image
import os
import sys
import math

pathname = sys.argv[1]
imgs = os.listdir(pathname)
imgcount = len(imgs)
n = math.ceil(pow(imgcount, 0.5))

img1 = Image.open(pathname + "/1.png")
img1_size = img1.size
new_im = Image.new('RGB', (n * img1_size[0], n * img1_size[1]), (0, 0, 0))

for i in range(imgcount):
    x = i % n
    y = int(i / n)

    imgi = Image.open(pathname + f"/{i+1}.png")
    new_im.paste(imgi, (x * img1_size[0], y * img1_size[1]))

new_im.save(pathname + ".png", "PNG")
