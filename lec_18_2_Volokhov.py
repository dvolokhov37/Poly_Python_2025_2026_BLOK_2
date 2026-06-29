from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
import numpy as np

img_path = "cat.png"
# img_path = "dog.png"

img = image.load_img(img_path, target_size=(224, 224))

img_array = image.img_to_array(img)
imgbatch = np.expand_dims(img_array, axis = 0)

from tensorflow.keras.applications.resnet50 import preprocess_input

img_preprocessed = preprocess_input(img_batch)

model = load_model("our_model.h5")

prediction = model.predict(img_preprocessed)

print(prediction)

# Важно: картинку надо всегда провести через нормализацию
# можем модель частично дообучить и частично или полностью поменять способ предсказания