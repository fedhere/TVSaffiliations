
# coding: utf-8

# In[4]:

import pandas as pd
import sys
from argparse import ArgumentParser
from config import tvsfile
from gooey import Gooey


@Gooey(program_name="Extracting contact with subgroup affiliation")
def parse_args():
    """ Use ArgParser to build up the arguments we will use in our script
    """
    stored_args = {}
    # get the script name without the extension & use it to build up
    # the json filename
    parser = ArgumentParser(description='Selecting members by subgroup')
    parser.add_argument('subgroup',
                        action='store',
                        default=None,
                        help='''Choose the subgroup affiliation:
Interacting Binaries    Galactic
Supernovae        Cosmological
Multiwavelength Characterization/Counterparts
Tidal Disruption Events   Blazars
Non-degenerate Eruptive Variables    Magnetically Active Stars
Classification/Characterization     Microlensing
Gravitational Waves     Classification/Characterization
Fast Transients     Distance Scale
Pulsating Variables   Transiting Planets
                        ''')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    if tvsfile is None:
        print "Required Argument: Google Doc file identifier (if you do not have it email federica!)"
        sys.exit()
        
    TVSMembers = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                             tvsfile +
                             '/export?gid=0&format=csv',
                             index_col=0)
    conf = parse_args()
    primary = conf.subgroup
    secondary = conf.subgroup

    

    emails = TVSMembers[TVSMembers.primary == primary]['email'].values
    print "These are the members with primary affiliation with " + primary
    print ("")
    print (' '.join([em+','for em in emails]))

    emails = TVSMembers[(TVSMembers.secondary == secondary) | (TVSMembers['secondary.1'] == secondary) | (TVSMembers['secondary.2'] == secondary)]['email'].values
    print ("\n")
    print "These are the members with secondary affiliation with " + secondary
    print ("")
    print (' '.join([em+','for em in emails]))

