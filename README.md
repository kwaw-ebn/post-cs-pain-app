<<<<<<< HEAD
# Post-Caesarean Pain Streamlit Project

Created by **Ebenezer Kwaw** 

🩺 Post-Caesarean Pain Prediction & Analytics Dashboard

Overview
This Streamlit app supports research and clinical decision-making on post-caesarean pain at Korle Bu Teaching Hospital and beyond.
It allows healthcare professionals to predict pain risk, analyze patient data, and visualize patterns interactively.

🚀 Features

✅ Pain Risk Prediction

Predicts Low, Medium, or High risk based on surgery duration, anaesthesia type, and pain score.

Uses a trained ML model stored as models/pain_predictor.pkl.

✅ Data Uploads

Supports CSV and Excel uploads.

Option to load Google Form data directly via Google Sheets CSV link.

✅ Analytics Dashboard

Interactive visualizations (Plotly):

Pain Score Distribution

Pain Score by Surgery Duration & Anaesthesia

✅ Simple UI

Fully responsive and lightweight Streamlit interface.

🧠 Model Details

The trained model (models/pain_predictor.pkl) is a Random Forest Classifier trained using demo data.

Feature	Description
Surgery_Duration	<30min, 30-60min, or >60min
Anaesthesia	Spinal or General
Pain_Score	Numeric (0–10)

Pain Risk Labels:

Low = Pain_Score ≤ 3

Medium = 4 ≤ Pain_Score ≤ 6

High = Pain_Score > 6

🛠️ Setup on Linux / Ubuntu
1️⃣ Clone the repository
# Navigate to your working directory
cd ~/Documents

2️⃣ Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🧩 Project Structure
post-caesarean-pain-dashboard/
│
├── app.py                    # Main Streamlit application
├── demo_pain_data.csv         # Sample dataset
├── models/
│   └── pain_predictor.pkl     # Trained ML model
├── requirements.txt           # Python dependencies
├── logo.jpg                   # Optional logo (Korle Bu / RootsLink / WHO)
└── README.md                  # Documentation

💾 GitHub Version Control Commands (Ubuntu)


# Check your current status
git status

# Stage all changes
git add .

# Commit with a message
git commit -m "Updated Streamlit pain prediction app"

# Push changes to GitHub
git push origin main


☁️ Streamlit Cloud Deployment Guide
1️⃣ Prepare your repository

Ensure your repo contains:

app.py
requirements.txt
models/pain_predictor.pkl
demo_pain_data.csv
README.md

2️⃣ Push everything to GitHub

From your Ubuntu terminal:

git add .
git commit -m "Final version for Streamlit Cloud"
git push origin main

3️⃣ Deploy on Streamlit Cloud

Go to https://share.streamlit.io

Sign in with your GitHub account.

Click “New app” → Select your repo and branch.

Enter the path to your main app file (e.g. app.py).

Click Deploy 🚀

Streamlit Cloud will automatically install your dependencies and start the app.

📊 Example (Prediction Tab)
Field	Example
Surgery Duration	30–60min
Type of Anaesthesia	Spinal
Pain Score	5

Predicted Output:
✅ Predicted Pain Risk: Medium

🧑‍💻 Tech Stack

Python 3.9+

Streamlit for web interface

Plotly for analytics visualization

Scikit-learn for machine learning

Pandas for data manipulation

❤️ Author

Developed by Ebenezer Kwaw
Public Health | Data Science | Machine Learning | AI for Health

📧 Email: [ekwaw4545@gmail.com]
]
🌐 GitHub: [github.com/kwaw-ebn]


