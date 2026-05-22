import os

IMAGE_NAME = "sivaranjany/ai-deploy-app:v1"

# Pull latest image
os.system(f"docker pull {IMAGE_NAME}")

# Stop old container
os.system("docker stop ai-container")

# Remove old container
os.system("docker rm ai-container")

# Run latest container
os.system(
    f"docker run -d -p 5000:5000 --name ai-container {IMAGE_NAME}"
)

print("Latest deployment completed")
