from django.conf import settings
from tensorflow.keras import models
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image # pillow
import cv2 # opencv-python


def predict_mnist_one(path):

    base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL # == './media/'
    model_url = base_url + 'mnist_2layer_bn.h5'
    model = models.load_model(model_url, compile=False)

    img = cv2.imread(path, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))

    sample_one = np.reshape(img, (1, 28*28))
    predict_result = np.argmax(model.predict(sample_one))

    return predict_result
