# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "staging" do |staging|

    staging.vm.hostname = "staging"
    staging.vm.box = "ubuntu/trusty64"
    staging.vm.synced_folder ".", "/vagrant"
    staging.vm.network "private_network", ip: "192.168.57.10"

    staging.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--name", "staging"]
      vb.memory = "1024"
    end 

    staging.vm.provision :docker
    staging.vm.provision :docker_compose

    staging.vm.provision "shell", path: "provision.sh"
  end
end


# Vagrant.configure("2") do |config|
#   config.vm.box = "ubuntu/bionic64"
#   config.vm.synced_folder ".", "/vagrant"
#   config.vm.network "private_network", ip: "192.168.57.10"

#   config.vm.provision :docker
#   config.vm.provision :docker_compose

#   config.vm.provision "shell", inline: <<-SHELL
#     cd /vagrant
#     pwd
#     ls -la
#     cd /vagrant/Python_Flask
#     chmod 777 -R ./Docker/redis_dump
#     sh start.sh
#     docker exec -i mongo-db mongorestore --archive --gzip < ./Docker/mongo_dump.gz
    
#     docker ps -a 
#     sleep 5
#     docker exec -i mysql-db /usr/bin/mysql -uroot -pdryan --force tadp < ./Docker/mysql_dump.sql
#   SHELL
# end



