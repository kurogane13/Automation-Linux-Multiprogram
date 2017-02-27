#!/bin/bash

echo "##############################################################################################################"
echo "TELNET SCRIPT MODE ACCESSED..."
echo "##############################################################################################################"
echo "THIS PROGRAM WILL CREATE A SHELL SCRIPT TO GET THE RUNNING CONFIG FROM A CISCO ROUTER"
echo "--------------------------------------------------------------------------------------------------------------"
echo "YOU WILL NEED TO PROVIDE THE FOLLOWING NECESSARY DATA TO GET THE SCRIPT CREATED"
echo "--------------------------------------------------------------------------------------------------------------"
echo "1 - SCRIPT FILENAME - PROVIDE A NAME FOR YOUR SCRIPT. EXAMPLE: ROUTER1"
echo "2 - HOST IP ADDRESS IN THE FOLLOWING FORMAT X.X.X.X, OR HOST FQDN ( IF YOU HAVE A DNS RESOLVER FOR IT )"
echo "3 - USERNAME ( CISCO ROUTER´S USERNAME )"
echo "4 - PASSWORD ( CISCO ROUTER´S PASSWORD )"
echo "5 - ENABLE PASSWORD ( CISCO ROUTER´S GLOBAL CONFIGURATION MODE PASSWORD )"
echo "--------------------------------------------------------------------------------------------------------------"
echo "ONCE YOU HAVE ALL THE DATA REQUESTED ABOVE, HIT ENTER TO BEGIN, OR CTRL+C TO ABORT PROGRAM: "
read -s enter
echo "-----------------------------------------------------------------------------------------------------"

echo "SCRIPT CREATION PROCESS INITIATED..."

echo "-----------------------------------------------------------------------------------------------------"

echo "Enter file name to create script: "

read filename

echo "-----------------------------------------------------------------------------------------------------"

echo "Named file is: " 

echo $filename

for file in 1.sh ; do cp -r -pi /home/telnet-running-config-template.sh $filename ; done

sudo mv $filename $filename.sh

sudo mv $filename.sh /home/cisco-telnet-access-scripts-logs/

sed -i "s/\(^namedfile=\).*/\1$filename/" $INPUT /home/cisco-telnet-access-scripts-logs/$filename.sh

echo "-----------------------------------------------------------------------------------------------------"

echo "Enter ip address of host: "

read ipaddress

sed -i "s/\(^host=\).*/\1$ipaddress/" $INPUT /home/cisco-telnet-access-scripts-logs/$filename.sh

echo "-----------------------------------------------------------------------------------------------------"

echo "Username: "

read user

sed -i "s/\(^user=\).*/\1$user/" $INPUT /home/cisco-telnet-access-scripts-logs/$filename.sh

echo "-----------------------------------------------------------------------------------------------------"

echo "Password: "

read -s pass

sed -i "s/\(^pass=\).*/\1$pass/" $INPUT /home/cisco-telnet-access-scripts-logs/$filename.sh

echo "-----------------------------------------------------------------------------------------------------"

echo "Enable Password: "

read -s enablepass

sed -i "s/\(^enablepass=\).*/\1$enablepass/" $INPUT /home/cisco-telnet-access-scripts-logs/$filename.sh
echo "-----------------------------------------------------------------------------------------------------"

echo "Your script file is here: "

ls -l -h -t -s /home/cisco-telnet-access-scripts-logs/$filename.sh

echo "-----------------------------------------------------------------------------------------------------"
echo "Hit enter to run the script now, or press CTRL+C to abort: "
read -s enter
echo "-----------------------------------------------------------------------------------------------------"
sudo bash /home/cisco-telnet-access-scripts-logs/$filename.sh 
