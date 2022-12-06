'''
Name: Kyle Lindeman, Drew Sexton, Ava Berling, Madison Bratton
email: drapernm@mail.uc.edu, sextondw@mail.uc.edu, berlinag@mail.uc.edu 
Assignment: Final Assignment 
Course: IS 4010
Semester/Year: Fall 2022
Brief Description:This projects demonstrates that we can make and API call with a URL
'''

import json
import requests
#from FunctionPackage import EncryptedGroupHints

decode = open('EncryptedGroupHints.json')

data= json.load(decode)

for i in data['emp_details']:
    print(i)
decode.close()


'''
#decode the json
def decode():
json.load(EncryptedGroupHints.json)
    
    parsed_json = json.loads(data.text) #python dictionary

    
    print("Title:", parsed_json[0]["title"]) #title of photo
    print("Explanation:", parsed_json[0]["explanation"]) #Explanation of photo
    print("Date:", parsed_json[0]["date"]) #Date Taken
    
    if "copyright" in parsed_json[0]:
        print("Copyright:", parsed_json[0]["copyright"]) #Copyright owner
    else:
        print("Image is public domain") #pulic domain image
    
    webbrowser.open(parsed_json[0]["url"]) #shows image in browser window
decode()


def printPic():
    #picture
    '''