import streamlit as st
import pickle

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Customer Sentiment Analyzer",
    page_icon="😄",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
with open("sentiment_analysis.pkl", "rb") as f:
    model = pickle.load(f)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Main Card */
.main-box {
    background: #155DFC;
    padding: 20px;
    border-radius: 22px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.10);
    border: 1px solid;
    margin-top: 40px;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: #E0E0E0;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #E0E0E0;
    font-size: 20px;
    margin-bottom: 25px;
}

/* Text Area */
textarea {
    border-radius: 10px !important;
    border: 1.3px solid  !important;
    font-size: 18px !important;
    max-width: 620px;
}

textarea:focus {
    border: 0.5px solid #C6D2FF !important;
    box-shadow: 0 12px 28px rgba(95, 158, 160,0.90);
}

/* Button */
.stButton > button {
    width: 463%;
    background: linear-gradient(110deg,#A6ACAF,#262626);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
    transition: 0.3s ease;
    margin-top: 10px;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(226, 232, 240,0.50);
    color: white;
}

.result-box {
    margin-top: 3px;
    border-radius: 35px;
    text-align: center;
    border: 2px solid #F5F5F4;
    animation: fadeIn 0.10s ease;
    max-width: 320px;
    margin-left: auto;
    margin-right: auto;
    height: 240px
}

.positive {
    background: #178236;
    color: #ECFCCA;
}

.neutral {
    background: #D4AC0D;
    color: #FEF9C2;
}

.negative {
    background: #C11007;
    color: #FFE2E2;
}

/* Emoji */
.emoji {
    font-size: 50px;
    margin-bottom: 1px;
}

/* Floating emojis */
.float {
    position: fixed;
    font-size: 65px;
    opacity: 0.75;
    animation: floatUp 10s linear infinite;
    z-index: 0;
}

.e1 { left: 4%; animation-delay: 3s; }
.e2 { left: 12%; animation-delay: 5s; }
.e3 { left: 21%; animation-delay: 7s; }
.e4 { left: 73%; animation-delay: 4s; }
.e5 { left: 81%; animation-delay: 6s; }
.e6 { left: 89%; animation-delay: 9s; }

/* Animations */
@keyframes floatUp {
    0% { transform: translateY(100vh) scale(0.7); opacity:0; }
    20% { opacity:.35; }
    50% { opacity:.4; }
    100% { transform: translateY(-10vh) scale(1.1); opacity:0; }
}

@keyframes fadeIn {
    from {opacity:0; transform:translateY(15px);}
    to {opacity:1; transform:translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# Floating Emojis Background
st.markdown("""
<div class="float e1">😊</div>
<div class="float e2">😎</div>
<div class="float e3">😉</div>
<div class="float e4">😐</div>
<div class="float e5">😞</div>
<div class="float e6">😂</div>
""", unsafe_allow_html=True)

# -------------------------------
# Main UI
# -------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">CUSTOMER SENTIMENT ANALYZER</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">NLP-based sentiment analysis system</div>', unsafe_allow_html=True)

user_text = st.text_area(
    "Enter customer support message...",
    height=135,
    label_visibility="collapsed",
    placeholder="Enter customer support message..."
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Analyze Sentiment"):

    if user_text.strip():

        prediction = model.predict([user_text])[0].capitalize()

        if prediction == "Positive":
            st.markdown(f"""
            <div class="result-box positive">
                <div class="emoji">😊</div>
                <h3>Predicted Sentiment</h3>
                <h2>{prediction}</h2>
            </div>
            """, unsafe_allow_html=True)

        elif prediction == "Negative":
            st.markdown(f"""
            <div class="result-box negative">
                <div class="emoji">😞</div>
                <h3>Predicted Sentiment</h3>
                <h2>{prediction}</h2>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="result-box neutral">
                <div class="emoji">😐</div>
                <h3>Predicted Sentiment</h3>
                <h2>{prediction}</h2>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("Please enter feedback first.")

st.markdown('</div>', unsafe_allow_html=True)
