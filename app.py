import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import matplotlib.pyplot as plt

# 1. Page Configuration (Wide Layout)
st.set_page_config(page_title="365 Coffee Café Intelligence", page_icon="☕", layout="wide")

# 2. Clean Modern Styling (No ugly boxed containers)
st.markdown("""
    <style>
    /* 1. Global Background (Premium Soft Cafe Cream) */
    .stApp {
        background-color: #EBE6E0;
        color: #3E2723;
    }

    /* 2. Remove Unwanted Column Boxes & Borders */
    div[data-testid="stVerticalBlock"] > div, 
    div.stMarkdown, div.stForm {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        backdrop-filter: none !important;
    }

    /* 3. 3D Centered Main Title */
    h1 {
        color: #4A3324 !important;
        text-align: center !important;
        font-weight: 900 !important;
        font-size: 42px !important;
        /* 3D Embossed Text Effect */
        text-shadow: 1px 1px 0px #FFFFFF, 
                     2px 2px 0px #C8C2BA, 
                     3px 3px 0px #A89F94, 
                     6px 6px 10px rgba(0,0,0,0.2) !important;
        margin-bottom: 25px !important;
    }
    h2, h3 {
        color: #4A3324 !important;
        font-weight: 800;
        text-shadow: 1px 1px 2px #FFFFFF, -1px -1px 2px rgba(0,0,0,0.05);
    }
    p, span, label {
        color: #5D4037 !important;
        font-weight: 600;
    }

    /* 4. Main App Container 3D Floating Effect */
    .block-container {
        background: #EBE6E0;
        border-radius: 30px;
        box-shadow: 20px 20px 60px #C8C2BA, -20px -20px 60px #FFFFFF;
        padding: 3rem !important;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* 5. 3D Input Fields (Pressed Inward / Debossed) */
    .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #EBE6E0 !important;
        border: none !important;
        border-radius: 12px;
        box-shadow: inset 5px 5px 10px #C8C2BA, inset -5px -5px 10px #FFFFFF !important;
        color: #3E2723 !important;
        padding: 12px !important;
        font-weight: 600 !important;
    }
    .stSelectbox div[data-baseweb="select"] * {
        color: #3E2723 !important;
    }

    /* 6. Professional 3D Buttons (Dark Coffee with Bright White Text) */
    div.stButton > button:first-child, div.stButton > button:first-child * {
        background: linear-gradient(145deg, #5D4037, #3E2723) !important;
        color: #FFFFFF !important; /* Pure White text for max visibility */
        border: none !important;
        border-radius: 12px;
        font-size: 17px !important;
        font-weight: 800 !important;
        padding: 12px;
        width: 100%;
        box-shadow: 7px 7px 14px #C8C2BA, -7px -7px 14px #FFFFFF !important;
        transition: all 0.2s ease-in-out;
    }
    
    /* Button Hover & Click Effect (Presses Down) */
    div.stButton > button:first-child:hover, div.stButton > button:first-child:active {
        background: linear-gradient(145deg, #3E2723, #261714) !important;
        box-shadow: inset 4px 4px 8px #1A100E, inset -4px -4px 8px #54352D !important;
        color: #FFD54F !important; /* Gold text touch on hover */
        transform: translateY(3px);
    }

    /* 7. Tabs Clean 3D Layout */
    .stTabs [data-baseweb="tab-list"] {
        background: transparent;
        gap: 15px;
    }
    .stTabs [data-baseweb="tab-list"] button {
        background: #EBE6E0;
        border-radius: 10px;
        box-shadow: 5px 5px 10px #C8C2BA, -5px -5px 10px #FFFFFF;
        color: #5D4037 !important;
        padding: 10px 20px;
        margin-bottom: 10px;
        border: none !important;
        font-weight: 600 !important;
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        box-shadow: inset 4px 4px 8px #C8C2BA, inset -4px -4px 8px #FFFFFF;
        color: #3E2723 !important;
        font-weight: 900 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Perfectly Centered Logo (Clean & Normal Size)
col_logo1, col_logo2, col_logo3 = st.columns([2, 1, 2]) 
with col_logo2:
    try:
        logo = Image.open("Coffee shop logo.png")
        st.image(logo, use_container_width=True)
    except FileNotFoundError:
        st.warning("Logo image 'Coffee shop logo.png' not found.")

# 4. Dashboard Header
st.markdown("<h1>Customer Retention Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #d4a373;'>Advanced Machine Learning system for 365 Coffee Café</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. Load the Model
@st.cache_resource
def load_model():
    return joblib.load("coffee_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("Error loading model. Please ensure 'coffee_model.pkl' exists in this folder.")
    st.stop()

# 6. Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🎯 Single Visit Predictor", "📁 Batch CSV Prediction", "📊 Key Model Insights"])

with tab1:
    st.markdown("### ⚡ Quick Preset Scenarios")
    preset_col1, preset_col2, preset_col3 = st.columns(3)
    
    if 'preset' not in st.session_state:
        st.session_state.preset = None

    if preset_col1.button("👑 Load Platinum Loyal VIP"):
        st.session_state.preset = "Platinum"
    if preset_col2.button("⚠️ Load At-Risk Basic Customer"):
        st.session_state.preset = "Basic"
    if preset_col3.button("🔄 Reset Form"):
        st.session_state.preset = "Reset"

    p_store = "Khayaban e Seher"
    p_tier = "Platinum" if st.session_state.preset == "Platinum" else ("Basic" if st.session_state.preset == "Basic" else "Gold")
    p_gender = "Female"
    p_age = 28 if st.session_state.preset == "Platinum" else 35
    p_first = "No" if st.session_state.preset == "Platinum" else "Yes"
    p_visits = 12 if st.session_state.preset == "Platinum" else 1
    p_days = 3 if st.session_state.preset == "Platinum" else 20
    p_channel = "Cafe App" if st.session_state.preset == "Platinum" else "Walk-in"
    p_pay = "App" if st.session_state.preset == "Platinum" else "Cash"
    p_weekday = "Saturday"
    p_hour = 15
    p_wait = 3.0 if st.session_state.preset == "Platinum" else 8.5
    p_rating = 5.0 if st.session_state.preset == "Platinum" else 2.0
    p_lines = 3
    p_qty = 3
    p_prod = 2
    p_cat = 2
    p_rev = 22.50
    p_disc = 2.0 if st.session_state.preset == "Platinum" else 0.0
    p_disc_pct = 0.1 if st.session_state.preset == "Platinum" else 0.0
    p_promo = "Yes" if st.session_state.preset == "Platinum" else "No"

    st.markdown("### 📋 Enter Visit Details")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**👤 Customer Profile**")
        store_location = st.selectbox("Store Location", ["Khayaban e Seher", "Tipu Sultan", "P.E.C.H.S"], index=["Khayaban e Seher", "Tipu Sultan", "P.E.C.H.S"].index(p_store))
        loyalty_tier = st.selectbox("Loyalty Tier", ["Basic", "Silver", "Gold", "Platinum"], index=["Basic", "Silver", "Gold", "Platinum"].index(p_tier))
        customer_gender = st.selectbox("Customer Gender", ["Male", "Female", "Other", "Unknown"], index=["Male", "Female", "Other", "Unknown"].index(p_gender))
        customer_age = st.number_input("Customer Age", min_value=16, max_value=100, value=p_age)
        is_first_visit = st.selectbox("Is this their first visit?", ["Yes", "No"], index=["Yes", "No"].index(p_first))
        visit_number = st.number_input("Visit Number", min_value=1, value=p_visits)
        days_since_prev = st.number_input("Days Since Previous Visit", min_value=0, value=p_days)

    with col2:
        st.markdown("**⚙️ Operations & Service**")
        order_channel = st.selectbox("Order Channel", ["Walk-in", "Cafe App", "Foodpanda", "Careem Quik", "Takeaway"], index=["Walk-in", "Cafe App", "Foodpanda", "Careem Quik", "Takeaway"].index(p_channel))
        payment_method = st.selectbox("Payment Method", ["Card", "Cash", "Wallet", "App"], index=["Card", "Cash", "Wallet", "App"].index(p_pay))
        weekday = st.selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(p_weekday))
        transaction_hour = st.slider("Transaction Hour (24h)", 0, 23, p_hour)
        wait_time_min = st.number_input("Wait Time (Minutes)", min_value=0.0, value=p_wait)
        service_rating = st.slider("Service Rating (1 to 5)", 1.0, 5.0, p_rating, 0.5)

    with col3:
        st.markdown("**🛒 Basket Summary**")
        basket_line_count = st.number_input("Basket Line Count", min_value=1, value=p_lines)
        basket_total_items_qty = st.number_input("Total Items Quantity", min_value=1, value=p_qty)
        basket_unique_products_count = st.number_input("Unique Products", min_value=1, value=p_prod)
        basket_unique_categories_count = st.number_input("Unique Categories", min_value=1, value=p_cat)
        net_revenue = st.number_input("Basket Net Revenue ($)", min_value=0.0, value=p_rev)
        total_discount = st.number_input("Total Discount Amount ($)", min_value=0.0, value=p_disc)
        average_discount_pct = st.number_input("Average Discount %", min_value=0.0, max_value=1.0, value=p_disc_pct)
        promo_used = st.selectbox("Promotion Used", ["Yes", "No"], index=["Yes", "No"].index(p_promo))

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Analyze & Predict Retention"):
        is_first_visit_val = 1 if is_first_visit == "Yes" else 0
        promo_used_val = 1 if promo_used == "Yes" else 0
        
        input_df = pd.DataFrame({
            "store_location": [store_location],
            "customer_gender": [customer_gender],
            "loyalty_tier": [loyalty_tier],
            "order_channel": [order_channel],
            "is_first_visit_label": [is_first_visit_val],
            "weekday": [weekday],
            "payment_method": [payment_method],
            "promo_used": [promo_used_val],
            "customer_age": [customer_age],
            "visit_number": [visit_number],
            "days_since_previous_visit_clean": [days_since_prev],
            "wait_time_min": [wait_time_min],
            "service_rating": [service_rating],
            "basket_net_revenue": [net_revenue],
            "basket_total_discount": [total_discount],
            "transaction_hour": [transaction_hour],
            "basket_line_count": [basket_line_count],
            "basket_total_items_qty": [basket_total_items_qty],
            "basket_unique_products_count": [basket_unique_products_count],
            "basket_unique_categories_count": [basket_unique_categories_count],
            "average_discount_pct": [average_discount_pct]
        })
        
        with st.spinner("AI is analyzing customer patterns..."):
            try:
                probabilities = model.predict_proba(input_df)[0]
                prob_yes = probabilities[1] * 100 
                
                st.markdown("---")
                st.markdown("### 📊 AI Analysis Result")
                
                res_col1, res_col2 = st.columns([1, 2])
                
                with res_col1:
                    if prob_yes >= 50.0:
                        st.success("### ✅ Likely to Return")
                    else:
                        st.error("### ❌ Unlikely to Return")
                        
                    st.metric(label="Return Probability", value=f"{prob_yes:.2f}%")
                    
                with res_col2:
                    st.write("**Probability Gauge:**")
                    st.progress(int(prob_yes))
                        
                st.warning("⚠️ **Decision-Support Notice:** This score is an estimate based on historical machine learning data. It is not an absolute guarantee of future customer behavior.")
                
            except Exception as e:
                st.error(f"Prediction Error: {e}")

with tab2:
    st.markdown("### 📁 Batch Prediction via CSV Upload")
    st.markdown("""
    Upload a CSV file containing multiple customer visit rows to run predictions in bulk. 
    > ⚠️ **Important Note:** The uploaded CSV file **must contain the exact same column names** that the model was trained on (e.g., `store_location`, `loyalty_tier`, `customer_age`, `wait_time_min`, etc.), otherwise the prediction will throw an error.
    """)
    
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file is not None:
        batch_df = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Data:", batch_df.head(3))
        
        if st.button("Run Batch Predictions"):
            try:
                batch_probs = model.predict_proba(batch_df)[:, 1] * 100
                batch_preds = ["Likely to Return" if p >= 50 else "Unlikely to Return" for p in batch_probs]
                
                batch_df["Return_Probability_%"] = batch_probs.round(2)
                batch_df["Predicted_Class"] = batch_preds
                
                st.success("Batch prediction completed successfully!")
                st.dataframe(batch_df.head(10))
                
                csv_data = batch_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Predictions CSV",
                    data=csv_data,
                    file_name="365_Coffee_Batch_Predictions.csv",
                    mime="text/csv"
                )
            except Exception as e:
                st.error(f"Batch Error: Ensure all required columns match training features. Details: {e}")

with tab3:
    st.markdown("### 📊 Model Insights & Feature Importance")
    st.write("Overview of what drives the Random Forest model's predictions based on project analysis:")
    
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#1e1e1e')
    
    features = ['Loyalty Tier (Platinum)', 'Loyalty Tier (Basic)', 'Visit Number', 'First Visit Flag', 'Days Since Prev Visit']
    importance = [0.242, 0.174, 0.144, 0.095, 0.082]
    
    ax.barh(features, importance, color='#dda15e')
    ax.set_xlabel("Relative Importance Score", color='#f3ede2')
    ax.set_title("Top Model Features", color='#f3ede2')
    ax.tick_params(colors='#f3ede2')
    ax.spines['bottom'].set_color('#d4a373')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#d4a373')
    ax.invert_yaxis()
    st.pyplot(fig)
    
    st.info("💡 **Key Takeaway:** The model heavily relies on loyalty status and visit history. Operational metrics like wait times have lower direct importance compared to customer loyalty tiers.")

with st.expander("ℹ️ About the Machine Learning Project"):
    st.write("""
        - **Business Case:** 365 Coffee Café Customer Retention Prediction.
        - **Algorithm:** Random Forest Classifier (Trained on executed workbook outputs).
        - **Performance:** 69.81% Accuracy, 92.46% Recall.
    """)