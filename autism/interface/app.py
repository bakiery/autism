# interface


# transform uploaded image to bytes or base64
# send the transformed image to the api using requests.post (requests library, post method)
# get back the prediction, take it out of the json string, display it

import streamlit as st
import requests
import base64

# Set the API endpoint URL
API_ENDPOINT = "http://your-api-endpoint" #The people with the backend will know. You will simulate the API on the computer to test if it's working before you upload.

# Function to send the image to the API and get the prediction
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

# Streamlit app
def main():
    # Set app title
    st.title("Autistic Child Detection")

    # File uploader for image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Perform prediction if file is uploaded
    if uploaded_file is not None:
        # Convert uploaded image to bytes
        image_bytes = uploaded_file.read()

        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Button to trigger the prediction
        if st.button("Predict"):
            # Get the prediction result
            prediction = get_prediction(image_bytes)

            # Display the prediction result
            st.success(f"Prediction: {prediction}")

# Run the app
if __name__ == "__main__":
    main()
