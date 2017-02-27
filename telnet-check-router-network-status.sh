#!/bin/sh

namedfile=

touch /home/cisco-telnet-access-scripts-logs/$namedfile.txt

host=
port=23
user=
pass=
enablepass=
enable=ena
termlength="terminal length 0"
showipintbr="sh ip int br"
showver="sh version"
exitdevice="exit"
shiproute="sh ip route"
shcdpnede="sh cdp nei de"
shippro="sh ip pro"
shipospf="sh ip ospf nei"
shipeigrp="sh ip eigrp nei"
shipbgpsu="sh ip bgp sum"
showrun="show run"
shlog="sh log"
 

sleep 2
echo "-------------------------------"
echo "Accessing device..."
sleep 2
echo "-------------------------------"

( echo open ${host}
sleep 1
echo ${user}
sleep 1
echo ${pass}
sleep 1
echo ${enable}
sleep 1
echo ${enablepass}
sleep 1
echo ${termlength}
sleep 1
echo ${showver}
sleep 1
echo ${showipintbr}
sleep 1
echo ${shiproute}
sleep 1
echo ${shippro}
sleep 1
echo ${shipospf}
sleep 1
echo ${shipeigrp}
sleep 1
echo ${shipbgpsu}
sleep 1
echo ${shcdpnede}
sleep 1
echo ${showrun}
sleep 1
echo ${shlog}
sleep 1
echo ${exitdevice}
sleep 1 ) | script -c telnet | tee /home/cisco-telnet-access-scripts-logs/$namedfile.txt

libreoffice /home/cisco-telnet-access-scripts-logs/$namedfile.txt


 











