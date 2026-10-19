# ☕ 365 Coffee Café - Customer Retention Intelligence

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-success.svg)

## 📌 Project Overview
The **Customer Retention Intelligence** dashboard is an end-to-end Machine Learning decision-support system built for 365 Coffee Café. It leverages a trained predictive model to analyze customer visit data and predict the likelihood of a customer returning within 14 days. 

Designed with a cutting-edge **3D Neumorphism UI**, the application provides cafe managers with actionable insights, automated batch processing, and data-driven customer retention strategies.

## 🚀 Key Features
* **🎯 Single Visit Predictor:** Real-time probability scoring based on 21 distinct customer and operational features.
* **⚡ Quick Presets:** One-click simulation testing (e.g., "Platinum VIP", "At-Risk Basic") for rapid scenario analysis.
* **📁 Batch Processing Pipeline:** Upload a CSV of historical customer data to generate bulk predictions and download the scored dataset.
* **📊 Model Insights:** Interactive visualizations showcasing key predictive drivers (e.g., Loyalty Tier, Visit History).
* **🎨 3D Neumorphic UI:** A custom-built, premium, and highly responsive glass/neumorphic design architecture.

## 🧠 Machine Learning Architecture
* **Algorithm:** Random Forest Classifier (`coffee_model.pkl`)
* **Target Variable:** 14-Day Return Probability (Binary: Likely to Return / Unlikely to Return)
* **Top Predictive Features:** Loyalty Tier, Visit Number, First Visit Flag, Days Since Previous Visit, Service Rating.
* **Model Performance:** 69.81% Accuracy | 92.46% Recall

## 🛠️ Technology Stack
* **Language:** Python
* **Frontend/UI:** Streamlit (Custom CSS)
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Visualization:** Matplotlib
* **Deployment/Serialization:** Joblib

## ⚙️ Installation & Usage

**1. Clone the repository:**
```bash
git clone [https://github.com/khan__zaibi/Coffee-Retention-Intelligence.git](https://github.com/khan__zaibi/Coffee-Retention-Intelligence.git)
cd Coffee-Retention-Intelligence

```

**2. Install dependencies:**

```bash
pip install -r requirements.txt

```

**3. Run the application:**

```bash
streamlit run app.py

```

## 📁 Repository Structure

* `app.py`: Main Streamlit application file containing UI logic and prediction pipeline.
* `coffee_model.pkl`: Serialized Random Forest machine learning model.
* `Coffee shop logo.png`: Application branding asset.
* `requirements.txt`: Python package dependencies.
* `model_training.ipynb`: Jupyter Notebook detailing EDA, feature engineering, and model training.

---

**Developed by:** Zohaib Ahmed Khan (Aspiring Data Scientist)

```

```
