
# coding: utf-8



#Imports
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt


#from
from keras.optimizers import Adam
from tqdm import tqdm
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten, Activation, BatchNormalization
from sklearn.model_selection import train_test_split
from keras.callbacks import ModelCheckpoint





#Variables
img_size = 256
img_size = 256
classes = 5
epochs = 75
batch_size = 32





x_img = []
y_label = []

model = Sequential()





#Import label data
labels = pd.read_csv('/floyd/input/trainlabels/trainLabels.csv')
label_series = pd.Series(labels['level'])
dummy_labels = pd.get_dummies(label_series, sparse = True)
labels_to_array = np.asarray(dummy_labels)





#Add labels and images

print('Adding labels.')
i = 0
for f, breed in tqdm(labels.values):
    if type(cv2.imread('/floyd/input/retina_images_30k_new2/{}.jpeg'.format(f)))==type(None):
        continue
    else:
        img = cv2.imread('/floyd/input/retina_images_30k_new2/{}.jpeg'.format(f))
        label = labels_to_array[i]
        x_img.append(img)
        y_label.append(label)
        i += 1

print(i)
print('Labels added.')
print('Amount of images: ')
print(len(x_img))
print('Amount of labels: ')
print(len(y_label))



#Convert to raw data
x_train_raw = np.array(x_img, np.float32) / 255 #divide by 255 to get the RGB value in a range between 0.0 and 1.0 instead of 255
y_train_raw = np.array(y_label, np.uint8)

# split dataset for training and validation
x_train, x_test, y_train, y_test = train_test_split(x_train_raw, y_train_raw, test_size=0.2)



def create_model():
    print('Creating model')
    ### 16
    model.add(Conv2D(16, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(16, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=3, strides=2))

    ### 32
    model.add(Conv2D(32, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=3, strides=2))

    ### 64
    model.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=3, strides=2))

    ### 96
    model.add(Conv2D(96, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(Conv2D(96, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=3, strides=2))

    ### 128
    model.add(Conv2D(128, (3, 3), strides=1, padding='same', activation='relu', input_shape=(256, 256, 3)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=3, strides=2))

    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(96, activation='relu'))
    model.add(Dense(5, activation='softmax'))
    print('Model created')


#Create model
create_model()


#Compile model
opt = Adam(lr=0.0001)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])


#Weights
class_weights = {0: 1.0,
                1: 8.46,
                2: 3.90,
                3: 23.69,
                4: 29.21}

history = model.fit(x_train, y_train, verbose=2, batch_size=batch_size, class_weight=class_weights, epochs=epochs, validation_data=(x_test, y_test))

model.save('21-12-2019.h5')
