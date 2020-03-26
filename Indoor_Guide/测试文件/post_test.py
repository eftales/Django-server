
import requests
import json
import simplejson
url = 'http://localhost:8000/Indoor_Guide/get_location'
data = str(list(range(0,133)))[1:-1]


r = requests.post(url, data=data)
print(r.text)
'''
import time
t1 = time.clock()
import numpy
t2 = time.clock()
print(t2 - t1)
'''