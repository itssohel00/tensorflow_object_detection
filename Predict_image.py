from tensorflow.keras.models import load_model
import numpy as np
import cv2

import PIL
from PIL import Image
import os, sys
import matplotlib.pyplot as plt
import statistics

model = load_model("ResNet50_model_weights_B8_L64(image).h5")

#take photo and save
input = "./images/"
output = "./images/"

dirs = os.listdir( input )
a = len(dirs)

CATEGORIES = ["nothing", "box1", "box2", "box3", "box4"]

prediction2 = "---"
video = cv2.VideoCapture(0) 
a = a + 1

def prepare(image):
        IMG_SIZE = 150  # in txt-based
        new_array = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    
while True:       
    check, frame = video.read()  
    cv2.imshow("Capturing",frame)
    crop_img = frame[100:400, 200:500]
    
    if cv2.waitKey(20) & 0xFF == ord('d'):

            cv2.imwrite(output + str(a) +'.jpg',crop_img)

            img = cv2.imread(output + str(a) +'.jpg',cv2.IMREAD_COLOR)
            #cv2.imshow('image', img)
            


            #predict photo
            #img = cv2.imread('images/0.jpg',cv2.IMREAD_COLOR)

            cv2.putText(img, prediction2, (20, 40), cv2.FONT_ITALIC, 1.0, (0,0,250))

            img_infer = img
            pre_img = prepare(img_infer)
            prediction = model.predict(pre_img)

            #print(prediction) # will be a list in a list.
            b = prediction[0]
            c = b.tolist()
            #print ("Max value element : ", c.index(max(c)))
            prediction2 = (CATEGORIES[int(c.index(max(c)))])
            print(prediction2)

            cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()

