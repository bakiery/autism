import pandas as pd
# $WIPE_BEGIN

# Import necessary modules for the autism project
from autism.ml_logic.registry import load_model
from autism.ml_logic.preprocessor import preprocess_image
# $WIPE_END

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# $WIPE_BEGIN
# 💡 Preload the model to accelerate the predictions
# We want to avoid loading the heavy Deep Learning model from MLflow at each `post("/predict")` request
# The trick is to load the model in memory when the Uvicorn server starts
# and then store the model in an `app.state.model` global variable, accessible across all routes!
# This will improve the inference performance of the API.

# Load the model and store it in the app state
app.state.model = load_model()
# $WIPE_END

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Make a single prediction for the uploaded image file.
    """

    # Preprocess the uploaded image file
    contents = await file.read()
    image = preprocess_image(contents)

    # Perform the prediction using the loaded model
    model = app.state.model
    assert model is not None
    prediction = model.predict(image)

    # Normalize the prediction probabilities
    total_prob = prediction.sum()
    prediction /= total_prob

    # Return the prediction result
    return {
        "autistic": float(prediction[0]),
        "not_autistic": float(prediction[1])
    }

@app.get("/")
def root():
    """
    Root endpoint for the API.
    """
    return {"greeting": "Hello"}
