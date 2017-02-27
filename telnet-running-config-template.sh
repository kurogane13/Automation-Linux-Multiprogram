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
showrun="show run"

 

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
echo ${showrun}
sleep 1
echo ${exitdevice}
sleep 1 ) | script -c telnet | tee /home/cisco-telnet-access-scripts-logs/$namedfile.txt

libreoffice /home/cisco-telnet-access-scripts-logs/$namedfile.txt
