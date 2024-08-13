import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])

def ai(txt):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now you are a chatbot that can provide reliable and relevant information about various things asked by user and your name is chatbot and you are created by Naveen"+txt)
    return response.text


st.title("Naveen's Chat Bot")

command = st.chat_input("How Can I Help You..")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])


if command:
    with st.chat_message("USER"):
        st.write(command)
        st.session_state.message.append({"role":"USER","message":command})
    if "Hello" in command:
        with st.chat_message("BOT"):
            st.write("Hello..Give me your informations to know your eligible government schemes")
            st.session_state.message.append({"role":"BOT","message":"Hello..Give me your informations to know your eligible government schemes"})
    elif "Hi" in command:
        with st.chat_message("BOT"):
            st.write("Hello..Give me your informations to know your eligible government schemes")
            st.session_state.message.append({"role":"BOT","message":"Hello..Give me your informations to know your eligible government schemes"}) 
    elif "Who" in command:
        with st.chat_message("BOT"):
            st.write("Im an AI Assistant and my job is to guide you towards government schemes which are eligible for you")
            st.session_state.message.append({"role":"BOT","message":"Im an AI Assistant and my job is to guide you towards government schemes which are eligible for you"})
    elif "who" in command:
        with st.chat_message("BOT"):
            st.write("Im an AI Assistant and my job is to guide you towards government schemes which are eligible for you")
            st.session_state.message.append({"role":"BOT","message":"Im an AI Assistant and my job is to guide you towards government schemes which are eligible for you"})
   
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})


print(st.session_state.message)
