#!/bin/bash
# setup pacchetti stack LAMP, MySQL user root account
sudo apt-get -y update
sudo apt-get -y install apache2
# Root di MySQL
sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password xpepper'
sudo debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password xpepper'
# User MySQL per Vagrant
mysql -uroot -pxpepper -e "CREATE USER vagrant@localhost IDENTIFIED BY 'vagrant';"
echo "Utente Vagrant creato!"
mysql -uroot -pxpepper -e "GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'localhost';"
mysql -uroot -pxpepper -e "FLUSH PRIVILEGES;"
echo "Grant utente Vagrant ok!"
# Installo i pacchetti
sudo apt-get -y install mysql-server libapache2-mod-auth-mysql php5-mysql
sudo apt-get -y install php5 libapache2-mod-php5 php5-mcrypt php5-curl libssh2-php python-mysqldb
