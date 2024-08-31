import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input text box
user_input = st.text_input("Enter some text:")

# Button to display the entered text
if st.button("Show text"):
    st.write("You entered:", user_input)
