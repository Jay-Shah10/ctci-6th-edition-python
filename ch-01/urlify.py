"""
Write a method to replace all spaces in a string with '%20'. 
you may assume that the string has sufficiant space at the end to hold
the additional charaters and that you are given the 'true' length of the string. 

Example: 
input: "Mr John Smith  ", 13
output: "Mr%20John%20Smith"
"""


from dataclasses import replace
import enum


def urlify(strs, length):

    strs = strs.strip() # remove whites paces from front and end.
    print(strs)

    # simple solution of using string replace. 
    result = strs.replace(" ", "%20")
    print(result)


    # another way: 
    r = strs[:length].replace(" ", "%20")
    print(r)
            

def main(): 
    
    strs = "Mr John Smith"
    length = 13
    urlify(strs=strs, length=length)

if __name__ == '__main__':
    main()
