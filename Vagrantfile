# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # For dev and config API Gateway
  config.vm.define "dev" do |dev|

    dev.vm.hostname = "dev"
    dev.vm.box = "ubuntu/bionic64"
    dev.vm.synced_folder ".", "/dev", SharedFoldersEnableSymlinksCreate: false
    dev.vm.network "forwarded_port", guest: 80, host: 1080
    dev.vm.network "private_network", ip: "192.168.50.10"

    dev.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--name", "dev"]
      vb.memory = "1024"
    end 

    dev.vm.provision :docker
    dev.vm.provision :docker_compose

    dev.vm.provision "shell", path: "dev_provision.sh"
  end

  # For staging and config API Gateway
  config.vm.define "staging" do |staging|

    staging.vm.hostname = "staging"
    staging.vm.box = "ubuntu/bionic64"
    staging.vm.synced_folder ".", "/staging", SharedFoldersEnableSymlinksCreate: false
    staging.vm.network "forwarded_port", guest: 80, host: 2080
    staging.vm.network "private_network", ip: "192.168.60.10"

    staging.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--name", "staging"]
      vb.memory = "1024"
    end 

    staging.vm.provision :docker
    staging.vm.provision :docker_compose

    staging.vm.provision "shell", path: "staging_provision.sh"
  end
end

