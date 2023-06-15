import base64
import requests
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

# file that connects everything together
# Please note that this is a Markdown representation of the code. To use the code, copy it into a Python file (e.g., `main.py`), making sure to replace `'path_to_trained_cnn_model.h5'` with the actual path to your trained CNN model file.

def model_prediction(mdl, image):
    '''model - keras CNN model
    image - np.array
    Returns: prediction'''

    #input_image = '/home/alex/code/bakiery/Autism-in-Children-A-CNN-Approach/raw_data/autism/test/non_autistic/001.jpg'
    #image = preprocessor.resize_58x64(input_image)
    #mdl = model.load_local_model()

    image = image/255
    image = np.array([image])
    prediction = mdl.predict(image)[0][0]

    return prediction

# Step 1: Load the trained CNN model
cnn_model = load_model('path_to_trained_cnn_model.h5')

# Step 2: Define functions for performing facial assessment
def preprocess_image(image):
    # Preprocess the image (resize, normalize, etc.)
    # Add your preprocessing steps here
    processed_image = ...

    return processed_image

def perform_facial_assessment(image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Perform facial assessment using the trained CNN model
    cnn_prediction = cnn_model.predict(processed_image)

    # Display the prediction result and probability
    st.subheader('Detection Result:')
    autistic_probability = cnn_prediction[0][0] * 100
    not_autistic_probability = 100 - autistic_probability

    st.success(f'Likelihood of being autistic: {autistic_probability:.2f}%')
    st.info(f'Likelihood of not being autistic: {not_autistic_probability:.2f}%')

    if autistic_probability > 50:
        st.info('Classification: Autistic')
    else:
        st.info('Classification: Not Autistic')


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

    # Citation
    st.markdown('''
        This tool is based on research papers conducted by Naomi Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, Robert Ward, Mohammad-Parsa Hosseini, Madison Beary, Alex Hadsell,
        Ryan Messersmith, Hamid Soltanian-Zadeh, K.K. Mujeeb Rahman and M. Monica Subashini. You can find the studies at the following links:

        - [Bangor University Study](https://ward-lab.bangor.ac.uk/pubs/Scott_Ward_14_AQ.pdf)
        - [Deep Learning for Autism Diagnosis and Facial Analysis in Children](https://www.frontiersin.org/articles/10.3389/fncom.2021.789998/full)
        - [Identification of Autism in Children Using Static Facial Features and Deep Neural Networks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773918/)

        Please note that this tool is provided for informational purposes only and is not a diagnostic tool. It assesses the likelihood of autism based on facial morphology, but a formal diagnosis should be made by a qualified healthcare professional.
        ''')

# Step 4: Run the Streamlit app
if __name__ == '__main__':
    main()
