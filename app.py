import streamlit as st

st.set_page_config( 
  page_title="kuliah praktisi 2026",
  page_icon="🧊",
  layout="centered",
  initial_sidebar_state="expended"
)

st.title (" Dashboard ")
st.hearder("laporan bulanan")
st.subharder(" monthly expenses"
st. caption("made with using streamlit")
st.write("Hello, *World!* :sunglasses:")  
             
title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
