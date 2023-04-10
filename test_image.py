# -*- coding: utf-8 -*-
"""
Author: Peter Nguyen and Chris Pham
"""

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

#Modules used to operate program
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

#Categories availiable for recognization
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def load_image(filename):
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = img.reshape(1, 32, 32, 3)
    img = img / 255.0
    return img

#Locate CIFAR Model File
model = load_model('Peterpoo3_CIFARmodel_baseline.h5')

#Set URLs for Image Recognization
URLs = [
    "https://ichef.bbci.co.uk/news/976/cpsprodpb/67CF/production/_108857562_mediaitem108857561.jpg",
    "https://s.yimg.com/ny/api/res/1.2/Cfxa5_BigR_CFmWzq83UUg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTM2MA--/https://media.zenfs.com/en/gobankingrates_644/bb21b2da85b65c42c75de0eece434e69",
    "https://cbsnews2.cbsistatic.com/hub/i/r/2017/03/27/73bd41ff-5703-48ca-995c-131d1b3572b4/thumbnail/640x335/10f4b442d725b8fa79d3e2dbf286ba76/air-force-one-two-planes.jpg",
    "data:image/jpeg;base64,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",
    "https://wagznwhiskerz.com/wp-content/uploads/2017/10/home-cat.jpg"
]

#Runs program to recognize each image, predict each class for image, and generates prediction for each result
for url in URLs:
    #Gather images off URL
    picture_path = tf.keras.utils.get_file(origin=url)
    img = load_image(picture_path)
    result = model.predict(img)

    #Plots pictures onto Plots
    image = plt.imread(picture_path)
    plt.imshow(image)
    plt.title("Prediction: " + class_names[int(result.argmax(axis=-1))])
    plt.axis('off')
    plt.show()