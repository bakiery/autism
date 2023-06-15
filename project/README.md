# Facial Assessment Tool

The Facial Assessment Tool is a web application that allows users to upload an image of a child and assess the likelihood of autism based on facial morphology. The tool uses a machine learning model trained on facial features to make predictions.

## Features

- Upload an image of a child for assessment
- Perform facial analysis using the trained machine learning model
- Display the likelihood of being autistic based on facial morphology
- Visualize the classification result and probability

## Installation

1. Clone the repository:
git clone <repository-url>


2. Install the required dependencies:
cd facial-assessment-tool
pip install -r backend/requirements.txt


3. Set up the backend:
- Configure the API endpoint URL in `backend/app.py` to match your deployment environment.
- Ensure the machine learning model and weights are available in the `backend/model.py` file.

4. Run the application:
cd backend
python app.py


5. Access the application:
Open your web browser and visit `http://localhost:8000` to access the Facial Assessment Tool.

## Dependencies

The dependencies for the backend are listed in the `backend/requirements.txt` file. You can install them using the following command:
pip install -r backend/requirements.txt



The frontend uses Streamlit, which will be installed automatically as a dependency for the backend.

## Usage

1. Open the Facial Assessment Tool in your web browser.
2. Upload an image of a child by clicking the "Upload an image" button.
3. Wait for the tool to process the image and display the prediction result.
4. The tool will show the likelihood of being autistic based on facial morphology and the classification result.
5. Explore the app and try different images for assessment.

## Citation

This tool is based on research papers conducted by Naomi Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, Robert Ward, Mohammad-Parsa Hosseini, Madison Beary, Alex Hadsell,
Ryan Messersmith, Hamid Soltanian-Zadeh, K.K. Mujeeb Rahman, and M. Monica Subashini. You can find the studies at the following links:

- [Bangor University Study](https://ward-lab.bangor.ac.uk/pubs/Scott_Ward_14_AQ.pdf)
- [Deep Learning for Autism Diagnosis and Facial Analysis in Children](https://www.frontiersin.org/articles/10.3389/fncom.2021.789998/full)
- [Identification of Autism in Children Using Static Facial Features and Deep Neural Networks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773918/)

**Disclaimer:** Please note that this tool is provided for informational purposes only and is not a diagnostic tool. It assesses the likelihood of autism based on facial morphology, but a formal diagnosis should be made by a qualified healthcare professional.
