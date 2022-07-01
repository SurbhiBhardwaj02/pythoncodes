##Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string.
##Original sequence: 000111000111
##Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
##True
##Original sequence: 00011100011
##Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
##False

def check(str1):
    while '10' in str1:
        str1= str1.replace('01','')
    return len(str1)==0

s1='01010101'
s2='000111000111'
s3='00011100011'
print(check(s1))
print(check(s2))
print(check(s3))