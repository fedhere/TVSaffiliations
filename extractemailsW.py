# coding: utf-8

# In[4]:

import pandas as pd
import sys
from argparse import ArgumentParser
from config import tvsfile

sbuglist = ['']


def my_parse_args():
    """ Use ArgParser to build up the arguments we will use in our script
    """
    stored_args = {}
    # get the script name without the extension & use it to build up
    # the json filename
    parser = ArgumentParser(description='Selecting members by subgroup')
    parser.add_argument('subgroup',
                        action='store',
                        default=None,
                        help='Choose the subgroup affiliation:' +
                        '-'.join([s for s in subglist]))
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    TVSMembers = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                             tvsfile +
                             '/export?gid=0&format=csv',
                             index_col=0)

    TVSMembers['last name'] = TVSMembers.index
    
    subgroups = TVSMembers.primary.unique()
    global subglist
    subglist = [x for x in subgroups if str(x) != 'nan']
    conf = my_parse_args()
    primary = conf.subgroup
    secondary = conf.subgroup

    tmp = TVSMembers[TVSMembers.primary == primary]

    sgemails = tmp['email'].values
    femail = open('SubgroupEmails_'+''.join(primary.split())+'.dat', 'w')
    femail.write("These are the members with primary affiliation with " + primary + "\n")
    femail.write("\n")
    femail.write('\n'.join([em + ','for em in sgemails]))
    femail.write("\n")

    sgLnames = tmp['last name'].values
    sgFnames = tmp['first name'].values
    
    fnames = open('SubgroupNames_'+''.join(primary.split())+'.dat', 'w')
    fnames.write("These are the members with primary affiliation with " + primary + "\n")
    fnames.write("\n")
    for em in zip(sgLnames, sgFnames, sgemails):
        fnames.write('{0:15} {1:15} {2}\n'.format(em[0], em[1], em[2]))
 

    tmp = TVSMembers[(TVSMembers.secondary == secondary) | (TVSMembers['secondary.1'] == secondary) | (TVSMembers['secondary.2'] == secondary)]

    sgemails = tmp['email'].values
    femail.write("\n")
    femail.write("These are the members with secondary affiliation with " + secondary + "\n")
    femail.write("\n")
    femail.write('\n'.join([em + ','for em in sgemails]))
    
    sgLnames = tmp['last name'].values
    sgFnames = tmp['first name'].values
    sgPrimary = tmp['primary'].values

    fnames.write("\n")
    fnames.write("These are the members with secondary affiliation with " + secondary + " and their primary affiliation\n")
    fnames.write("\n")
    for em in zip(sgLnames, sgFnames, sgemails, sgPrimary):
        fnames.write('{0:15} {1:15} {2:40} {3}\n'.format(em[0], em[1], em[2], em[3]))
    
