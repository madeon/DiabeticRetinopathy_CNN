import cv2 as cv
import os

scale = 300

path1 = "../data/AverageColor/"
path2 = "../data/AverageColor2/"


def normalize_colors(current_path, new_path):
    count = 0
    print(count)

    for file in os.listdir(current_path):
        image = cv.imread(current_path + file)
        image = cv.addWeighted(image, 4, cv.GaussianBlur(image, (0, 0), scale / 30), -4, 128)
        cv.imwrite(new_path + file, image)
        count += 1
        print(count)


normalize_colors(path1, path2)




