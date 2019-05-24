'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal
format. IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:
1.2.3.4
123.45.67.89
'''

def is_valid_IP(strng):
    values = strng.split('.')
    if len(values)!=4:
        return False
    for value in values:
        if not valid_value(value):
            return False
    return True

def valid_value(value):
    if not value.isdigit():
        return False
    if len(value) > 1 and value[0] == '0':
        return False
    value  = int(value)
    if value >=0 and value <= 255:
        return True
    else:
        return False
        
            

        
    
    
#Other solutions

import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))




#Other solution

from re import compile, match

REGEX = compile(r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}'
                r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$')


def is_valid_IP(strng):
    return bool(match(REGEX, strng))



#One other solution

def is_valid_IP(strng):
    if len(strng.split(".")) != 4:
        return False
    
    for group in strng.split("."):
        if not group.isdigit() or group != str(int(group)) or not 0 <= int(group) <= 255:
            return False
    
    return True


#One more


import re

def is_valid_IP(string):
    ip = string.split('.')
    return len(ip) == 4 and all(
        re.match('^([1-9]\d*|0)$', v)
        and int(v) in range(256)
        for v in ip
    )
