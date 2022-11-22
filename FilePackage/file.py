'''
Created on Nov 22, 2022

@author: drewsexton
'''
import json
  
 
# Opening JSON file
englishFile = open('english.txt','r').readlines()
  
jsonFile = open('EncryptedGroupHints.json')

jsonDict = json.load(jsonFile)

hints = jsonDict['Lindeman']

print(hints)

print(type(englishFile))

print(englishFile[42060])

for x in hints:
    print(englishFile[int(x)])
    print(x.join(','))


'''for i in data['28419','19311','22146', '42048', '23886', '598', '105654', '24231', '19311', '9442']:
    print(i)
    
file1.close()

'''

