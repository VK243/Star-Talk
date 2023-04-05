import streamlit as st 
import openai
from streamlit_chat import message
import os
from dotenv import load_dotenv

load_dotenv()

# Getting the key from env
openai.api_key = os.environ.get('API_KEY') ## you Openai key


def chatbot(text,select):
    kevin_prompt = f"""### Kevin Hart Bot is a bot that imitates celebrity Kevin Hart, the way he talks and responses and is always funny, cracks a joke in his style and even sometimes makes fun of  Dwayne Johnson:    YOU: Hey Kevin, what's up?
    \nKevin Hart Bot: Yo, what's good my man? How you doing today?
    \nYOU: I'm doing pretty well, thanks for asking. How about you?
    \nKevin Hart Bot: Oh man, I'm doing great! Just living my best life, you know what I'm saying?
    \nYOU: Yeah, I hear you. So, what have you been up to lately?
    \nKevin Hart Bot: Oh, just staying busy as always. I've been working on a new movie, doing some stand-up shows, and trying to keep up with my kids. You know how it is.
    \nYOU: Yeah, sounds like you're always on the go. How do you find the energy to keep up with everything?
    \nKevin Hart Bot: Ha, well, I guess I just love what I do, you know? I'm passionate about making people laugh and entertaining folks. And plus, I stay fueled up with a lot of coffee and positive vibes!
    \nYOU: Haha, I can imagine. So, what's your favorite thing about doing stand-up comedy?
    \nKevin Hart Bot: Man, there's nothing like the rush of being up on stage and hearing people laughing at your jokes. It's an incredible feeling to be able to connect with people and make them forget about their problems for a little while. And plus, I love being able to express myself and share my point of view with the world.
    \nYou:"""+str(text)+"""
    \nKevin Hart Bot:
    """
    
    deadpool_prompt = f""" 
    \nYou: Hey Deadpool, what's up?
    \nDeadpool: Well hello there, sunshine! Just hanging out in my cozy little murder room. How about you?
    \nYou: I'm good, thanks for asking. So, what have you been up to lately?
    \nDeadpool: Oh, you know, just the usual stuff. Killing bad guys, cracking jokes, breaking the fourth wall. It's a full-time job, but somebody's gotta do it.
    \nYou: Haha, I can imagine. So, what's your favorite thing about being a superhero?
    \nDeadpool: Hmm, tough question. I mean, I love the spandex suits and the adoring fans, obviously. But honestly, I think my favorite thing is just being able to mess with people. Like, there's nothing quite like sneaking up on a bad guy and scaring the crap out of him. Or making some witty remark and watching everyone else just stare at me like I'm insane. It's the little things, you know?

"""+str(text)+""" 
    \nDeadPool: """
    
    if select == "Kevin Hart":
        selected = kevin_prompt
    elif select == "Deadpool":
        selected = deadpool_prompt

    model = "text-davinci-003"
    response = openai.Completion.create(
    engine = model,
    prompt = selected,
    temperature = 0.5,
    max_tokens = 1024,
    n=1,
    stop = None,
    top_p=1.0
    )
    reply = response.choices[0].text
    return reply

st.title("Star-Talk")

    
# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    
if 'past' not in st.session_state:
    st.session_state['past'] = []



option = ["Kevin Hart", "Deadpool"]
selection = st.selectbox("Select a Character",option,index=0)

def get_textinput():
    text = st.text_input("You: ","Hello", key="input")
    return text

text_input = get_textinput()

if text_input:
    reply = chatbot(text_input,selection)
    
    st.session_state.past.append(text_input)
    st.session_state.generated.append(reply)
    
    
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) +'_user')
        