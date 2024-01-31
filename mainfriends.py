import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])

def ai(txt):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("from now your name is Naveen and you are a developer"+txt)
    return response.text


st.title("Ai Assistant")

command = st.chat_input("how can I help you?")

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
            st.write("Hi Dude")
            st.session_state.message.append({"role":"BOT","message":"Hi Dude"})
    elif "Who" in command:
        with st.chat_message("BOT"):
            st.write("Im Naveen's AI Assistant")
            st.session_state.message.append({"role":"BOT","message":"Im Naveen's AI Assistant"})
    elif "Aswin" in command:
        with st.chat_message("BOT"):
            st.write("vanakam")
            st.session_state.message.append({"role":"BOT","message":"vanakam"}) 
    elif "Akash" in command:
        with st.chat_message("BOT"):
            st.write("ombaaa...vandu ombu")
            st.session_state.message.append({"role":"BOT","message":"ombaaa...vandu ombu"})  
    elif "Ragesh" in command:
        with st.chat_message("BOT"):
            st.write("kavya purusan....welcome")
            st.session_state.message.append({"role":"BOT","message":"kavya purusan....welcome"}) 
    elif "Gopinath" in command:
        with st.chat_message("BOT"):
            st.write("dei pp...poda bumda")
            st.session_state.message.append({"role":"BOT","message":"dei pp...poda bumda"}) 
    elif "Jothilakshmi" in command:
        with st.chat_message("BOT"):
            st.write("hi mam...nalla irukingala?...")
            st.session_state.message.append({"role":"BOT","message":"hi mam...nalla irukingala?..."})     
    elif "Vaishnavi" in command:
        with st.chat_message("BOT"):
            st.write("i said you to type your name da")
            st.session_state.message.append({"role":"BOT","message":"i said you to type your name da"})
    elif "Saron" in command:
        with st.chat_message("BOT"):
            st.write("celebrity bro...ninga la")
            st.session_state.message.append({"role":"BOT","message":"celebrity bro...ninga la"})  
    elif "Shalu" in command:
        with st.chat_message("BOT"):
            st.write("po t nayae")
            st.session_state.message.append({"role":"BOT","message":"po t nayae"})      
    elif "Monik" in command:
        with st.chat_message("BOT"):
            st.write("grow up soon..lets have fun")
            st.session_state.message.append({"role":"BOT","message":"grow up soon..lets have fun"})                                                 
    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role":"BOT","message":data})




print(st.session_state.message)
