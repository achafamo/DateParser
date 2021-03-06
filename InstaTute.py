import datefinder
import datetime
import requests
import csv
import sys
import random
from  scrapeDepartment import *

MONTH_DICT = {"Jan. ": "January ",
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

COLORS = ['blue', 'green', 'red', 'purple', 'yellow']
def createEvents(filename, className):
    # class_time = get_time(filename)
    dates = []
    prev = None
    with open(filename, 'r') as f:
        for line in f:
            line = replaceAbbreviation(line)
            matches = datefinder.find_dates(line, source=False)

            for match in matches:
                event = Event(className, line, match)
                # print type(event.start_date)
                dates.append(event)
    return dates
    # After done getting the events, I need to post this to some url on


def get_time(filename):
    # should get the class time of the class for the given syllabus
    pass


def isEmpty(matches):
    try:
        date = matches.next()
        return False
    except StopIteration:
        return True


def writeToCsv(events, filename, course):
    '''
    should update events.csv
    '''
    dateKnown = True
    if len(course.time) == 4:
        hour = int(course.time[0:2])
        minute = int(course.time[2:])
    elif course.time!="TBA":
        hour = int(course.time[0])
        minute = int(course.time[1:])
    else:
        dateKnown = False
    color = random.choice(COLORS)
    output = "events.csv"
    with open(output, 'w') as f:
        writer = csv.DictWriter(f, ["start_date", "end_date", "name", "Class", "context", "description", "color"])
        writer.writeheader()
        for event in events:
            start_date = event.start_date
            if not start_date.time() and dateKnown:
                start_date = start_date.replace(hour=hour, minute=minute)
            try:
                writer.writerow(
                    {'start_date': start_date.strftime('%Y-%m-%d %H:%M:%S'), 'name': "Event Title", 'Class': event.name,
                     'context': event.description, 'color':color})
            except ValueError:
                # print "problem with date format"
                continue


def replaceAbbreviation(line):
    for m in MONTH_DICT.keys():
        line = line.replace(m, MONTH_DICT[m])

    return line


def getCourseInfo(section):
    '''
    should update course.csv
    '''

    print section
    department = section.split()[0]    
    url = get_url(department)
    courses = scrape(url, department)
    for course in courses:
        if course.section.strip() == section.strip():
            return course
    return False


def writeCourse(course):
    output = "course.csv"
    with open(output, 'w') as f:
        writer = csv.DictWriter(f, ["name", "email", "class_time"])
        writer.writeheader()
        classname = course.name + " (" + course.section + ")"
        writer.writerow({"name": classname, "email": course.email})


class Event:
    def __init__(self, name, description, start_date, end_date=None):
        self.name = name
        self.description = description
        self.start_date = start_date

        if end_date:
            self.end_date = end_date

    def __str__(self):
        return self.name + " " + self.description + " " + str(self.start_date)


if __name__ == '__main__':

    try:
        sys.argv[1]
    except IndexError:
        section = "COSC 304 A"
    else:
        section = sys.argv[1]
    course = getCourseInfo(section)
    classname = course.name + " (" + course.section + ")"
    filename = "syllabus.txt"
    writeCourse(course)
    events = createEvents(filename, classname)
    print str(len(events)) + " events have been extracted from the syllabus for " + classname
    print "The professor's name is " + course.professor_name + " and their email address is " + course.email 
    writeToCsv(events, filename, course)



