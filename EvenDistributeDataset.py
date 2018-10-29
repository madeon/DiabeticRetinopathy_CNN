
from PIL import Image
import pandas as pd

path = 'trainLabels.csv'

##Dict containing image name as key and level as value
labels = pd.Series.from_csv(path, header=0).to_dict()

# Moves images to a folder corresponding with the image label, 0, 1, 2, 3 or 4.
def move_images(current_path):

    for key, value in labels.items():

        if (value == 0):
            image = Image.open(current_path + key + '.jpeg')
            image.save('H:/Bachelor data/even_distributed_data/0/' + key + '.jpeg', 'JPEG')
            print('Saved: ' + str(key) + ' to folder: ' + str(0))

        if (value == 1):
            image = Image.open(current_path + key + '.jpeg')
            image.save('H:/Bachelor data/even_distributed_data/1/' + key + '.jpeg', 'JPEG')
            print('Saved: ' + str(key) + ' to folder: ' + str(1))

        if (value == 2):
            image = Image.open(current_path + key + '.jpeg')
            image.save('H:/Bachelor data/even_distributed_data/2/' + key + '.jpeg', 'JPEG')
            print('Saved: ' + str(key) + ' to folder: ' + str(2))

        if (value == 3):
            image = Image.open(current_path + key + '.jpeg')
            image.save('H:/Bachelor data/even_distributed_data/3/' + key + '.jpeg', 'JPEG')
            print('Saved: ' + str(key) + ' to folder: ' + str(3))

        if (value == 4):
            image = Image.open(current_path + key + '.jpeg')
            image.save('H:/Bachelor data/even_distributed_data/4/' + key + '.jpeg', 'JPEG')
            print('Saved: ' + str(key) + ' to folder: ' + str(4))


move_images('H:/Bachelor data/train/')
