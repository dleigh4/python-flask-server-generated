import connexion
import six
import json
import os.path
from os import path
from bisect import bisect_left

from swagger_server.models.phonenumber import Phonenumber  # noqa: E501
from swagger_server import util


def phone_get():  # noqa: E501
    """Requests a phone number to be allotted by the server

     # noqa: E501


    :rtype: Phonenumber
    """
    if not(path.exists('numbers.json')):
        currentAllotted = { 'next': 1111111111, 'count': 0, 'allotted': [], 'nextloc' = 0 } 
        
    else:
        with open('numbers.json', 'r') as fp:
            currentAllotted = json.loads(fp.read())
            
            
    if (currentAllotted['count'] == 8888888889):
        return {}, 404
    
    allottedNumber = currentAllotted['next']                                            # set next allottable number for further manipulation
    strNumber = str(allottedNumber)
    
    currentAllotted['allotted'].insert(currentAllotted['nextloc'], allottedNumber)      # insert allotted number into list of allotted numbers
    
    if (currentAllotted['nextloc'] < currentAllotted['count']):                         # if there's later allotted numbers, check for the next "free" sequential number
        
        nextNum = allottedNumber + 1
        nextLoc = currentAllotted['nextloc'] + 1

        while (currentAllotted['allotted'][nextLoc] == nextNum):
            ++nextNum
            ++nextLoc
        
        currentAllotted['next'] = nextNum
        currentAllotted['nextloc'] = nextLoc
            
    else:
        currentAllotted['next'] += 1
        currentAllotted['nextloc'] += 1
        
        
    currentAllotted['count'] += 1
    
    output = Phonenumber(id = alottedNumber, name = strNumber[0:4] + "-" + strNumber[4:8] + "-" + strNumber[8:13]
    
    with open('numbers.json', 'w') as fp:
        fp.write(json.dumps(currentAllotted))
    
    return output, 200


def phone_number_get(number):  # noqa: E501
    """Requests a specific number to be allotted, which is returned if available; if unavailable, responds with a system-allotted number

     # noqa: E501

    :param number: The phone number requested by the user
    :type number: int

    :rtype: Phonenumber
    """
    if not(path.exists('numbers.json')):
        currentAllotted = { 'next': 1111111111, 'count': 0, 'allotted': [], 'nextloc' = 0 } 
        
    else:
        with open('numbers.json', 'r') as fp:
            currentAllotted = json.loads(fp.read())
            
            
    if (currentAllotted['count'] == 8888888889):
        return {}, 404
    
    
    if ((currentAllotted['next'] != number) && (BinarySearch(currentAllotted['allotted'], number) == -1)):     # Case: requested number is out of sequence & not already allotted
        currentAllotted['allotted'].insert(bisect.bisect_left(currentAllotted['allotted'], number), number)
        
        
    else:                                                                               # Case: requested number is next in sequence or already allotted
        allottedNumber = currentAllotted['next']                                        # set next allottable number for further manipulation
        strNumber = str(allottedNumber)
        
        currentAllotted['allotted'].insert(currentAllotted['nextloc'], allottedNumber)  # insert allotted number into list of allotted numbers
        
        if (currentAllotted['nextloc'] < currentAllotted['count']):                     # if there's later allotted numbers, check for the next "free" sequential number
            
            nextNum = allottedNumber + 1
            nextLoc = currentAllotted['nextloc'] + 1

            while (currentAllotted['allotted'][nextLoc] == nextNum):
                ++nextNum
                ++nextLoc
            
            currentAllotted['next'] = nextNum
            currentAllotted['nextloc'] = nextLoc
                
        else:
            currentAllotted['next'] += 1
            currentAllotted['nextloc'] += 1
            
            
        
    currentAllotted['count'] += 1
    
    output = Phonenumber(id = alottedNumber, name = strNumber[0:4] + "-" + strNumber[4:8] + "-" + strNumber[8:13]
    
    with open('numbers.json', 'w') as fp:
        fp.write(json.dumps(currentAllotted))
    
    return output, 200
    
    
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
