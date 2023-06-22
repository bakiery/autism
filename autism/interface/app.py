# interface
import streamlit as st
import requests
from PIL import Image
import os


# Set the API endpoint URL
API_URL = "https://autsim-wq7gvazpga-ew.a.run.app/"
API_ENDPOINT = API_URL + "predict_image"

def get_prediction(image_bytes):
    # Send POST request to the API endpoint
    response = requests.post(API_ENDPOINT, files={"img": image_bytes.getvalue()})

    # Extract the prediction result from the response
    result = response.json()

    return result

def main():
    # Load the logo image
    logo_image = Image.open("autistic_logo_light.png")

    # Resize the logo image
    current_width, current_height = logo_image.size
    max_width = 200  # Specify the maximum width of the resized logo
    max_height = 100  # Specify the maximum height of the resized logo

    # Calculate the aspect ratio
    aspect_ratio = current_width / current_height

    # Calculate the resized dimensions based on the maximum width or height
    if current_width > current_height:
        # If the current image is wider
        desired_width = min(current_width, max_width)
        desired_height = int(desired_width / aspect_ratio)
    else:
        # If the current image is taller or square
        desired_height = min(current_height, max_height)
        desired_width = int(desired_height * aspect_ratio)

    # Resize the logo image
    logo_image_resized = logo_image.resize((desired_width, desired_height))

    st.set_page_config(
        page_title="Is My Child Autistic?",
        page_icon="🧩",
        layout="wide",
        initial_sidebar_state="auto",
    )
    # Place the resized logo image in the sidebar
    st.sidebar.image(logo_image_resized)

    # Display the title in the main section
    st.write('<h2 style="color: #F74F9C;"> Is My Child Autistic? </h2>', unsafe_allow_html=True)
    st.markdown("<div style='background-color: #2E86EF; height: 5px'></div>", unsafe_allow_html = True)
    st.write ('Find out the possibility of your child having autism with AI facial detection')
    # Check if the 'styles.css' file exists
    css_file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    if not os.path.isfile(css_file_path):
        st.warning("The 'styles.css' file is missing. Please make sure it exists in the same directory as the script.")
    else:
        # Add the custom CSS styles
        with open(css_file_path) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    # Sidebar navigation
    pages = ['Home', 'About']
    page = st.sidebar.selectbox('Navigate', options=pages)

    if page == 'Home':

        # Upload image
        uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

        if uploaded_file is not None:
            # Read image file
            image = Image.open(uploaded_file)
            st.image(image)

            # Perform facial assessment using the API
            result = get_prediction(uploaded_file)
            probability_percentage = round(result["prediction"][0][0] * 100, 2)
            st.subheader(f'Probability of Autism: {probability_percentage}%')

        st.write('<h3 style="color: #2E86EF;"> Interpretation of Scores </h3>', unsafe_allow_html=True)
        st.markdown('''
    - **Score below 30%:** <br> Indicates a lower likelihood of ASD-related facial features.
    - **Score between 30% to 70%:**<br> Suggests a moderate likelihood of ASD-related facial features.
    - **Score above 70%:**<br> Indicates a higher likelihood of ASD-related facial features.
''', unsafe_allow_html=True)

        st.write('<h3 style="color: #2E86EF;"> Background </h3>', unsafe_allow_html=True)
        st.markdown('''
    This tool is designed to provide information about facial features associated with Autism Spectrum Disorder (ASD). It will analyze the facial features based on research findings related to ASD.

    Please remember that this tool is for informational purposes only and should not be used as a diagnostic tool. A formal diagnosis of autism should be made by a qualified healthcare professional.

            ''', unsafe_allow_html=True)

    elif page == 'About':
        st.write('<h3 style="color: #2E86EF;"> Understanding Facial Features Associated with Autism Spectrum Disorder (ASD) </h3>', unsafe_allow_html=True)
        st.markdown('''
    Recent studies have identified certain facial features that are commonly observed in children with Autism Spectrum Disorder (ASD). These features include a broader top face, a shorter midface, eyes with a wider palpebral fissure length (PFL) and interpupillary distance (IPD), a wider mouth, and a shorter and wider philtrum (the groove between the nose and top lip)[1].

    Moreover, there are suggestions from other sources that indicate a potential association between ASD and other features such as larger lips and small tufting in spots at the hairline. However, it's important to note that these features are not universally present in individuals with autism and require further verification through additional research.

    Baron-Cohen’s extreme male brain theory proposes that autism results from elevated prenatal testosterone levels. In a separate study [2] on adult morphology and facial features associated with masculinity, researchers created composite images capturing statistical regularities in facial appearance linked to high and low Autism-Spectrum Quotient (AQ) scores. However, given the lack of available, verificable data, this model has not been trained on autistic adult faces.

    It's worth mentioning that these facial features associated with autism are generally subtle and may not be noticeably distinct to the average observer. Additionally, the presence of these features can vary within the autistic population, as autism itself encompasses a range of characteristics.

    Please note that this tool is for informational purposes only and should not be used as a diagnostic tool. A formal diagnosis of autism should be made by a qualified healthcare professional.
    ''')

    st.write('<h3 style="color: #2E86EF;"> References </h3>', unsafe_allow_html=True)
    st.markdown('''
    For more information and references, please refer to the studies provided:

    - Mujeeb Rahman KK and Subashini MM. "Identification of Autism in Children Using Static Facial Features and Deep Neural Networks." *Brain Sci*, vol. 12, no. 1, 2022, article 94. doi: [10.3390/brainsci12010094](https://doi.org/10.3390/brainsci12010094). PMID: 35053837; PMCID: PMC8773918. [1]

    - Naomi Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, and Robert Ward. "Deep Learning for Autism Diagnosis and Facial Analysis in Children." *Frontiers in Computational Neuroscience*, vol. 15, 2022, article 789998. doi: [10.3389/fncom.2021.789998](https://doi.org/10.3389/fncom.2021.789998). ISSN: 1662-5188. [2]

    - Naomi Jane Scott, Alex Lee Jones, Robin Stewart Samuel Kramer, and Robert Ward. "Facial dimorphism in autistic quotient scores." *Clinical Psychological Science*, vol. 3, no. 2, 2015, pp. 230–241. doi: [10.1177/2167702614534238](https://doi.org/10.1177/2167702614534238). [3]
    ''')

if __name__ == '__main__':
    main()
