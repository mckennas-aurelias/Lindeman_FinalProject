#function.py
'''
Name: Drew Sexton, Kyle Lindeman, Madi Bratton, Ava Berling
email: sextondw@mail.uc.edu, lindemkj@mail.uc.edu,  berlinag@mail.uc.edu, brattomn@mail.uc.edu
Assignment: Final Assignment
Course: IS 4010
Semester/Year: Fall 2022
Description: collaborate with your team to develop an Eclipse app and go on a scavenger hunt.
'''
 
from PIL import Image, ImageFilter

def loadImage ( filename ):
    myimage = Image.open(filename)
    myimage.load()
    return myimage.show()

