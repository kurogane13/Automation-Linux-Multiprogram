
sudo apt-get install uml-utilities   

sudo apt-get install bridge-utils 

modprobe tun

#below command will creat tap interface

sudo tunctl -u $USER

#below command will create a bridge interface (br0), and bond tap and etho together

sudo brctl addbr br0

sudo brctl addif br0 tap0   

sudo brctl addif br0 eth0

sudo brctl show

sudo ifconfig br0 up

sudo ifconfig tap0 up

#edit this entry and enter the network address and subnet mask of your lan

sudo ifconfig br0 192.168.0.205/24

sudo route add -net 192.168.0.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.1.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.2.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.3.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.4.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.5.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.6.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.7.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.8.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.9.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.10.0 netmask 255.255.255.0 dev br0

