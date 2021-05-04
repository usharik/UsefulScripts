#! /bin/sh
sudo apt purge mysql-server mysql-client mysql-common
sudo apt autoremove
sudo rm -rf /var/lib/mysql*

sudo apt update
sudo apt install mysql-server
mysqld --initialize
sudo /usr/bin/mysql_secure_installation
