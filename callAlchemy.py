from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import requests
import os
apikey='' 

picture = open('1.jpg', 'rb').read() 
url = "http://access.alchemyapi.com/calls/image/ImageGetRankedImageFaceTags?apikey=%s&outputMode=json&imagePostMode=raw&forceShowAll=1" % apikey
r = requests.post(url = url, data = picture)
print (r.text)