#Question 
#List or provide all the key words in python 
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

#Question 2
# Select 3 key words and eplain what they do
Control Flow Keywords: if, elif, else
if: The if statement is used for decision-making operations.
    It contains some code and the said code will only run if the conditions in    the if statment are "true"
    
elif:The full name is "else if." The elif checks for multiple epressions.
     It runs after the condition of the if statement returns "false"
     Then python will run the conditions in the net elif blocks.
     If the elif conditions are false,python will eecute the else body. 

else: The else statement is used in conditional (if statements). 
      It is run when the if stament if false and python will do what is in the
      else statement. It is run only if previous if statements are "False"


