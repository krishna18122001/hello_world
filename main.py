import streamlit as st
import socket

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 1))
        ip_address = s.getsockname()[0]
    except Exception as e:
        ip_address = "Unable to get IP address"
    finally:
        s.close()
    return ip_address

# Create a text input widget for the user to enter their name
name = st.text_input("What's your name?")

# Display the IP address of the server
st.write(f"Server IP Address: {get_ip_address()}")

# Check if the name field is not empty
if name:
    # Display a personalized greeting message
    st.write(f"Hi, {name}!")
else:
    # Prompt the user to enter their name
    st.write("Please enter your name above.")
