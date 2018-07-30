#!/usr/bin/env bash
# configures a new Ubuntu machine with installed nginx web server
if ! which nginx > /dev/null 2>&1;
then
    apt-get -y update
    apt-get -y install nginx
fi
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "good luck!" > /data/web_static/releases/test/index.html
ln -f -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default
service nginx restart
