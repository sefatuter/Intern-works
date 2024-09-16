```
$ /etc/nginx/sites-available$ sudo nano djangoTask
$ sudo rm /etc/nginx/sites-enabled/djangoTask
$ sudo nginx -t
$ sudo ln -s /etc/nginx/sites-available/djangoTask /etc/nginx/sites-enabled/
$ sudo systemctl restart nginx
```
