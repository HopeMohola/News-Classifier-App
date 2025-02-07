import streamlit as st
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load all the models
log_reg_model = joblib.load("optimized_log_reg_model.pkl")
svm_model = joblib.load("optimized_svm_model.pkl")
naive_bayes_model = joblib.load("optimized_nb_model.pkl")
random_forest_model = joblib.load("optimized_rf_model.pkl")

# Load the TF-IDF vectorizer
tfidf_vectorizer = joblib.load("optimized_tfidf_vectorizer.pkl")

# Dictionary to map model names to actual models
models = {
    "Logistic Regression": log_reg_model,
    "SVM (Support Vector Machine)": svm_model,
    "Naïve Bayes": naive_bayes_model,
    "Random Forest": random_forest_model
}

# Streamlit UI
st.title("📰 News Classification App")
st.write("Enter a news headline or article content and choose a model to classify it.")

# User Input
user_input = st.text_area("Enter News Content Here:", height=100)

# Model Selection
model_option = st.selectbox("Choose a Model:", list(models.keys()) + ["Compare All Models"])

# Predict Button
if st.button("Classify News"):
    if user_input:
        # Vectorize the user input
        input_tfidf = tfidf_vectorizer.transform([user_input])

        if model_option == "Compare All Models":
            st.subheader("🔍 Model Comparison")
            for model_name, model in models.items():
                prediction = model.predict(input_tfidf)[0]
                prediction_prob = model.predict_proba(input_tfidf)
                confidence = np.max(prediction_prob) * 100

                st.write(f"**{model_name}:**")
                st.write(f"➡️ **Predicted Category:** {prediction}")
                st.write(f"📊 **Confidence:** {confidence:.2f}%")
                st.markdown("---")

        else:
            # Get prediction for the selected model
            selected_model = models[model_option]
            prediction = selected_model.predict(input_tfidf)[0]
            prediction_prob = selected_model.predict_proba(input_tfidf)
            confidence = np.max(prediction_prob) * 100

            # Display result
            st.subheader("🔍 Prediction Result")
            st.write(f"**Model Used:** {model_option}")
            st.write(f"➡️ **Predicted Category:** {prediction}")
            st.write(f"📊 **Confidence:** {confidence:.2f}%")
    
    else:
        st.warning("⚠️ Please enter some news content before classifying.")

