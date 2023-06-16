import numpy as np
from fastapi import FastAPI, File, UploadFile
import requests
from fastapi.middleware.cors import CORSMiddleware
import io
import json
import base64
import logging
import numpy as np
from PIL import Image
#from tensorflow import keras
import models
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allows all origins
    allow_credentials=True,
    allow_methods=['*'],  # Allows all methods
    allow_headers=['*'],  # Allows all headers
)

@app.get('/')
def test():
    return {'hello' : 'friend'}

# @app.post('/upload_image_predict')
# def test_image(img: UploadFile=File(...)):
#     with open(img, "rb") as f:
#         im_bytes = f.read()
#         im_b64 = base64.b64encode(im_bytes).decode("utf8")
#         img_bytes = base64.b64decode(im_b64.encode('utf-8'))
#         # convert bytes data to PIL Image object
#         img = Image.open(io.BytesIO(img_bytes))
#         img = img.resize((256,256))
#         # PIL image object to numpy array
#         img_arr = np.asarray(img)
#         model = keras.models.load_model('models/model_homemade.h5')
#         prediction = model.predict(img_arr)

#         return f'autism prediction : {prediction}'
