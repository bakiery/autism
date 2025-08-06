# Facial Assessment Tool – Autism Face Detection

<img width="365" alt="autism_logo" src="https://github.com/bakiery/autism/assets/128114576/189f2f8d-ed41-41eb-a3bb-eb49c0bd16c5">

**[Try the Live Tool →](https://ismychildautistic.streamlit.app/)**

---

## About

The Facial Assessment Tool is a web application for the automated analysis of child facial morphology, estimating the likelihood of autism spectrum disorder (ASD)–associated features. Built with a custom machine learning pipeline, the tool applies convolutional neural networks (CNNs) to image uploads and provides a probability-based assessment.

> **Disclaimer:**  
> This application is a research prototype intended for informational and experimental use only. It is not a diagnostic tool, and clinical decisions should not be made based on its output. For formal assessment, consult a qualified healthcare professional.

---

## Features

- **Facial Image Upload:** Intuitive interface for submitting child facial images.
- **Automated Analysis:** End-to-end facial feature extraction and prediction using CNNs.
- **Likelihood Scoring:** Probability output and clear classification thresholds.
- **Result Visualization:** Graphical display of results and interpretive feedback.

---

## Score Interpretation

- **Score below 30%:** Low likelihood of ASD-associated facial features.
- **Score between 30–70%:** Moderate likelihood.
- **Score above 70%:** High likelihood.

*Note: Model validation accuracy is 90% on test data. Real-world accuracy may be lower; results should be interpreted cautiously. Try multiple images for a more robust assessment.*

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd facial-assessment-tool
    ```

2. **Install dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

3. **Set up the backend:**
    - Configure the API endpoint URL in `backend/app.py` to match your deployment.
    - Ensure the machine learning model weights are present in `backend/model.py`.

4. **Run the backend:**
    ```bash
    cd backend
    python app.py
    ```

5. **Launch the frontend:**
    - Open your web browser and visit `http://localhost:8000` to use the tool.

---

## Dependencies

- All backend dependencies are listed in `backend/requirements.txt`.
    ```bash
    pip install -r backend/requirements.txt
    ```
- The frontend uses Streamlit (installed via requirements).

---

## Usage

1. Open the Facial Assessment Tool in your browser or use the [live demo](https://ismychildautistic.streamlit.app/).
2. Upload a child's facial image via the interface.
3. Wait for the automated analysis and result visualization.
4. View the probability score and interpretation.
5. Repeat with other images as needed.

---

## Data

- Dataset (source: `gpiosenka`) can be downloaded [here (Google Drive)](https://drive.google.com/drive/folders/1XQU0pluL0m3TIlXqntano12d68peMb8A).
- All data used is public/open source.

---

## References

1. **Rahman, K.K., & Subashini, M.M.**  
   [Identification of Autism in Children Using Static Facial Features and Deep Neural Networks.](https://doi.org/10.3390/brainsci12010094)  
   *Brain Sci*, 12(1), 2022, 94. PMID: 35053837; PMCID: PMC8773918.

2. **Hosseini, M.-P., et al.**  
   [Deep Learning for Autism Diagnosis and Facial Analysis in Children.](https://doi.org/10.3389/fncom.2021.789998)  
   *Frontiers in Computational Neuroscience*, 15, 2022, 789998.

3. **Scott, N.J., et al.**  
   [Facial dimorphism in autistic quotient scores.](https://doi.org/10.1177/2167702614534238)  
   *Clinical Psychological Science*, 3(2), 2015, 230–241.

---

## Credits

Original authors: [bakiery](#), [jake-humphreys](#), [alex-mazheika](#), [Xavrob123](#).  
Ongoing maintenance and development by [bakiery](#).

---

## License

MIT License. See `LICENSE` for full details.
