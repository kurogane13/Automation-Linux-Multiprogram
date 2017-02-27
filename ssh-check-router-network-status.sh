#!/bin/sh

#Remember to install sshpass for this script to run

#sudo apt-get install sshpass

#Remember to enter these lines at the bottom in /etc/ssh/ssh_config
#with the following commands, to avoid ssh-key warning!!

#sudo nano /etc/ssh/ssh_config

#nosshcheck="StrictHostKeyChecking no"
#knownsshhost="UserKnownHostsFile=/dev/null"

namedfile=

touch /home/cisco-ssh-access-scripts-logs/check-device-network-status/$namedfile-check-device.txt

host=
port=22
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

( echo ${enable}
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
sleep 1 ) | sshpass -p $pass ssh $user@$host | tee /home/cisco-ssh-access-scripts-logs/check-device-network-status/$namedfile-check-device.txt
echo "----------------------------------------------------------------------------------------------"
echo "SCRIPT EXECUTION FINISHED"
echo "----------------------------------------------------------------------------------------------"
echo "YOU CAN VIEW THE OUTPUT LOGGED IN THE FILE HERE: "
ls -a -l -h /home/cisco-ssh-access-scripts-logs/check-device-network-status/$namedfile-check-device.txt
echo "----------------------------------------------------------------------------------------------"
echo "TO VIEW IT, USE THE FOLLOWING COMMAND: "
echo "cat /home/cisco-ssh-access-scripts-logs/name_of_your_file.txt"
echo "----------------------------------------------------------------------------------------------"
echo "DO YOU WISH TO VIEW THE FILE NOW?  HIT ENTER TO VIEW/CTRL+C TO ABORT AND RETURN TO MAIN MENU..."
read -s selectedchoice
cat /home/cisco-ssh-access-scripts-logs/check-device-network-status/$namedfile-check-device.txt
echo "----------------------------------------------------------------------------------------------"
echo "HIT ENTER TO GET BACK TO PREVIOUS SCREEN..."
read -s entertogetbacktomain







