import datefinder
import datetime
import requests

if __name__ == '__main__':
    s = "string with no dates"
    matches = datefinder.find_dates(s)
    try:
        date = matches.next()
        print date
    except StopIteration:
        print "none"

