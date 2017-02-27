#!/bin/bash
clear
sleep 1
sudo rm systeminfologs.txt
clear
sudo touch /home/systeminfologs.txt
echo "####################################################################"
echo "SYSTEMINFO PROGRAM INITIATED..."
sleep 2
echo "===================================================================="
echo "Program starts now..."
sleep 2 
echo "--------------------------------------------------------------------"
echo "Writing report to txt file..."
sleep 1
( echo "Hello, $USER" 
echo 
echo "Today's date is `date`, this is week `date +"%V"`." 
echo
sleep 4
echo "SHOWING SUMMARIZED HARDWARE INFORMATION ABOUT YOUR SYSTEM"
echo "--------------------------------------------------------------------"
lshw -short
echo "--------------------------------------------------------------------"
echo "These users are currently connected now:" 
echo 
w | cut -d " " -f 1 - | grep -v USER | sort -u 
echo 
echo "--------------------------------------------------------------------"
echo "This is `uname -s` running on a `uname -m` processor." 
echo 
echo "--------------------------------------------------------------------"
echo "Showing system uptime:" 
uptime 
echo
echo "Free and available memory..."
echo
free -m -h
echo "--------------------------------------------------------------------"
echo "Used and available disk file space in your system.."
df -h
echo
echo "--------------------------------------------------------------------"
echo
echo "Installed memory modules, and available slots/banks in motherboard..."
echo
sudo dmidecode -t memory
echo
echo "--------------------------------------------------------------------"
echo 
echo "--------------------------------------------------------------------"
echo "Showing usb tree..." 
echo 
lsusb -t 
echo 
echo "--------------------------------------------------------------------"
echo "Showing pci list..." 
echo 
lspci 
echo 
echo "--------------------------------------------------------------------"
echo "Screen dimensions are:" 
echo 
xdpyinfo  | grep dimensions
echo
echo
echo "--------------------------------------------------------------------"
echo "Networking information..." 
echo 
ifconfig -a
echo 
echo
echo "--------------------------------------------------------------------"
echo "Scanning available wireless SSID´s..." 
echo 
sudo iw dev wlan0 scan | grep SSID 
echo 
echo 
echo "--------------------------------------------------------------------"
echo "Displaying connection status to current SSID..." 
echo 
iwconfig wlan0 
echo 
echo "--------------------------------------------------------------------"
echo "Running arp-a scan..." 
echo 
echo 
arp -a                
echo
echo "--------------------------------------------------------------------"
echo 
netstat -s 
echo 
echo "--------------------------------------------------------------------"
echo
route -n 
echo
echo "--------------------------------------------------------------------"
echo
echo "Listing all current active internet connections..." 
echo 
echo 
lsof -i 
echo
echo "--------------------------------------------------------------------"
echo
echo 
echo  ) | tee -a > /home/systeminfologs.txt
echo
sleep 1
echo
echo "Your systeminfologs file is here: "
echo "--------------------------------------------------------------"
ls -l -h | grep systeminfologs.txt
echo
echo "--------------------------------------------------------------------"
echo
echo
echo
sleep 1
sudo gedit /home/systeminfologs.txt


