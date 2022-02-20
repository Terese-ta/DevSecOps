#!/home/takuma/Development/DevSecOps_Projects/DevSecOps_Class/bin/python
#Author: Venza Tech 
#Date: eb 19, 2022
#Purpose: To print all python keywords
import keyword
if __name__== "__main__":
    #to get all python keywords
    keywords = keyword.kwlist
    #to print the keywords
    for key in keywords:
        print(key)