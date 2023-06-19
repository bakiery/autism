# interface


# transform uploaded image to bytes or base64
# send the transformed image to the api using requests.post (requests library, post method)
# get back the prediction, take it out of the json string, display it

import streamlit as st
import requests
import base64
from PIL import Image
import os

# Set the API endpoint URL
API_ENDPOINT = "https://autsim-wq7gvazpga-uc.a.run.app/"

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
    result = response.json()

    return result

def perform_facial_assessment(image):
    # Get prediction from API
    prediction = get_prediction(image)

    # Extract probabilities for autistic and not autistic
    autistic_probability = prediction["autistic"]
    not_autistic_probability = prediction["not_autistic"]

    # Normalize probabilities to sum up to 1.0
    total_probability = autistic_probability + not_autistic_probability
    autistic_probability /= total_probability
    not_autistic_probability /= total_probability

    # Display the prediction result and probability
    st.subheader('Detection Result:')
    st.success(f'Likelihood of being autistic: {autistic_probability:.2f}')
    st.info(f'Likelihood of not being autistic: {not_autistic_probability:.2f}')

def main():
    st.set_page_config(
        page_title="Facial Assessment Tool",
        page_icon="🧩",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title('Facial Assessment Tool')

    # Check if the 'styles.css' file exists
    css_file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    if not os.path.isfile(css_file_path):
        st.warning("The 'styles.css' file is missing. Please make sure it exists in the same directory as the script.")
    else:
        # Add the custom CSS styles
        with open(css_file_path) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

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

        # Perform facial assessment using the API
        perform_facial_assessment(image)

if __name__ == '__main__':
    main()
