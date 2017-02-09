# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "public_network"
  # Parte VBox
  config.vm.provider "virtualbox" do |vb|
  vb.memory = "2048"
  end
  # Parte bash
  config.vm.define "lampstack" do|lampstack|
  lampstack.vm.hostname = "lampstack"
  lampstack.vm.provision :shell, path: "apt_step.sh"
  end
  # Parte Ansible (esegui un provision alla volta)
  config.vm.provision :ansible do |ansible|
  ansible.playbook = "ansible_step/playbook.yml"
 end

end
