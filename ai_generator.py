from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini client
client = genai.Client(api_key=api_key)

# Prompt
prompt = """
Generate a production-ready Dockerfile for a Flask application.
The application runs on port 5000.
Only provide Dockerfile content.
"""

# Generate response
response = client.models.generate_content(
        model="gemini-2.5-flash",
    contents=prompt
)

# Extract text
dockerfile_content = response.text.strip()

# Remove markdown formatting
dockerfile_content = dockerfile_content.replace("```dockerfile", "")
dockerfile_content = dockerfile_content.replace("```", "")
dockerfile_content = dockerfile_content.strip()
# Print output
print(dockerfile_content)

# Save Dockerfile
with open("Dockerfile", "w") as file:
    file.write(dockerfile_content)

print("Dockerfile generated successfully")
