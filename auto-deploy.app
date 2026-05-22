import os
import subprocess

IMAGE_NAME = "ai-deploy-app"
CONTAINER_NAME = "ai-container"

print("Starting AI deployment pipeline...")

# Step 1 - Generate Dockerfile
print("Generating Dockerfile using AI...")
os.system("python ai-generator.py")

# Step 2 - Stop old container
print("Stopping old container...")
os.system(f"docker stop {CONTAINER_NAME}")

# Step 3 - Remove old container
print("Removing old container...")
os.system(f"docker rm {CONTAINER_NAME}")

# Step 4 - Build Docker image
print("Building Docker image...")
build = subprocess.run(
    f"docker build -t {IMAGE_NAME} .",
    shell=True
)

if build.returncode != 0:
    print("Docker build failed")
    exit()

# Step 5 - Run new container
print("Running new container...")
run = subprocess.run(
    f"docker run -d -p 5000:5000 --name {CONTAINER_NAME} {IMAGE_NAME}",
    shell=True
)

if run.returncode != 0:
    print("Container run failed")
    exit()

print("Deployment completed successfully")
