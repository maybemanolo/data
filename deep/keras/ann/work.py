import numpy as np
import pandas as pd
import keras as k
from keras.models import model_from_json

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

loaded_model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])