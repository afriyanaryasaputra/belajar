import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.decomposition import PCA
import pickle

# Load SVM model
model = pickle.load(open('model.pkl', 'rb'))
encoder_dict = pickle.load(open('encoder.pkl', 'rb'))
pca_weights = pickle.load(open('pca_weights.pkl', 'rb'))

# Korelasi antar fitur
correlation_values = {
    'Curricular_units_2nd_sem_approved': 0.653995,
    'Curricular_units_2nd_sem_grade': 0.605350,
    'Curricular_units_1st_sem_approved': 0.554881,
    'Curricular_units_1st_sem_grade': 0.519927,
    'Tuition_fees_up_to_date': 0.442138,
    'Scholarship_holder': 0.313018,
    'Application_mode': -0.244507,
    'Gender': -0.251955,
    'Debtor': -0.267207,
    'Age_at_enrollment': -0.267229
}

cols = list(correlation_values.keys())

def encode_features(df, encoder_dict):
    for feature, encoder in encoder_dict.items():
        if feature in df.columns:
            # Tambahkan penanganan nilai tidak dikenal
            df[feature] = df[feature].apply(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else encoder.transform([encoder.classes_[0]])[0])
    return df

def scale_features(df):
    scaler = preprocessing.StandardScaler()
    scaled_features = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_features, columns=df.columns)
    return df_scaled

def main():
    st.title("Jaya Jaya Institut")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Graduation Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Menambahkan heatmap korelasi
    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(pd.DataFrame(correlation_values, index=[0]).T, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    st.pyplot()

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
        # Encode categorical features
        features = [[curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
                     curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
                     tuition_fees_up_to_date, scholarship_holder, application_mode,
                     gender, debtor, age_at_enrollment]]
        df = pd.DataFrame(features, columns=cols)

        df = encode_features(df, encoder_dict)

        # Convert categorical features to numerical
        df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].map({'Yes': 1, 'No': 0})

        for col in ['Scholarship_holder', 'Application_mode', 'Gender', 'Debtor']:
            df[col] = df[col].map({'Yes': 1, 'No': 0})

        # Scale numerical features
        df_scaled = scale_features(df[['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
                                        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                                        'Age_at_enrollment']])

        df_final = pd.concat([df_scaled, df.drop(['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
                                                  'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                                                  'Age_at_enrollment'], axis=1)], axis=1)

        # Predict
        prediction = model.predict(df_final)

        output = int(prediction[0])
        if output == 1:
            text = "Will Graduate"
        else:
            text = "Will Dropout"

        st.success('Prediction: {}'.format(text))

if __name__ == '__main__':
    main()
