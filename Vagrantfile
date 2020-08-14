Vagrant.configure("2") do |config|
  config.vm.box = "fedora/32-cloud-base"
  config.vm.provider "virtualbox" do |v|
  	v.memory = 2048
  	v.cpus = 2
  end

  # Django ports forward
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Override's the default "RSYNC" (one-way sync)
  # => Makes it two-way sync
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

  # Initialization scripts
  config.vm.provision "shell", privileged: true,
    path: "./init_scripts/init-root.sh"
  config.vm.provision "shell", privileged: false,
    path: "./init_scripts/init-user.sh"
end
