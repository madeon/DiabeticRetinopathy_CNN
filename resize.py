import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image

image_size = 256


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def crop_and_resize_images(current_path, new_path):

    create_directory(new_path)
    dirs = [l for l in os.listdir(current_path) if l != '.DS_Store']
    total = 0

    #Opens each image in the directory and performs crop on each image
    for item in dirs:
        image = Image.open(current_path + item)

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

                            print("Saving: ", item, total)
                            print(x, 0, x2, image.height)
                            print(image.getpixel((x2, y2)))

                            original_image = image.crop((x, 0, x2, image.height))

                            resized_image = original_image.resize([image_size, image_size], Image.ANTIALIAS)
                            resized_image.save(os.path.join(new_path, item), 'JPEG')
                            total += 1

                            finishedRight = True
            except Exception:
                print("error: " + item)
                break


if __name__ == '__main__':
    crop_and_resize_images('H:/Bachelor data/distributed_data_set/', new_path='../data/evenly-distributed-256')
