
import os
import cv2 as cv
from PIL import Image

input_filepath = '../data/AverageColor2/'
output_filepath = '../data/AverageColor_resized/'

image_size = 256


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def resize(current_path, new_path):
    dirs = [l for l in os.listdir(current_path) if l != '.DS_Store']
    total = 0

    # Opens each image in the directory and performs crop on each image
    for item in dirs:
        image = Image.open(current_path + item)


        print("Saving: ", item, total)
        resized_image = image.resize([image_size, image_size], Image.ANTIALIAS)
        resized_image.save(os.path.join(new_path, item), 'JPEG')
        total += 1


resize(input_filepath, output_filepath)




