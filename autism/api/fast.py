import numpy as np
import cv2
import fastapi
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
import requests
#from tensorflow.keras.models import load_model
from tensorflow import keras
from keras.models import load_model
from PIL import Image
from numpy import asarray
import numpy as np
import io

app = FastAPI()

app.state.model = load_model('autism/api/model/model_accuracy.h5')

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],  # Allows all origins
     allow_credentials=True,
     allow_methods=["*"],  # Allows all methods
     allow_headers=["*"],  # Allows all headers
 )
@app.get("/")
def root():
    """
    Root endpoint for the API.
    """
    return {"status": "ok"}
@app.post('/predict_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    img = img.file
    img = Image.open(img).convert('RGB')
    img = img.resize((256, 256))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    print(img.shape)
    model = app.state.model
    assert model is not None
    pred = model.predict(img)
    return {"prediction": pred.tolist()}
