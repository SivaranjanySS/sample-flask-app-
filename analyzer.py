import os

files = os.listdir()

if "requirements.txt" in files:
    print("python")

elif "package.json" in files:
    print("node")

elif "pom.xml" in files:
    print("java")
