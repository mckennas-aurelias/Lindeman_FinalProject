'''
Created on Nov 22, 2022

@author: drewsexton
'''
import json
  
 
# Opening JSON file
f = open('EncryptedGroupHints.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['Lindeman']:
    print(i)
  
# Closing file
f.close()

