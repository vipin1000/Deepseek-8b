import subprocess
import streamlit as st

# Function to run the Ollama model
def run_ollama_model(input_text):
    # Command to run the Ollama model
    command = [
        "ollama",  # Assuming "ollama" is the command-line tool
        "run",     # Command to run the model
        "deepseek-r1:7b",  # Replace with your specific model's name
        input_text  # Input text for the model
    ]
    
    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running Ollama model: {e}\nError Output: {e.stderr}"

# Streamlit app layout
st.title("Ollama Chatbot")

# Input text area for the chatbot
user_input = st.text_input("You: ", "")

if user_input:
    # Display the user's input
    st.write(f"You: {user_input}")

    # Run the Ollama model with the user input
    response = run_ollama_model(user_input)
    if '</think>' in response:
        result = response.split('</think>')[1].strip()  # Return the part after '--'
    else:
        result = response.strip()  # If no '--', just return the full response

    # Display the response from the model
    st.write(f"Bot: {result}")

