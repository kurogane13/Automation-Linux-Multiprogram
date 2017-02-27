
#!/bin/bash
sudo touch /home/connection-reload.txt

echo "NOTE: THIS SCRIPT WILL RUN ONLY IF NMCLI ( NETWORK MANAGEMENT COMMAND LINE ) IS INSTALLED IN YOUR SYSTEM"
echo "--------------------------------------------------------------------------------------------------------"
echo "INITIATING SCRIPT..."
sleep 5
notify-send "Reloading all network interfaces, this may take a few seconds..."
sleep 5

( nmcli networking off 


nmcli networking on 

sleep 10

ifconfig -a
echo "------------------------------------------------------------------"
nmcli general status
sleep 2
echo "-----------------------------------------------------------------"
nmcli connection show --active 
echo "................................................................." ) 
( echo "THIS FILE WAS SAVED UNDER THE NAME OF CONNECTION-RELOAD.TXT, AND"
echo "WAS SAVED IN THE SAME PATH WHERE THIS PROGRAM WAS EXECUTED"
echo "-----------------------------------------------------------------"
echo "File generated on:"
date
echo "-----------------------------------------------------------------"
echo "System information:"
uname -a 
echo "-----------------------------------------------------------------"
ifconfig
echo "-----------------------------------------------------------------"
iwconfig wlan0
echo "-----------------------------------------------------------------"
iwlist scan
echo "-----------------------------------------------------------------"
sudo netstat -tup
echo "-----------------------------------------------------------------"
nmcli device show 
) | sudo tee -a > /home/connection-reload.txt
echo "-----------------------------------------------------------------"



echo "Generating connection report in 3 seconds..."
sleep 3 
echo "-----------------------------------------------------------------"

echo " Exported output log to connection-reload.txt.."
sleep 2
echo " Opening output log from connection-reload.txt.."
sleep 2
notify-send "Output log opened"
sudo gedit /home/connection-reload.txt
notify-send "YOU ARE VIEWING THE REPORT NOW, ONCE CLOSED YOU WILL RETURN TO MAIN MENU"



