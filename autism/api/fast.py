import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
import requests
from tensorflow import keras


app = FastAPI()

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    ### PREPOCESSING   CHANGE NAME WITH ACTUAL FUNCTION NAME
    prepoc_img = preprocessor(cv2_img)

    ### Encoding and responding with the image
    im = cv2.imencode('.png', prepoc_img)[1] # extension depends on which format is sent from Streamlit
    return requests.Response(content=im.tobytes(), media_type="image/png")




@app.get('/predict')
async def predict(prepoc_img):
    model = keras.model.load_model('./model/model_homemade.h5')
    pred = model.predict(prepoc_img)
    return pred





@app.get("/")
def root():
    """
    Root endpoint for the API.
    """
    return {"greeting": "Hello"}
