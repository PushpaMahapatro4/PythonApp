import streamlit as st

# Set the title of the web app
st.title("Simple Streamlit App")

# Create a text input widget
user_input = st.text_input("Enter your name:")

# Create a button
if st.button("Submit"):
    # Display the input text
    st.write(f"Hello, {user_input}!")

# Create a slider
age = st.slider("Select your age:", 0, 100, 25)

# Display the slider value
st.write(f"Your age is: {age}")

# Create a selectbox
option = st.selectbox(
    'Select your favorite color:',
    ('Red', 'Green', 'Blue')
)

# Display the selected option
st.write(f'Your favorite color is: {option}')
