import sys
import requests

from formid_config import *

f = open("newmembers.txt").readlines()

newmembers = {}
i = 0

myname = sys.argv[1]

for i,l in enumerate(f):
    if len(l.split()) < 1:
        continue
    if "Name:" in l.split()[0]:
        name = " ".join(l.split()[1:]) 
        newmembers[name] = {}
    if "Email:" in l.split()[0]:
        newmembers[name]['email']=l.split()[1]
    if "Affiliation:" in l.split()[0]:
        newmembers[name]['affiliation'] = " ".join(l.split()[1:])

#for k in newmembers:
#    print (k, newmembers[k])
        
url = 'https://docs.google.com/forms/d/e/' + formid + '/formResponse'

user_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

for k in newmembers.iterkeys():
    
    print (k)
    form_data = {'entry.829708031':k,
             'entry.292670442':newmembers[k]['email'],
             'entry.1859017614':newmembers[k]['affiliation'],
             'entry.1707165737':myname,
             'entry.360865007':'Transients and Variable Stars'}
    
    #print (form_data)
    r = requests.post(url, data=form_data)#, headers=user_agent)
    print (r)

