import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Chatbot Suite",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for premium design
st.markdown(
    """
    <style>
    body {
        background-color: black;  /* Dark background for a premium look */
        color: black;
    }
    .premium-header {
        color: #c45b10;
        font-size: 36px;
        font-weight: bold;
        border: 4px solid #c45b10;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #e30780;
        font-size: 28px;
        text-align: center;
        margin-top: 28px;
        font-family: cursive;
    }
    .description {
        color: #eb7907;
        font-size: 22px;
        text-align: justify;
        margin: 20px auto;
        
        font-family: cursive;
        line-height: 2.0;
    }
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .social-links {
        margin-top: 30px;
        text-align: center;
    }
    .social-links a {
        color: royal blue;
        text-decoration: none;
        font-size: 24px;
        margin: 0 15px;
    }
    .social-links a:hover {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.logo("Chatbots-removebg-preview.png")
# Premium header title
st.markdown('<div class="premium-header">AI Chatbot Suite</div>', unsafe_allow_html=True)

# Subtitle with custom color
st.markdown('<div class="subtitle">Conversational and RAG-based AI Solutions</div>', unsafe_allow_html=True)

# Brief description of the page with better alignment
st.markdown('<div class="description">Welcome to the AI Chatbot Suite, an elite platform at the forefront of conversational AI innovation. Whether you desire effortless, human-like interactions through our cutting-edge Conversational Chatbot , data-enriched responses driven by our advanced Retrieval-Augmented Generation (RAG)-based Chatbot, we are here to redefine your digital experience and elevate engagement to new heights.</div>', unsafe_allow_html=True)


st.markdown('<div  class= "description"></div>', unsafe_allow_html=True)


st.markdown(
    """
    <div class="social-links">
        <a href="https://www.linkedin.com/in/kamesh-rasu-01641a280/" target="_blank">LinkedIn</a>
        <a href="https://github.com/Kameshrasu" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)



