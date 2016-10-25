''' author: Aaront Taylor
    email: halfnote1004@gmail.com
    
    Summary: This code posts JSON data to a given api and recieves a JSON dictionary containing a date in ISO 8601 format and 
    a time interval in seconds. The program then parses the date, adds the interval to it, and sends it back to the api for validation.
'''

import requests
import json
import datetime
import urllib2

# function to add the interval(seconds) to the date
def add_dates(date,seconds):

    # pull the year, month, day, hour, minute, and second from the date string
    y = int(date[0:4])
    m = int(date[5:7])
    d = int(date[8:10])
    h = int(date[11:13])
    mins = int(date[14:16])
    s = int(date[17:19])
    
    # confirm the date was parsed correctly
    print "Date =",date
    print "Parsed Date =",y,m,d,h,mins,s
        
    # turn the date into an object using the datetime module
    date = datetime.datetime(y,m,d,h,mins,s)
    print "Date Object =",date
    
    print "\nInterval =",seconds,"seconds"

    # add the interval to the date and convert it back to ISO 860 format
    newdate = date + datetime.timedelta(0,seconds)
    newdate = newdate.isoformat()
    print "Old date =",date.isoformat()
    print "New date =",newdate
    
    # return the date with the timezone tacked on at the end
    return str(newdate)+"Z"

if __name__ == "__main__":
    
    # saving the urls for get and post requests
    url = "http://challenge.code2040.org/api/dating"
    url2 = "http://challenge.code2040.org/api/dating/validate"
    
    # post the token to the api and convert the JSON to a dictionary
    data = {"token" : "3c05f7d89a15e581a0136af169568e9e"}
    response = requests.post(url, json=data)
    response =  json.loads(response.content)
        
    # grab the datestamp and interval from the dictionary
    datestamp = response.get("datestamp",None)
    interval =  response.get("interval", None)
    
    # add the interval to the date
    result = add_dates(datestamp,interval) 

    #repost the result to the api for validation
    data2 = {"token" : "3c05f7d89a15e581a0136af169568e9e","datestamp" : result }
    response = requests.post(url2, json=data2)    