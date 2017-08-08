import datefinder
import datetime
import requests
import csv
import sys

MONTH_DICT  = {"Jan. ": "January ",
              "Feb. ": "February ",
              "Mar. ": "March ",
              "Apr. ": "April ",
              "May. ": "May ",
              "Jun. ": "June ",
              "Jul. ": "July ",
              "Aug. ": "August ",
              "Sep. ": "September ",
              "Sept. ": "September ",
              "Oct. ": "October ",
              "Nov. ": "November ",
              "Dec. ": "December "}
def createEvents(filename, className):
    #class_time = get_time(filename)
    dates = []
    prev = None
    with open(filename, 'r') as f:
        for line in f:
            line = replaceAbbreviation(line)
            matches = datefinder.find_dates(line, source=True)

            for match in matches:
                event = Event(className, line, match)
                #print event.start_date
                dates.append(event)
    return dates
    #After done getting the events, I need to post this to some url on
def get_time(filename):
    #should get the class time of the class for the given syllabus
    pass

def isEmpty(matches):

    try:
        date = matches.next()
        return False
    except StopIteration:
        return True

def writeToCsv(events, filename):
    output = filename.split('.')[0] + '.csv'
    with open(output, 'w') as f:
        writer = csv.DictWriter(f, ["Date", "Class", "Description"])
        writer.writeheader()
        for event in events:
            writer.writerow({'Date':event.start_date ,'Class':event.name , 'Description':event.description})

def replaceAbbreviation(line):
    #print line
    for m in MONTH_DICT.keys():
        line = line.replace(m, MONTH_DICT[m])
    #print line
    return line


class Event:
    def __init__(self, name,description, start_date,  end_date = None):
        self.name = name
        self.description = description
        self.start_date = start_date

        if end_date:
            self.end_date = end_date
    def __str__(self):
        #print str(self.start_date)
        return self.name + " " + self.description + " " + str(self.start_date)
if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        filename = "syllabus3.txt"
    else:
        filename = sys.argv[1]
    try:
        sys.argv[2]
    except IndexError:
        classname = "Model African Union"
    else:
        classname = sys.argv[2]

    print filename, classname
    events = createEvents(filename, classname)
    print len(events)
    #url = 'http://instatutee.herokuapp.com/' #users/sign_in'
    #for event in events:
        #print event
    writeToCsv(events, filename)
    #need to
    #event_params = {"event_params": events[-1]}
    #res = requests.post(url, data=event_params)
    #print(res.text)
    #if time part is 0 make it equal to classtime
    #figure out how to access text file from remote database


    # Fill in your details here to be posted to the login form.
    #payload = {
     #   'email': 'achafamo@colgate.edu',
      #  'password': 'password'
    #}

    # Use 'with' to ensure the session context is closed after use.
    #with requests.Session() as s:
     #   p = s.get(url)
        #p = s.post(url, data=payload)
        # print the html returned or something more intelligent to see if it's a successful login page.
      #  print p.text

        # An authorised request.
        #r = s.get('A protected web page url')
        #print r.text
        # etc...