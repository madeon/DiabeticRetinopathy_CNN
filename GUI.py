# USAGE
# tkinter_test.py

# import the necessary packages
import tensorflow
from tkinter import *

import numpy as np
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import pandas as pd
import cv2
from keras.engine.saving import load_model

scale = 30
image_size = 256

#Load the pre-trained model
model = load_model(r'C:\Users\mathi\OneDrive\Desktop\Bachelor\Bachelor\Neural Networks\Competitions\Diabetes\PythonProjects\GUI\data\150epochs.h5')

#Load labels
labels = pd.read_csv('data/retinopathy_solution.csv')
df = labels.set_index("image", drop=False)

def crop_images(image):

    # Gets the center left part of the image
    x = 0
    y = image.height / 2

    finishedLeft = False;

    # Loops untill a pixel that is not black is found
    while (finishedLeft != True):

        finishedRight = False;

        # Gets the pixel RGB value for each pixel from the starting point
        image.getpixel((x, y))

        # Moves the pixel once to the right
        x += 1

        try:
            # Checks if a given pixel does not have a black RGB
            # 20 is used to avoid that a bit of noise will cause it to mess up if it was only 0)
            if (image.getpixel((x, y)) > (20, 20, 20)):

                x2 = image.width - 1
                y2 = image.height / 2
                finishedLeft = True;

                while (finishedRight != True):
                    image.getpixel((x2, y2))
                    x2 -= 1

                    if (image.getpixel((x2, y2)) > (20, 20, 20)):
                        original_image = image.crop((x, 0, x2, image.height))
                        return normalize(original_image)
                        finishedRight = True
        except Exception as e:
            print("error: " + str(e))
            break

def normalize(image):
    image = np.array(image)
    image = cv2.addWeighted(image, 4, cv2.GaussianBlur(image, (0, 0), scale / 30), -4, 128)
    return resize(image)


def resize(image):
    img = Image.fromarray(image, 'RGB')
    resized_image = img.resize([image_size, image_size], Image.ANTIALIAS)
    predict(resized_image)
    return resized_image

def predict(image):
    im2arr = np.array(image, np.float32) / 255
    im2arr = im2arr.reshape(1, 256, 256, 3)
    prediction = model.predict_proba(im2arr)
    y_proba = model.predict_classes(im2arr)
    print_each_class_percentage(prediction)

    var.set(str(print_each_class_percentage(prediction)))






def print_each_class_percentage(prediction):
    percent_chance1 = round(prediction[0][0] * 100, 2)
    percent_chance2 = round(prediction[0][1] * 100, 2)
    percent_chance3 = round(prediction[0][2] * 100, 2)
    percent_chance4 = round(prediction[0][3] * 100, 2)
    percent_chance5 = round(prediction[0][4] * 100, 2)

    return "No DR: " + str(percent_chance1)+"%\n" + " Mild DR: " + str(percent_chance2) +"%\n" + " Moderate: " + str(percent_chance3) +"%\n" + " Severe: " + str(percent_chance4) +"%\n" + " Proliferative: " + str(percent_chance5) +"%\n"



def select_image():
    global panelA, panelB, label_prediction
    path = filedialog.askopenfilename()

    if(len(path) > 0):
        image = Image.open(path)
        processed = crop_images(image)
        processed = np.array(processed)

        #Original image
        image = np.array(image)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        #Processed
        processed = Image.fromarray(processed)
        processed = ImageTk.PhotoImage(processed)

        if panelA is None or panelB is None:
            #Original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            #Processed image
            panelB = Label(image=processed)
            panelB.image = processed
            panelB.pack(side="right", padx=10, pady=10)

            #Prediction
            label_prediction

        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=processed)
            panelA.image = image
            panelB.image = processed




# initialize the window toolkit along with the two image panels
root = Tk()
root.title("Diabetic Retinopathy - Screening Tool")
root.geometry('600x600')
panelA = None
panelB = None
label_prediction = None


btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

var = StringVar()
label = Label(root, textvariable=var)
label.pack()




root.mainloop()