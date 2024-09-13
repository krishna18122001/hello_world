import streamlit as st

# Create a text input widget for the user to enter their name
name = st.text_input("What's your name?")

# Check if the name field is not empty
if name:
    # Display a personalized greeting message
    st.write(f"Hi, {name}!")
else:
    # Prompt the user to enter their name
    st.write("Please enter your name above.")
