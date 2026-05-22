import os
import subprocess

DOCKER_USERNAME = "sivaranjany"

IMAGE_NAME = f"{DOCKER_USERNAME}/ai-deploy-app:v1"

CONTAINER_NAME = "ai-container"

print("Starting AI deployment pipeline...")

# Generate Dockerfile
os.system("python ai_generator.py")

# Stop old containers
os.system("docker stop $(docker ps -q)")
os.system("docker rm $(docker ps -aq)")

# Build image
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

# Run container
run = subprocess.run(
    f"docker run -d -p 5000:5000 --name {CONTAINER_NAME} {IMAGE_NAME}",
    shell=True
)

if run.returncode != 0:
    print("Container run failed")
    exit()

print("Deployment completed successfully")
