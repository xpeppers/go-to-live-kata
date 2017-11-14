#!/bin/bash  
# Bash scripting to download and install vagrant on debian like linux distribution x86_64

VAGRANTINSTALLERURL=https://releases.hashicorp.com/vagrant/2.0.1/vagrant_2.0.1_x86_64.deb
TOOLSDIR=tools

mkdir "$TOOLSDIR"
wget -c "$VAGRANTINSTALLERURL" -P "$TOOLSDIR"

sudo dpkg -i "$TOOLSDIR"/vagrant_2.0.1_x86_64.deb

echo `dpkg -s vagrant`

vagrant plugin install vagrant-docker-compose


