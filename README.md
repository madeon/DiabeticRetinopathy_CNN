# Diabetic Retinopathy

This project was developed by Mathias Gundertofte (magun15).



## The project idea


The idea of the project is to use Convolutional Neural Networks to detect signs of Diabetic Retinopathy in retina images from the kaggle competition - https://www.kaggle.com/c/diabetic-retinopathy-detection

Each image must be classified using the following scale:

0 - No DR
1 - Mild
2 - Moderate
3 - Severe
4 - Proliferative DR


## Pre-processing

The original dataset contained 35.126 images in different sizes, shapes and colors. The image distribution is as follows:

| Class         | Name          | Number of images | Percentage |
| ------------- | ------------- | ---------------- | ---------- |
| 0             | No DR         | 25.810           | 73.5%      |
| 1             | Mild DR       | 2443             | 7%         |
| 2             | Moderate DR   | 5292             | 15%        |
| 3             | Severe DR     | 873              | 2.5%       |
| 4             | Proliferative DR | 708           | 2%         |
|Total          | -             | 35.126           | 100%       |

## Training

## Built With

* [TensorFlow] Backend for the Convolutional Neural Network
* [Keras] - 
* [PyCharm] - IDE
* [OpenCV] - Image

