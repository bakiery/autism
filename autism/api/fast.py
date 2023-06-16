import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
import requests
from tensorflow import keras
from autism.ml_logic import main, model, preprocessor


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

@app.post('/test')
def test_image(img: UploadFile=File(...)):
    import base64, io
    from PIL import Image

    im_bytes = img.file.read()
    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    img_c = Image.open(io.BytesIO(img_bytes))
    img_arr = np.asarray(img_c)

    im_resized = preprocessor.resize_58x64(img_arr)
    mdl = model.load_local_model()
    prediction = main.model_prediction(mdl, im_resized)
    prediction = float(prediction)

    return f'autism probability: {round(prediction,2)}'
