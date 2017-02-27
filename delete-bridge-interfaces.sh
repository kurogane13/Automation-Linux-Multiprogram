sudo brctl show

ip link show

sudo ifconfig br0 down

sudo ifconfig tap0 down

sudo ip link delete br0

sudo ip link delete tap0

sudo ip link delete tap1

sudo ip link delete tap2

sudo brctl delif br0 tap0

sudo brctl delif br0 eth0

sudo brctl show

ip link show

sudo route del -net 192.168.0.0 netmask 255.255.255.0 dev br0
sudo route del -net 192.168.1.0 netmask 255.255.255.0 dev br0
sudo route del -net 192.168.2.0 netmask 255.255.255.0 dev br0
