import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from pathlib import Path

st.set_page_config(page_title="Post-Caesarean Pain Dashboard", layout="wide", initial_sidebar_state="expanded")

# Sidebar
logo_path = Path("logo.jpg")
if logo_path.exists():
    st.sidebar.image(str(logo_path), use_container_width=True)
else:
    st.sidebar.info("Add your logo file named 'logo.jpg' to show it here.")

st.sidebar.markdown("""
### Post-Caesarean Pain App  
Created by **Ebenezer Kwaw**   

This prototype supports research and clinical decision-making on  
**post-caesarean pain at Korle Bu Teaching Hospital**.  

---
""")

menu = st.sidebar.radio("Navigation", ["Upload Data", "Prediction", "Analytics Dashboard", "About"])

# Load model
@st.cache_resource
def load_model():
    model_path = Path("models/pain_predictor.pkl")
    if not model_path.exists():
        return None
    try:
        with open(model_path, "rb") as f:
            data = pickle.load(f)
            return data
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model_data = load_model()

# Upload Data
if menu == "Upload Data":
    st.title("📂 Upload Patient Data")
    uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                data = pd.read_excel(uploaded_file)
            st.success("✅ Data uploaded successfully!")
            st.dataframe(data.head())
        except Exception as e:
            st.error(f"⚠️ Could not read file: {e}")

    st.markdown("---")
    st.markdown("### 🔗 Load Data from Google Forms (Google Sheets link)")
    sheet_url = st.text_input("Paste Google Sheet CSV link (must end with export?format=csv)")
    if sheet_url:
        try:
            if "export?format=csv" not in sheet_url:
                st.warning("Make sure the link ends with `export?format=csv`")
            else:
                data = pd.read_csv(sheet_url)
                st.success("✅ Google Form data loaded successfully!")
                st.dataframe(data.head())
        except Exception as e:
            st.error(f"⚠️ Failed to load Google Form data: {e}")

# Prediction
elif menu == "Prediction":
    st.title("🤖 Pain Risk Prediction")

    surgery_duration = st.selectbox("Duration of Surgery", ["<30min", "30-60min", ">60min"])
    anaesthesia = st.selectbox("Type of Anaesthesia", ["Spinal", "General"])
    pain_score = st.number_input("Pain Score", 0, 10, 5)

    if st.button("Predict Risk"):
        if model_data is None:
            st.error("⚠️ No trained model found. Please add 'models/pain_predictor.pkl'")
        else:
            try:
                model = model_data["model"]
                encoders = model_data["encoders"]

                # Encode input
                surgery_encoded = encoders["Surgery_Duration"].transform([surgery_duration])[0]
                anaesthesia_encoded = encoders["Anaesthesia"].transform([anaesthesia])[0]

                input_data = [[surgery_encoded, anaesthesia_encoded, pain_score]]
                prediction = model.predict(input_data)[0]
                predicted_label = encoders["Pain_Risk"].inverse_transform([prediction])[0]

                st.success(f"✅ **Predicted Pain Risk:** {predicted_label}")
                st.metric("Pain Score Entered", pain_score)
            except Exception as e:
                st.error(f"Prediction failed: {e}")

# Analytics
elif menu == "Analytics Dashboard":
    st.title("📈 Pain Analytics Dashboard")
    demo_file = Path("demo_pain_data.csv")
    if demo_file.exists():
        df = pd.read_csv(demo_file)
        if not df.empty:
            col1, col2 = st.columns(2)
            with col1:
                fig1 = px.histogram(df, x="Pain_Score", nbins=10, title="Distribution of Pain Scores")
                st.plotly_chart(fig1, use_container_width=True)
            with col2:
                fig2 = px.box(df, x="Surgery_Duration", y="Pain_Score", color="Anaesthesia",
                              title="Pain Score by Surgery Duration & Anaesthesia")
                st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("⚠️ No data available. Upload or link a dataset.")

# About
elif menu == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
This dashboard was developed to support **research and clinical decision-making** 
on post-caesarean pain at Korle Bu Teaching Hospital.

**Features:**
- Upload patient data (CSV, Excel, or Google Forms)
- Predict risk of low, medium, or high post-caesarean pain
- Explore analytics with interactive visualizations
- Future integration with DHIS2/EMR APIs

Built with ❤️ by **Ebenezer Kwaw**
""")
