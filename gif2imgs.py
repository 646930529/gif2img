from PIL import Image
import os
import sys

filename = sys.argv[1]
pathname = filename[:-4]
im = Image.open(filename)
os.mkdir(pathname)
try:
    while 1:
        im.seek(im.tell() + 1)
        im.save(pathname + '/' + str(im.tell()) + '.png')
except EOFError:
    pass
