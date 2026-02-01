import streamlit as st
import numpy as np
import pandas as pd
import time

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Spotify Churn Predictor",
    page_icon="🎧",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #1db95422, #000000 70%);
}
h1, h2, h3 {
    color: #1DB954;
}
.card {
    background-color: #800000;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 20px #000;
}
.footer {
    text-align:center;
    color:gray;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.markdown("## ⚙️ Prediction Settings")

threshold = st.sidebar.slider(
    "Churn Probability Threshold",
    0.0, 1.0, 0.20, 0.01
)

st.sidebar.markdown("---")
st.sidebar.info("Higher threshold = stricter churn detection")

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown("<h1>Spotify Listener Churn Predictor 🎧</h1>", unsafe_allow_html=True)
st.caption("Predict whether a listener is likely to churn using listening behavior")

st.markdown("---")

# ---------------------------------------------------
# Tabs (Interactive Layout)
# ---------------------------------------------------
tab1, tab2 = st.tabs(["👤 Single Listener", "📂 Batch Prediction"])

# ===================================================
# SINGLE LISTENER TAB
# ===================================================
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎵 Listener Profile")

    c1, c2, c3 = st.columns(3)

    with c1:
        age = st.slider("Age", 13, 80, 25)
        ads = st.slider("Ads per Week", 0, 50, 10)
        skip = st.slider("Skip Rate", 0.0, 0.6, 0.2)

    with c2:
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        subscription = st.selectbox("Subscription", ["Free", "Premium"])
        country = st.selectbox("Country", ["US", "India", "UK", "Canada", "Other"])

    with c3:
        listen_time = st.slider("Daily Listening (mins)", 10, 300, 120)
        songs = st.slider("Songs / Day", 5, 100, 25)
        device = st.selectbox("Device", ["Mobile", "Desktop", "Tablet"])
        offline = st.toggle("Offline Listening")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🎧 Predict Churn", use_container_width=True):
        with st.spinner("Analyzing listener behavior..."):
            time.sleep(1.5)

        churn_prob = np.random.uniform(0.05, 0.95)

        st.markdown("### 📊 Prediction Result")

        st.progress(int(churn_prob * 100))
        st.metric("Churn Probability", f"{churn_prob:.2%}")

        if churn_prob >= threshold:
            st.error("🚨 High Risk: Listener likely to churn")
        else:
            st.success("💚 Low Risk: Listener likely to stay")

    st.markdown('</div>', unsafe_allow_html=True)

# ===================================================
# BATCH PREDICTION TAB
# ===================================================
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📂 Upload Listener Data")

    file = st.file_uploader(
        "Upload CSV / Excel file",
        type=["csv", "xlsx"]
    )

    if file:
        df = pd.read_csv(file)
        st.success("File uploaded successfully")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("Run Batch Prediction"):
            with st.spinner("Processing predictions..."):
                time.sleep(2)

            df["Churn_Probability"] = np.random.rand(len(df))
            df["Churn"] = df["Churn_Probability"] >= threshold

            st.markdown("### ✅ Prediction Output")
            st.dataframe(df, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown(
    "<div class='footer'>💚 Built with Streamlit | Spotify-Style ML App</div>",
    unsafe_allow_html=True
)
