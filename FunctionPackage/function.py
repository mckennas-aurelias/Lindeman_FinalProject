'''
Created on Dec 1, 2022

@author: drewsexton
'''
 
from PIL import Image, ImageFilter

def loadImage ( filename ):
    myimage = Image.open(filename)
    myimage.load()
    return myimage.show()

'''def blur_image(imageObject):    #requires the image already loaded
    # Doesn't look too different but it does blur a little. Depends on the original image
    #blurred = imageObject.filter(ImageFilter.BLUR)
    blurred = imageObject.filter(ImageFilter.EMBOSS)    # This produces dramatic results. 
    #blurred = imageObject.filter(ImageFilter.DETAIL)    # Doesn't look much different 
    return blurred'''