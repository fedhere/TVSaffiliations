from __future__ import print_function
import numpy as np
from oauth2client.client import SignedJwtAssertionCredentials
from submitNewMember import submitMember
import json
import sys
import gspread
import datetime


def putInSheet(sheet, values, i=1,  nmax=20) :
    allcells = ['A','B','C','D','E','F','G','H','I','J','K']
    
    while i<1000:
        cells = np.array([ sheet.acell('%s%d'%(c, i)).value for c in allcells])
        print (cells[0])
        if (cells == '').all():
            break
        i += 1 
    
    for v,k in values.iteritems():
            print (v,k)
            sheet.update_acell('%s%d'%(v,i), k)
        
    
if __name__ == '__main__':

    myname = sys.argv[1]
    json_key = json.load(open('tvscredentials.json')) # json credentials you downloaded earlier
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

    file = gspread.authorize(credentials) # authenticate with Google
    sheet = file.open("LSST_TVS_subgroups").sheet1 # open sheet

    newmembers = {}
    
    vals = {'A': 'last name',
            'B': 'first name',
            'C': 'affiliation',
	    'E': 'email',
            'D': '',
            'F': 'primary',
            'G': '',
            'H': '',
	    'I': ''}

    app = open("application.txt", "r").readlines()
    for i,l in enumerate(app):
        if l.startswith("Name: "):
            #print (l)
            name = " ".join(l.split()[1:]) 
            newmembers[name] = {}            
            vals['A'] = l.split()[-1].strip()
            vals['B'] = ' '.join(l.split()[1:-1]).strip()
            
        elif l.startswith("Email: "):
            #print (l)
            vals['E'] = l.replace("Email: ", "").strip()

            newmembers[name]['email'] = l.split()[1]
            
            if vals['E'].split('.')[-1] in ['com', 'edu', 'gov']:
                vals['D'] = ''
            elif vals['E'].endswith('.cl'):
                vals['D'] = 'CL'
            elif vals['E'].split('.')[-1] in ['nz', 'au', 'br']:
                vals['D'] = 'other'                
            elif vals['E'].split('.')[-1] in ['fr','de','uk','it', 'sl']:
                vales['D'] = EU
            
        elif l.startswith("Affiliation: "):
            #print (l)
            vals['C'] = l.replace("Affiliation: ", "").strip()
            newmembers[name]['affiliation'] = " ".join(l.split()[1:])
            
        elif l.startswith("Primary subgroup affiliation (exactly one): "):
            #print (l)
            vals['F'] = l.replace(
                "Primary subgroup affiliation (exactly one): ",
                                  "").strip()
            
        elif l.startswith("Subgroups to join (at most 3):"):
            #print (app[i:])

            try:
                #print (app[i+1])
                vals['G'] = app[i+1].replace("  - ", "").strip()
            except:
                pass
         
            try:
                #print (app[i+2])
                vals['H'] = app[i+2].replace("  - ", "").strip()      
            except:
                break
         
            try:
                #print (app[i+3])
                vals['I'] = app[i+3].replace("  - ", "").strip()     
            except:
                break
    vals['L'] = datetime.date.today().strftime("%d %B %Y")
    #print (vals)
    #submitMember(newmembers, myname)
    
    putInSheet(sheet, vals, i=170)

