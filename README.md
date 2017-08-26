# DateParser
The main script in this repository is InstaTute.py. Instatute.py reads the contents of the syllabus that is found in the syllabus.txt file and creates a spreadsheet document with a list of all the dates in the syllabus and the context for each extracted date. Then we are going to need to edit the created spreadsheet(events.csv) to add the event title and event description (from the context) for each given date. We will then be able to programmatically create these events on InstaTute. 

## Installation

Install Python 2 if you DON'T have python or if you have python 3.x version
  
  	sudo apt-get install python2.7
 
Then install pip if you don't already have it and using pip, install virtualenv which is a tool that we can use to ensure we
are all working on the same environment and the same dependencies

	pip install -U pip setuptools
	pip install datefinder


Finally, you need to make sure you have git on your computer. This link might help: http://rogerdudler.github.io/git-guide/ 
Then you need to download this code repository by running 
	
	git clone https://github.com/achafamo/DateParser.git

on your terminal 

## How to Use	
Go to downloded folder and run the following command

	python Instatute.py "Exact class section code"
	eg. python Instatute.py "ECON 375 A"

This will create two csv files: "events.csv" and "course.csv". The file that we need to edit is "events.csv"

## How to add to InstaTute

After editing the events document, you can then copy both "events.csv" and "course.csv" to lib/seeds folder of our application codebase. You should replace the existing files in that folder with the new ones. Then to create the new class and add the events onto InstaTute, simply run the followingcommand in the home directory of the InstaTute code base. 
	
	rake fill:data
    
