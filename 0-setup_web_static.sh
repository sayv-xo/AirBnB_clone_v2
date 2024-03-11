#!/usr/bin/env bash
# set up server to deploy static site
sudo apt -y update
sudo apt -y install nginx
mkdir -p /data/web_static/shared /data/web_static/releases/test
printf %s "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -hR ubuntu:ubuntu /data/
SERVER_CONFIG=\
"server {
	listen 80 default_server;
	listen [::]:8080 default_server;
	root /var/www/html/;
	index index.html index.htm index.nginx-debian.html;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://google.com;
	}

	error_page 404 /404.html;
	location /404.html {
		internal;
	}

	add_header X-Served-By \$hostname;
}"
printf %s "$SERVER_CONFIG" > /etc/nginx/sites-available/default
sudo service nginx restart
