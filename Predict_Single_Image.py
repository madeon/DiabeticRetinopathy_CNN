import numpy as np
import cv2 as cv

from PIL import Image
from keras.models import load_model
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


image_size = 256
scale = 300

path = '../data/validation/'
image_name = '11_right.jpeg'

#Load the pre-trained model
model = load_model('pre_trained_h5_model/my_model.h5')


## Step 1: Crop image
def crop_images(current_path, image_name):
    image = Image.open(current_path + image_name)

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
                        normalize(original_image)
                        finishedRight = True
        except Exception as e:
            print("error: " + str(e))
            break


## Step 2: Normalize image
def normalize(image):
    image = np.array(image)
    image = cv.addWeighted(image, 4, cv.GaussianBlur(image, (0, 0), scale / 30), -4, 128)
    resize(image)


## Step 3: Resize image
def resize(image):
    img = Image.fromarray(image, 'RGB')
    resized_image = img.resize([image_size, image_size], Image.ANTIALIAS)
    predict(resized_image)


## Step 4: Predict
def predict(image):
    im2arr = np.array(image)
    im2arr = im2arr.reshape(1, 256, 256, 3)
    prediction = model.predict_proba(im2arr)
    print(prediction)




##Run prediction
crop_images(path, image_name)