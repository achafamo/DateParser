from bs4 import BeautifulSoup
import urllib2
import requests
import csv
import json
import ctypes

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
url = "http://www.colgate.edu/academics/courseofferings/results?term=201701&core=&distribution=&dept=ECON&before=22:30&after=07:30&level=&meets=M;T;W;R;F;&instructor=&firstYear=" 
def scrape(url, results_file):
    with open(results_file, 'w') as results:
        results.write("-- id, Course\n")
        #soup = BeautifulSoup(requests.get(url)., 'html5lib')
        request = urllib2.Request(url)
        content = urllib2.urlopen(request).read()
        soup = BeautifulSoup(content)
        classes = soup.findAll('div', attrs={'class':'clms'}) #,'font-size':'9px;width:60px'})
        print len(classes)
        idx =1
        for i in range(1, len(classes), 12):
            print classes[i]
            results.write("(" + str(idx) + "," +  "'" +classes[i].string+ "'),"+"\n" )
            idx+=1

if __name__ == '__main__':
    
    scrape(url, 'courses.csv')
    write_json('courses.csv')

