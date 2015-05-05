from alchemyapi import AlchemyAPI
import json
import requests
import os


import glob, os

apikey='' 
os.getcwd()
os.chdir("images")

#img='000120.jpg'

#imr=imread(img)
#plt.imshow(imr,zorder=0)
c=0
x=0;y=0;w=100;h=100
for img in glob.glob("*.jpg"):
    c=c+1
    if (c%10==0):   
        im = Image.open(img)
        draw = ImageDraw.Draw(im) 
        picture = open(img, 'rb').read() 
        url = "http://access.alchemyapi.com/calls/image/ImageGetRankedImageFaceTags?apikey=%s&outputMode=json&imagePostMode=raw&forceShowAll=1" % apikey
        r = requests.post(url = url, data = picture)
        j=json.loads(r.text)
        ct=len(j['imageFaces'])
        if ct>0 :
            i=1
            nx=int(j['imageFaces'][i-1]['positionX'])
            ny=int(j['imageFaces'][i-1]['positionY'])
            nh=int(j['imageFaces'][i-1]['height'])
            nw=int(j['imageFaces'][i-1]['width'])
            if nw+nh+6<w+h:
                print img
                print ('x, y, w, h:',nx,ny,nh,nw)
                #or nx-x+ny-y>w+h
                print ('frame:',c)
                print ('count_total', ct)        
                cm=0;cf=0 
                a0=0;a18=0;a25=0;a35=0;a45=0;a55=0;a99=0
                for i in range(1,ct+1):
                    if j['imageFaces'][i-1]['gender']['gender']=='MALE':
                        cm=+1
                    else:
                        cf=+1    
                    if j['imageFaces'][i-1]['age']['ageRange']=='<18':
                        a0=+1
                    elif j['imageFaces'][i-1]['age']['ageRange']=='18-24':
                        a18=+1 
                    elif j['imageFaces'][i-1]['age']['ageRange']=='25-34':
                        a25=+1 
                    elif j['imageFaces'][i-1]['age']['ageRange']=='35-44':
                        a35=+1 
                    elif j['imageFaces'][i-1]['age']['ageRange']=='45-54':
                        a45=+1 
                    elif j['imageFaces'][i-1]['age']['ageRange']=='55-64':
                        a55=+1 
                    elif j['imageFaces'][i-1]['age']['ageRange']=='>64':
                        a99=+1                     
                print ('count_male:',cm)
                print ('count_female:',cf)
                print ('count_<18:',a0)
                print ('count_18-24:',a18)
                print ('count_25-34:',a25)
                print ('count_35-44:',a35)
                print ('count_45-54:',a45)
                print ('count_55-64:',a55)
                print ('count_>64:',a99)
            x=nx;y=ny;h=nh;w=nw


        


        

