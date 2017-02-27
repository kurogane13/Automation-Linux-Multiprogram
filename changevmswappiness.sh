

sudo sed -i "s/\(^vm.swapiness=\).*/\1$2/" $INPUT /etc/sysctl.conf
