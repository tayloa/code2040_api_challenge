''' author: Aaront Taylor
    email: halfnote1004@gmail.com
    
    Summary: This code posts JSON data to a given api, recieves a string as a response,
    reverses the string, then sends it back for validation.
'''

import requests
import json
import urllib2

# funciton to reverse
def reverse_string(string):
    
    # set up the index for the while loop and create empty string to store reversed version
    i = len(string)-1
    new = ""
    
    # iterate backwards through the string and add each letter to the empty sting
    while i > -1:
        new += string[i]
        i-= 1
        
    # return the result
    return new

if __name__ == "__main__":
    
    #saving the urls for get and post requests
    url = "http://challenge.code2040.org/api/reverse"
    url2 = "http://challenge.code2040.org/api/reverse/validate"
    
    #post the token to the api
    data = {"token" : "3c05f7d89a15e581a0136af169568e9e"}
    response = requests.post(url, json=data)
    
    #save the returned JSON in a string
    normal =  response.content
    print normal
        
    #reverse the string
    reverse = reverse_string(normal)
    print reverse
    
    #repost the reverse to the api for validation
    data2 = {"token" : "3c05f7d89a15e581a0136af169568e9e", "string" : reverse }
    response = requests.post(url2, json=data2)    