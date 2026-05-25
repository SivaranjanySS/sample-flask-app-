import os

folders = ["flask-app", "node-app", "django-app"]

for folder in folders:

    files = os.listdir(folder)

    if "requirements.txt" in files:
        print(f"{folder} -> flask")

    elif "package.json" in files:
        print(f"{folder} -> node")

    elif "manage.py" in files:
        print(f"{folder} -> django")
