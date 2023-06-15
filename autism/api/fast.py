import numpy as np
import cv2
from fastapi import FastAPI, File, UploadFile
import requests
from autism.ml_logic import main, model, preprocessor


app = FastAPI()

@app.post('/upload_image')
async def receive_image(img: UploadFile=File(...)):   #################################### WHATS GOING ON HERE ?
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    ### Do cool stuff with your image.... For example face detection
    annotated_img = annotate_face(cv2_img) ############################################### WHATS GOING ON HERE ? DOESNT CONCERN US ?

    ### Encoding and responding with the image
    im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
    return Response(content=im.tobytes(), media_type="image/png")




@app.post('/predict')
async def receive_image(img: UploadFile=File(...)):   #################################### WHATS GOING ON HERE ?
    ### Receiving and decoding the image
    contents = await img.read()

    nparr = np.fromstring(contents, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type(cv2_img) => numpy.ndarray

    ### Do cool stuff with your image.... For example face detection
    annotated_img = annotate_face(cv2_img) ############################################### WHATS GOING ON HERE ? DOESNT CONCERN US ?

    ### Encoding and responding with the image
    im = cv2.imencode('.png', annotated_img)[1] # extension depends on which format is sent from Streamlit
    return Response(content=im.tobytes(), media_type="image/png")

@app.post('/test')
def receive_image(img: UploadFile=File(...)):
    im_resized = preprocessor.resize_58x64(img)
    mdl = model.load_local_model()
    prediction = main.model_prediction(mdl, im_resized)
    return prediction
