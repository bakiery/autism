# Facial Assessment Tool

The Facial Assessment Tool is a web application that allows users to upload an image of a child and assess the likelihood of autism based on facial morphology. The tool uses a machine learning model trained on facial features to make predictions.

## Overview
Detect autism in children using CNNs. Analyze facial features to accurately identify autism. Preprocessing, model development, evaluation. Reliable diagnostic tool for early intervention.

## Features

- Upload an image of a child for assessment
- Perform facial analysis using the trained machine learning model
- Display the likelihood of being autistic based on facial morphology
- Visualize the classification result and probability

## Interpretation of Scores
- Score below 30%:
Indicates a lower likelihood of ASD-related facial features.
- Score between 30% to 70%:
Suggests a moderate likelihood of ASD-related facial features.
- Score above 70%:
Indicates a higher likelihood of ASD-related facial features.

The accuracy of prediction of the model is 90%, meaning 1/10 predictions could be incorrect. Please try several images in order to ensure the suggested result is more accurate.

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

For more information and references, please refer to the studies provided:

Mujeeb Rahman KK and Subashini MM. "Identification of Autism in Children Using Static Facial Features and Deep Neural Networks." *Brain Sci*, vol. 12, no. 1, 2022, article 94. doi: [10.3390/brainsci12010094](https://doi.org/10.3390/brainsci12010094). PMID: 35053837; PMCID: PMC8773918. [1]

Mohammad-Parsa Hosseini, Madison Beary, Alex Hadsell, Ryan Messersmith and Hamid Soltanian-Zadeh. "Deep Learning for Autism Diagnosis and Facial Analysis in Children." *Frontiers in Computational Neuroscience*, vol. 15, 2022, article 789998. doi: [10.3389/fncom.2021.789998](https://doi.org/10.3389/fncom.2021.789998). ISSN: 1662-5188. [2]

Naomi Jane Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, and Robert Ward. "Facial dimorphism in autistic quotient scores." *Clinical Psychological Science*, vol. 3, no. 2, 2015, pp. 230–241. doi: [10.1177/2167702614534238](https://doi.org/10.1177/2167702614534238). [3]

**Disclaimer:** Please note that this tool is provided for informational purposes only and is not a diagnostic tool. It assesses the likelihood of autism based on facial morphology, but a formal diagnosis should be made by a qualified healthcare professional.

To download the dataset (source: gpiosenka from Kaggle) click on this link and unzip the files:
https://drive.google.com/drive/folders/1XQU0pluL0m3TIlXqntano12d68peMb8A
