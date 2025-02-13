import subprocess
import json

# Example input for the model
input_text = "President of India"



# The command to run the Ollama model (adjust according to your system and model name)
command = [
    "ollama",  # Assuming "ollama" is the command-line tool means it is downloaded
    "run",     # Command to run the model
    "deepseek-r1:7b",  
    input_text  # Input text for the model
]

# Run the command and capture the output
try:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    # Process the output
    output = result.stdout.strip()
    print("Model Output:", output)
except subprocess.CalledProcessError as e:
    print(f"Error running Ollama model: {e}")
    print("Error Output:", e.stderr)

