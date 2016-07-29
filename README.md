# TVSaffiliations

These chunks of python code allow the user to collect emails of LSST TVS members based on affiliation. Two scripts are provided, one which uses the command line argument, and one which uses a gui, which ultimately is to be implemented on my website.

Change the value of tvsfile in conf.py to the correct GoogleDoc file link, which the TVS co-chairs Ashish and Federica can provide.

## Withot the GUI: 

run as 

    python extractemails_nogui.py <subgroups>

to see a list of the subgroups run as   

    python extractemails_nogui.py  -h


## GUI use:

run as 

    python extractemails.py
  

The GUI will ask you which affiliation you are interested in and a list of emails of member with that primary subgroup affiliation, and a list of emails of member with that secondary subgroup affiliation are printed.

Notice: depending on your python version and your system running the command may return an error related to screen access


    This program needs access to the screen.
    Please run with a Framework build of python, and only when you are
    logged in on the main display of your Mac.

In this case use pythonw

    pythonw exractemails.py
