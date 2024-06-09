import numpy as np
import pandas as pd
import streamlit as st
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.decomposition import PCA
import pickle

# Load SVM model
model = pickle.load(open('model.pkl', 'rb'))
encoder_dict = pickle.load(open('encoder.pkl', 'rb'))
pca_weights = pickle.load(open('pca_weights.pkl', 'rb'))

cols = ['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Tuition_fees_up_to_date', 'Scholarship_holder', 'Application_mode',
        'Gender', 'Debtor', 'Age_at_enrollment']

def encode_features(df, encoder_dict):
    for feature, encoder in encoder_dict.items():
        if feature in df.columns:
            df[feature] = encoder.transform(df[feature])
    return df

def main():
    st.title("Graduation Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Graduation Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    curricular_units_2nd_sem_approved = st.text_input("Curricular Units 2nd Semester Approved", "0")
    curricular_units_2nd_sem_grade = st.text_input("Curricular Units 2nd Semester Grade", "0")
    curricular_units_1st_sem_approved = st.text_input("Curricular Units 1st Semester Approved", "0")
    curricular_units_1st_sem_grade = st.text_input("Curricular Units 1st Semester Grade", "0")
    tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ["Yes", "No"])
    scholarship_holder = st.selectbox("Scholarship Holder", ["Yes", "No"])
    application_mode = st.selectbox("Application Mode", ["Online", "Offline"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    debtor = st.selectbox("Debtor", ["Yes", "No"])
    age_at_enrollment = st.text_input("Age at Enrollment", "0")

    if st.button("Predict"):
        features = [[curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
                     curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
                     tuition_fees_up_to_date, scholarship_holder, application_mode,
                     gender, debtor, age_at_enrollment]]
        df = pd.DataFrame(features, columns=cols)

        # Encode categorical features
        df_encoded = encode_features(df.copy(), encoder_dict)

        # Apply PCA transformation
        df_pca = np.dot(df_encoded, pca_weights.T)

        # Predict
        prediction = model.predict(df_pca)

        output = int(prediction[0])
        if output == 1:
            text = "Will Graduate"
        else:
            text = "Will Dropout"

        st.success('Prediction: {}'.format(text))

if __name__ == '__main__':
    main()
