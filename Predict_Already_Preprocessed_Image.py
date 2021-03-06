import os

import keras
import numpy as np
import cv2 as cv
import glob
import pandas as pd
from PIL import Image
from keras.models import load_model
from PIL import ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True


image_size = 256
scale = 300

un_processed_path = '../data/validation/'
processed_path = '../data/validation-average-resized/'

image_name = '113_right.jpeg'

#Load the pre-trained model
model = load_model('TeslaK80/03-12-2019.h5')

#Load labels
labels = pd.read_csv('TeslaK80/retinopathy_solution.csv')

df = labels.set_index("image", drop=False)



correct = 0
wrong = 0
total = 0

def predict_results_categorical(filename, prediction):
    global correct
    global wrong
    global total


    for index, row in df.iterrows():
        imageName = row['image']
        actual_level = row['level']

        if (imageName == filename):

            #Correct prediction
            if (prediction == actual_level):
                total += 1
                correct += 1
                print(' ' + str(imageName) + ': Actual result: ' + str(actual_level) + ' Prediction: ' + str(prediction))
                print_percentage()
                break;

            #Wrong prediction
            else:
                total += 1
                wrong += 1
                print(' ' + str(imageName) + ': Actual result: ' + str(actual_level) + ' Prediction: ' + str(prediction))
                print_percentage()
                break;



def predict_results_binary(filename, result):
    global correct
    global wrong
    global total

    for index, row in df.iterrows():
        imageName = row['image']
        actual_level = row['level']

        if (imageName == filename):

            ## NO DR Detected - and correct prediction
            if(actual_level == 0 and result == 0):
                correct += 1
                total += 1
                print_percentage()
                break;

            ## DR Detected - and correct prediction
            elif (actual_level > 0 and result > 0):
                correct += 1
                total += 1
                print_percentage()
                break;

            ## DR Detected - wrong prediction
            elif (actual_level > 0 and result == 0):
                wrong += 1
                total += 1
                print_percentage()
                break;

            ## NO DR Detected - wrong prediction
            elif (actual_level == 0 and result > 0):
                wrong += 1
                total += 1
                print_percentage()
                break;



def print_percentage():
    print('Total images: ' + str(total))
    print('Correct guesses: ' + str(correct))
    print('Wrong guessed: ' + str(wrong))
    percentage = correct / total
    print('Percentage correct: ' + str(percentage))


def print_each_class_percentage(prediction):
    percent_chance1 = round(prediction[0][0] * 100, 2)
    percent_chance2 = round(prediction[0][1] * 100, 2)
    percent_chance3 = round(prediction[0][2] * 100, 2)
    percent_chance4 = round(prediction[0][3] * 100, 2)
    percent_chance5 = round(prediction[0][4] * 100, 2)

    print(
        "No DR: " + str(percent_chance1) + " Mild DR: " + str(percent_chance2) + " Moderate: " + str(percent_chance3) +
        " Severe: " + str(percent_chance4) + " Proliferative: " + str(percent_chance5))


count0 = 0
count1 = 0

def sick_or_healthy(prediction):
    no_dr = round(prediction[0][0] * 100, 2)
    total = round(prediction[0][1] * 100, 2) + round(prediction[0][2] * 100, 2) + round(prediction[0][3] * 100, 2) + round(prediction[0][4] * 100, 2)

    if (no_dr > total):
        print("Case 0: No DR Detected! Percentage: " + str(no_dr))
        count0 + 1
    else:
        print("Case 1: DR Detected! Percentage: " + str(total))
        count1 + 1



def predict_already_processed_images(path):
    for filename in glob.glob(
            path + '/*.jpeg'):
        image = Image.open(filename)
        name = os.path.basename(filename)
        name_without_extension = name.split(".",maxsplit=1)[0]

        im2arr = np.array(image, np.float32) / 255
        im2arr = im2arr.reshape(1, 256, 256, 3)
        prediction = model.predict_classes(im2arr)


        predict_results_categorical(name_without_extension, prediction)

        # Remove comment to predict result as binary
        # predict_results_binary(name_without_extension, prediction)



predict_already_processed_images(processed_path)



