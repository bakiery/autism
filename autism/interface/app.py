# interface


# transform uploaded image to bytes or base64
# send the transformed image to the api using requests.post (requests library, post method)
# get back the prediction, take it out of the json string, display it

import streamlit as st
import requests
import base64
from PIL import Image

# Set the API endpoint URL
API_ENDPOINT = "http://your-api-endpoint"

# Step 1: Load the trained CNN model
#cnn_model = load_model('path_to_trained_cnn_model.h5')
#NEED TO PROVIDE THE PATH TO THE CNN MODEL HERE BEFORE I UNCOMMENT THE COMMENTED LINES

# Step 2: Define functions for preprocessing and prediction
def preprocess_image(image):
    # Preprocess the image (resize, normalize, etc.)
    # Add your preprocessing steps here
    processed_image = ...

    return processed_image

def get_prediction(image_bytes):
    # Convert image bytes to base64 string
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Prepare the request payload
    payload = {
        "image": image_base64
    }

    # Send POST request to the API endpoint
    response = requests.post(API_ENDPOINT, json=payload)

    # Extract the prediction result from the response
    result = response.json()["prediction"]

    return result

def perform_facial_assessment(image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Perform facial assessment using the trained CNN model
    #cnn_prediction = cnn_model.predict(processed_image)

    # Display the prediction result and probability
    st.subheader('Detection Result:')
    #autistic_probability = cnn_prediction[0][0] * 100
    #not_autistic_probability = 100 - autistic_probability

    #st.success(f'Likelihood of being autistic: {autistic_probability:.2f}%')
    #st.info(f'Likelihood of not being autistic: {not_autistic_probability:.2f}%')

    #if autistic_probability > 50:
    #    st.info('Classification: Autistic')
    #else:
    #    st.info('Classification: Not Autistic')

# Step 3: Create the Streamlit app
def main():
    st.set_page_config(
        page_title="Facial Assessment Tool",
        page_icon="🧩",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title('Facial Assessment Tool')

    # Add the custom CSS styles
    st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)

    # Display the introduction and instructions
    st.markdown('''
        ## Facial Assessment Tool
        Upload an image of a child to assess the likelihood of autism based on facial morphology.
        ''')

    # Upload image
    uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Read image file
        image = Image.open(uploaded_file)

        # Perform facial assessment using the trained model
        perform_facial_assessment(image)

# Step 4: Run the Streamlit app
if __name__ == '__main__':
    main()
