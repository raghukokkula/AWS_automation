#!/bin/bash
yum update -y
yum install httpd -y
cd /var/www/html
echo "Web Server 1 - Northern Virginia" > index.html
service httpd start
chkconfig httpd on