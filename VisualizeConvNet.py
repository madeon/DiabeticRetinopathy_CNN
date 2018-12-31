
from convnet_drawer import Model, Conv2D, MaxPooling2D, Flatten, Dense


def create_model():
    model = Model(input_shape=(256, 256, 3))

    #16
    model.add(Conv2D(16, (3, 3), (1, 1), padding='same'))
    model.add(Conv2D(16, (3, 3), (1, 1), padding='same'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))


    #32
    model.add(Conv2D(32, (3, 3), (1, 1), padding='same'))
    model.add(Conv2D(32, (3, 3), (1, 1), padding='same'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    #64
    model.add(Conv2D(64, (3, 3), (1, 1), padding='same'))
    model.add(Conv2D(64, (3, 3), (1, 1), padding='same'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    #96
    model.add(Conv2D(96, (3, 3), (1, 1), padding='same'))
    model.add(Conv2D(96, (3, 3), (1, 1), padding='same'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    #128
    model.add(Conv2D(128, (3, 3), (1, 1), padding='same'))
    model.add(Conv2D(128, (3, 3), (1, 1), padding='same'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(Flatten())
    model.add(Dense(96))
    model.add(Dense(5))

    # save as svg file
    model.save_fig("example5.svg")






create_model()
