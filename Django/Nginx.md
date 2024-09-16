```                   
# Configuration for the Django user panel on port 80
server {
    listen 80;
    server_name 127.0.0.1;

    location / {
        proxy_pass http://127.0.0.1:8000/admin;  # Forward requests to Django
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /home {
        return 403;  # Deny access to /home from this server
    }

    location /admin {
        proxy_pass http://127.0.0.1:8000/admin;  # Forward /admin requests to Django admin
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
}

# Configuration for the Django user panel on port 85
server {
    listen 85;
    server_name 127.0.0.1;

    location / {
        proxy_pass http://127.0.0.1:8000/home;  # Pass all requests to Django
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        absolute_redirect off;
    }

    # Handle /home route explicitly if needed, but without the return 403
    location /home {
        proxy_pass http://127.0.0.1:8000/home;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        absolute_redirect off;
    }

    # Optionally handle /admin route
    location /admin {
        return 403;  # Forbidden access to /admin on port 85
    }
}


```
