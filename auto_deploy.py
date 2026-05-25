import os
import subprocess

DOCKER_USERNAME = "sivaranjany"

IMAGE_NAME = f"{DOCKER_USERNAME}/ai-deploy-app:v1"

CONTAINER_NAME = "ai-container"

print("Starting AI deployment pipeline...")

# Generate Dockerfile automatically
os.system("python ai_generator.py")

# Stop old container safely
os.system(f"docker stop {CONTAINER_NAME} || true")

# Remove old container safely
os.system(f"docker rm {CONTAINER_NAME} || true")

# Pull latest code image if exists
os.system(f"docker pull {IMAGE_NAME} || true")

# Build Docker image
build = subprocess.run(
    f"docker build -t {IMAGE_NAME} .",
    shell=True
)

if build.returncode != 0:
    print("Docker build failed")
    exit()

# Push image to DockerHub
push = subprocess.run(
    f"docker push {IMAGE_NAME}",
    shell=True
)

if push.returncode != 0:
    print("Docker push failed")
    exit()

# Run new container
run = subprocess.run(
    f"docker run -d -p 5000:5000 --name {CONTAINER_NAME} {IMAGE_NAME}",
    shell=True
)

if run.returncode != 0:
    print("Container run failed")
    exit()

print("Deployment completed successfully")
