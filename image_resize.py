import PIL
from PIL import Image
import os, sys

# parameter
input = "./box4/"
output = "./resize/box4/"
mywidth = 300

dirs = os.listdir( input )
number = len(dirs)
print("resize from: " + input + "     file number: " + str(number))
print("-"*50)
print("processing")
def resize_aspect_fit():
    count=0
    i=180
    for item in dirs:
        img = Image.open(input+item)
        wpercent = (mywidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
        i = i+1
        img.save(output + str(i) +'.jpg', 'JPEG', quality=80)

resize_aspect_fit()
print("Finished")
