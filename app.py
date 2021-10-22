from __future__ import division, print_function

import sys
import os
import glob
import re

import numpy as np
import tensorflow as tf
import cv2

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

MODEL_PATH ='stjmodel.h5'

model = load_model(MODEL_PATH)


def model_predict(img_path,model):
    
    img = image.load_img(img_path, target_size=(256, 256))
    
    # Preprocessing the image
    x = image.img_to_array(img)
    
    x=x/255
    
    x = np.expand_dims(x, axis=0)
    
    predict = model.predict(x)
    
    predict = np.argmax(predict, axis=1)
    
    
    if predict == 0:
        
        predict = "The chosen image is a Saree for Women"
        
    elif predict == 1:
        
        predict = "The chosen image is a Trouser for Men"
        
    elif predict == 2:
        
        predict = "The chosen image is a Jeans for Men"
        
    else:
        
        predict = "Sorry No results found!"
            
    
    return predict
        
    


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])

def upload():
    if request.method == 'POST':
        
        f = request.files['file']
        
        basepath = os.path.dirname(__file__)
        
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        
        f.save(file_path)
        
        predict = model_predict(file_path,model)
        
        result = predict
        
        return result
    
    return None


if __name__ == '__main__':
    
    app.run(port=5001,debug=True)







