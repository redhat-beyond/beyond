class Hash
  def slice(*keep_keys)
    h = {}
    keep_keys.each { |key| h[key] = fetch(key) if has_key?(key) }
    h
  end unless Hash.method_defined?(:slice)
  def except(*less_keys)
    slice(*keys - less_keys)
  end unless Hash.method_defined?(:except)
end

# Specify minimum Vagrant version
Vagrant.require_version '= 2.2.10'

Vagrant.configure("2") do |config|
  config.vagrant.plugins= ["vagrant-env"]
  config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: [ "venv/", ".git/", ".idea/" ]
  config.vm.provision :docker
  config.env.enable

  config.vm.provision "shell", path: "bootstrap.sh"

  config.vm.define "dev" do |dev|
    dev.vm.box = "bento/ubuntu-18.04"
    dev.vm.network "forwarded_port", guest: 5000, host: 5000
  end

  config.vm.define "stage" do |stage|

    stage.vm.box = "dummy"
    stage.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

    stage.vm.provider :aws do |aws,override|
      override.nfs.functional = false
      aws.aws_profile = ENV['PROFILE_STAGE']
      aws.keypair_name = ENV['KEY_NAME_STAGE']
      aws.ami = ENV['AMI_STAGE']
      aws.instance_type = ENV['INSTANCE_TYPE_STAGE']
      aws.region = ENV['REGION_STAGE']
      aws.subnet_id = ENV['SUBNET_ID_STAGE']
      aws.security_groups = ENV['SECURITY_GROUPS_STAGE']
      aws.associate_public_ip = true
      override.ssh.username = ENV['USERNAME_STAGE']
      override.ssh.private_key_path = ENV['PRIVATE_KEY_PATH_STAGE']
    end

  end

  config.vm.define "prod" do |prod|

    prod.vm.box = "dummy"
    prod.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

    prod.vm.provider :aws do |aws,override|
      override.nfs.functional = false
      aws.aws_profile = ENV['PROFILE_PROD']
      aws.keypair_name = ENV['KEY_NAME_PROD']
      aws.ami = ENV['AMI_PROD']
      aws.instance_type = ENV['INSTANCE_TYPE_PROD']
      aws.region = ENV['REGION_PROD']
      aws.subnet_id = ENV['SUBNET_ID_PROD']
      aws.security_groups = ENV['SECURITY_GROUPS_PROD']
      aws.elastic_ip = ENV['ELASTIC_IP']
      override.ssh.username = ENV['USERNAME_PROD']
      override.ssh.private_key_path = ENV['PRIVATE_KEY_PATH_PROD']
    end

  end

end
