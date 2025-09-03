# Post-Caesarean Pain Streamlit Project

Created by **Ebenezer Kwaw** & **Abena Onomah**

This is a ready-to-run Streamlit app for predicting and analyzing post-caesarean pain.

## 1) Setup on Ubuntu/Linux

```bash
cd ~/Downloads
unzip post_cs_pain_streamlit_project.zip -d post_cs_pain_streamlit_project
cd post_cs_pain_streamlit_project
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## 2) Uploading Data

The app supports three ways to load data:

### a) Upload CSV
- Export your dataset as `.csv`
- Go to **Upload Data** in the sidebar
- Select your file → preview appears

### b) Upload Excel
- Supported format: `.xlsx`
- Select your file under **Upload Data**

### c) Google Forms / Google Sheets
- In Forms: **Responses → Open in Google Sheets**
- In Sheets: **File → Share → Publish to Web → CSV format**
- Copy the link (must end with `export?format=csv`)
- Paste it in the app to fetch live responses

## 3) Adding Your Logo

- Place `logo.jpg` in the project root (same folder as `app.py`).
- It will automatically appear in the sidebar.

## 4) Features

- **Upload Data**: CSV, Excel, or Google Forms
- **Prediction**: Uses ML model (`models/pain_predictor.pkl` if available)
- **Analytics Dashboard**: Visualize pain score distribution and factors
- **About**: App info and future plans

