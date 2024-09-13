import streamlit as st


# --- PAGE SETUP ---
pages={
    
    " ":[st.Page(
    "home_page.py",
    title="HOME",
    icon=":material/home:",
    default=True
    
)],

    "Tools":[

 st.Page(
    "Chatbot.py",
    title="Conversation_chat",
    icon=":material/forum:",
    
),
st.Page(
    "RAG_CODE.py",
    title="RAG MODEL",
    icon=":material/picture_as_pdf:",
),
st.Page(
    "WEB_BASED.py",
    title="WEB-RAG MODEL",
    icon=":material/public:",
)]
}



# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(pages)


# --- SHARED ON ALL PAGES ---



# --- RUN NAVIGATION ---
pg.run()