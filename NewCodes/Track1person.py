from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import requests
import os

from pylab import *
from PIL import Image, ImageDraw

import glob, os

apikey='' 
os.getcwd()
os.chdir("i2")

img='000120.jpg'

imr=imread(img)
plt.imshow(imr,zorder=0)
c=0
for img in glob.glob("*"):
    c=c+1
    if (c%10==0):    
        im = Image.open(img)
        draw = ImageDraw.Draw(im) 
        print(img)
        picture = open(img, 'rb').read() 
        url = "http://access.alchemyapi.com/calls/image/ImageGetRankedImageFaceTags?apikey=%s&outputMode=json&imagePostMode=raw&forceShowAll=1" % apikey
        r = requests.post(url = url, data = picture)
        j=json.loads(r.text)
        x=int(j['imageFaces'][0]['positionX'])
        y=int(j['imageFaces'][0]['positionY'])
        h=int(j['imageFaces'][0]['height'])
        w=int(j['imageFaces'][0]['width'])
        
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((x - .5, y - .5), w, h,alpha=.2))

plt.show()

