Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provision "shell", path: "bootstrap.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
end
