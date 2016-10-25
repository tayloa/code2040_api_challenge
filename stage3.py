''' author: Aaront Taylor
    email: halfnote1004@gmail.com
    
    Summary: This code posts JSON data to a given api and recieves a JSON dictionary containing a prefix and an array.
    The program then finds strings in the array without the prefix, stores them in an array and sends it back to the api for 
    validation.
'''

import requests
import json
import urllib2

# function to find strings without the prefix
def find_prefix(string,array):
    
    # empty list to hold strings without the the prefix
    strings = []
    
    # iterate through the array, add the string to the list if it doesn't have the prefix 
    for i in range(len(array)):
        # slice the string and see if the first few letters are the prefix
        cut = array[i][:len(string)]
        if string != cut:
            strings.append(array[i])
    
    return strings

if __name__ == "__main__":
    
    # saving the urls for get and post requests
    url = "http://challenge.code2040.org/api/prefix"
    url2 = "http://challenge.code2040.org/api/prefix/validate"
    
    # post the token to the api and convert the JSON to a dictionary
    data = {"token" : "3c05f7d89a15e581a0136af169568e9e"}
    response = requests.post(url, json=data)
    response =  json.loads(response.content)
        
    # grab the prefix and array from the dictionary
    prefix = response.get("prefix",None)
    array =  response.get("array", None)
    
    # find the strings without the prefix
    prefix_strings = find_prefix(prefix,array)        

    #repost the array to the api for validation
    data2 = {"token" : "3c05f7d89a15e581a0136af169568e9e","array" : prefix_strings }
    response = requests.post(url2, json=data2)    