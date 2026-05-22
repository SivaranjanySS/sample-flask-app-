import os

subdomain = "flask"
domain = "sivaranjany.online"

container_port = 5000

nginx_config = f"""
server {{
    listen 80;

    server_name {subdomain}.{domain};

    location / {{
        proxy_pass http://localhost:{container_port};
    }}
}}
"""

config_path = f"/etc/nginx/sites-available/{subdomain}"

with open(subdomain, "w") as f:
    f.write(nginx_config)

os.system(f"sudo mv {subdomain} {config_path}")

os.system(
    f"sudo ln -s {config_path} /etc/nginx/sites-enabled/"
)

os.system("sudo nginx -t")
os.system("sudo systemctl restart nginx")

print("NGINX configured successfully")
