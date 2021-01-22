#!/usr/bin/env bash
# Add a custom HTTP header with Puppet


exec { 'header':
command  => 'sudo apt-get update && sudo apt-get install -y nginx && echo "Holberton School for the win!" | sudo tee /var/www/html/index.html && sed -i "/server_name _;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sudo sed -i "/http {/a \ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf && sudo service nginx restart',
provider => shell,
}
