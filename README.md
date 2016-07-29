# TVSaffiliations

Download the code extractemails.py and the configuration file conf.py

Change the value of tvsfile in conf.py to the correct GoogleDoc file link, which the TVS co-chairs Ashish and Federica can provide.

run as 

    python extractemails.py
  

The GUI will ask you which affiliation you are interested in and a list of emails of member with that primary subgroup affiliation, and a list of emails of member with that secondary subgroup affiliation are printed.

Notice: depending on your python version and your system running the command may return an error related to screen access

    python extractemails.py 
This program needs access to the screen.
Please run with a Framework build of python, and only when you are
logged in on the main display of your Mac.

In this case use pythonw

    pythonw exractemails.py
