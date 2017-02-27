
#!/bin/bash
sudo touch /home/connection-reload.txt

echo "NOTE: THIS SCRIPT WILL RUN ONLY IF NMCLI ( NETWORK MANAGEMENT COMMAND LINE ) IS INSTALLED IN YOUR SYSTEM"
echo "--------------------------------------------------------------------------------------------------------"
echo "INITIATING SCRIPT..."
sleep 2
notify-send "Reloading all network interfaces, this may take a few seconds..."
sleep 2

nmcli networking off 


nmcli networking on

echo "ALL NETWORK INTERFACES WERE RELOADED..."






