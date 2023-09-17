import streamlit as st
import clarifai

# Create a Clarifai client
client = clarifai.Client('a7cf76e4c31146d19e5e406343d696bd')

# Set the LLAMA2 model
model = client.text().predict(model_id="llama2-13b")

# Define a function to generate predictions
def generate_predictions(text):
    predictions = model.predict(text)
    return predictions

# Create a text input field
text_input = st.text_input("Enter some text:")

# Generate predictions
predictions = generate_predictions(text_input)

# Display the predictions
st.write("Predictions:")
for prediction in predictions:
    st.write(prediction['text'])
