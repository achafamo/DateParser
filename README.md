# DateParser
The main scripts in this repository are Instatute.py and scrape_classes.py. Instatute.py takes in a Syllabus in .txt format and creates a spreadsheet document with a list 
of all the dates in the syllabus and the context for each extracted date. The people at Amazon Mechanical Turk are going to need to edit the 
created spreadsheet to add the event title and event description (from the context) for each given date. We will then be able to 
programmatically create these events on the InstaTute Calendars. 

## Installation

Install Python 2 if you DON'T have python or if you have python 3.x version
  
  sudo apt-get install python2.7
 
Then install pip if you don't already have it and using pip, install virtualenv which is a tool that we can use to ensure we
are all working on the same environment and the same dependencies

    pip install -U pip setuptools
    
    pip install datefinder

## How to Use

    python Instatute.py NAME_OF_SYLLABUS_FILE, NAME_OF_COURSE

This should create a .csv file with same name as the file name of the syllabus which contains records of the extracted dates and their contexts
    
