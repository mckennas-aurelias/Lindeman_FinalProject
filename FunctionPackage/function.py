'''
Created on Dec 1, 2022

@author: drewsexton
'''
 
from PIL import Image

def loadImage ( filename ):
    myimage = Image.open(filename)
    myimage.load()
    return myimage.show