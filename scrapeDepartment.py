from bs4 import BeautifulSoup
import urllib2
import requests
import csv
import json
import ctypes
import sys

def add_classes():
	url ='http://hyve.bitnamiapp.com/colgate/index.php?qa=login&to=index.php%3Fqa%3Dadmin%26qa_1%3Dcategories'
	values = {'emailhandle': 'achafamo',
	    'password': 'Abeni#0921307891'}

	r = requests.post(url, data=values)
	print r.content

def write_json(results_file):
	with open(results_file) as f:
		reader = csv.DictReader(f)
		rows = list(reader)

	with open('courses.json', 'w') as f:
		json.dump(rows, f)
	return

def get_url(department="ECON"):
	BASE_URL = "http://www.colgate.edu/academics/courseofferings/results?term=201701&core=&distribution=&dept=" + department + "&before=22:30&after=07:30&level=&meets=M;T;W;R;F;&instructor=&firstYear=" 
	return BASE_URL
	 
def scrape(url, department):	
	request = urllib2.Request(url)
	content = urllib2.urlopen(request).read()
	soup = BeautifulSoup(content)
	classes = soup.findAll('div', attrs={'class':'clms'}) #,'font-size':'9px;width:60px'})
	sections = soup.findAll('a', attrs={'class': 'bodyLink'})
	
	idx =1
	sec = 0
	courses = []
	for i in range(1, len(classes), 12): 	          
		line = "(" + str(idx) + "," +  "'" +classes[i].string+ sections[sec].string + sections[sec+1].string +"'),"+"\n" 		         
		email = sections[sec+1]['href'].split('/')[-1] + "@colgate.edu"
		
		course = Course(classes[i].string, department, sections[sec+1].string, sections[sec].string, email, classes[i+3].string)
		courses.append(course) 
		idx+=1
		sec+=2
	return courses

class Course:
	def __init__(self, name, department, professor_name, section, professor_email = None, time = None):
		self.name = name
		self.department = department
		self.professor_name = professor_name
		self.section = section 
		self.email = professor_email
		self.time = time

	def __str__(self):
		return "name: " + self.name + " professor_name: " + self.professor_name + " section: "+ self.section + " email: " + self.email +"\n"
if __name__ == '__main__':
	try:
		sys.argv[1]
	except IndexError:
        	department = "ECON"
	else:
        	department = sys.argv[1]
  	url =get_url(department)
	courses = scrape(url, department)
	for course in courses:
		print str(course)

