import streamlit as st
import sys
import os
import time



from Llama import Llama_call

# Streamlit app setup
st.title("💬🤖 ConvoAI")
st.caption("🚀 A ConvoAI powered by llama")
st.logo("Chatbots-removebg-preview.png")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello buddy!"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt_text := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    st.chat_message("user").write(prompt_text)
    
    # Placeholder for assistant's response
    assistant_placeholder = st.chat_message("assistant")
    typing_effect_placeholder = assistant_placeholder.empty()

    # Get response from Llama model
    response = Llama_call(prompt_text)
    
    # Typewriter effect: reveal text one letter at a time
    typed_text = ""
    for char in response:
        typed_text += char
        typing_effect_placeholder.write(typed_text)
        time.sleep(0.01)  # Adjust typing speed here
    
    st.session_state.messages.append({"role": "assistant", "content": response})

