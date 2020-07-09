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

Vagrant.configure("2") do |config|
  config.vagrant.plugins= ["vagrant-env"]
  config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: [ "venv/", ".git/", ".idea/" ]
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
      aws.keypair_name = "aws_key_pair"
      aws.ami = "ami-0701e7be9b2a77600"
      aws.instance_type = "t2.micro"
      aws.region = "eu-west-1c"
      aws.subnet_id = ENV['SUBNET_ID']
      aws.security_groups = ENV['SECURITY_GROUPS']
      aws.associate_public_ip = true
      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = ENV['PRIVATE_KEY_PATH']
    end

  end

end
