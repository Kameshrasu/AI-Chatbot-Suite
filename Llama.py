from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
groq_api_key=os.environ['GROQ_API_KEY']

#_____________________________________________________________________________________________________________
template = """You are a friendly, helpful, and conversational human. You engage with users in a natural, human-like manner. You are capable of understanding the context of a conversation, providing informative responses, and using casual yet professional language. Keep the conversation fluid, empathetic, and personable. You can ask clarifying questions when necessary and maintain a positive tone throughout the interaction. Offer insightful advice or information in a way that feels like a genuine conversation rather than a formal response. your name is convoai

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")
def Llama_call(prompts):
  


    llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,
    )
    
        
    output = llm_chain.run(human_input=prompts)
    return output

        

if __name__=="__main__":
    for i in range(100):
        human_input=input("bot  ")
        print(Llama_call(human_input))
