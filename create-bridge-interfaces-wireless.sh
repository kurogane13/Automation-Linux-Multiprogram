sudo apt-get install uml-utilities   

sudo apt-get install bridge-utils 

modprobe tun

#below command will creat tap interface

sudo tunctl -u $USER

#below commanda will create a bridge interface (br0), and bond tap and etho together

sudo brctl addbr br0

sudo brctl addif br0 tap0

iw dev <wifiInterface> set 4addr on  

sudo brctl addif br0 wlan0

sudo brctl show

sudo ifconfig br0 up

sudo ifconfig tap0 up

#edit this entry and enter the network address and subnet mask of your lan

sudo ifconfig br0 192.168.0.210/24

sudo route add -net 192.168.0.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.1.0 netmask 255.255.255.0 dev br0
sudo route add -net 192.168.2.0 netmask 255.255.255.0 dev br0
