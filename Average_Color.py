import cv2 as cv
import os


##Important: Must be done before images are resized

scale = 300

path1 = "../data/evenly_distributed_data_cropped/"
path2 = "../data/evenly_distributed_data_cropped_average_color/"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def normalize_colors(current_path, new_path):
    create_directory(new_path)
    count = 0
    print(count)

    for file in os.listdir(current_path):
        image = cv.imread(current_path + file)
        image = cv.addWeighted(image, 4, cv.GaussianBlur(image, (0, 0), scale / 30), -4, 128)
        cv.imwrite(new_path + file, image)
        count += 1
        print(count)


normalize_colors(path1, path2)




