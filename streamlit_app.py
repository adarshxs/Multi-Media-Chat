import streamlit as st
from streamlit_chat import message


st.set_page_config(page_title="Murph", page_icon="📖")
st.title("Bhagwaan Bharose :sunglasses:")
st.image("logo.png", use_column_width=True)
st.write("Welcome to my multi-page app! Use the sidebar to navigate between pages.")
st.write("![Your Awsome GIF](https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif)")
def PDF():
    st.write("PDF SHIT")

def VIDEO():
    st.write("VIDEO SHIT")

def LINKS():
    st.write("LINKS SHIT")