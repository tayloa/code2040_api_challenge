''' author: Aaront Taylor
    email: halfnote1004@gmail.com
    
    Summary: This code posts JSON data to a given api and recieves a JSON dictionary containing a string and an array.
    The program then finds the index at which the given string is located in the array and sends it back to the api for 
    validation.
'''

import requests
import json
import urllib2

# funciton to find the needle
def find_needle(string,array):
    
    # iterate through the array, break when the "needle" is found, and return the index, 
    for i in range(len(array)):
        if string == array[i]:
            return i

if __name__ == "__main__":
    
    # saving the urls for get and post requests
    url = "http://challenge.code2040.org/api/haystack"
    url2 = "http://challenge.code2040.org/api/haystack/validate"
    
    # post the token to the api and convert the JSON to a dictionary
    data = {"token" : "3c05f7d89a15e581a0136af169568e9e"}
    response = requests.post(url, json=data)
    response =  json.loads(response.content)
        
    # grab the needle and haystack from the dictionary
    needle = response.get("needle",None)
    haystack =  response.get("haystack", None)
    
    # find the needle    
    needle = find_needle(needle,haystack)
        

    #repost the needle to the api for validation
    data2 = {"token" : "3c05f7d89a15e581a0136af169568e9e", "needle" : needle }
    response = requests.post(url2, json=data2)    