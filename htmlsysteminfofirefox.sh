#!/bin/bash
clear
sleep 2
echo "##########################################################################################################"
echo "SYSTEMINFO PROGRAM INITIATED, DETAILED HARDWARE INFO FROM THIS SYSTEM WILL BE DISPLAYED IN HTML FORMAT"
echo
echo "WITH FIREFOX WEB BROWSER"
echo "----------------------------------------------------------------------------------------------------------"
sleep 4
echo "=========================================================================================================="
sleep 2
lshw -html > lshw.html
sleep 1
sudo notify-send "HTML REPORT GENERATED, ONCE YOU CLOSE THIS TAB YOU WILL RETURN TO MAIN MENU..."
firefox -new-tab -url lshw.html
clear
echo "Your Detailed system information, displayed in firefox in html format,  is here: "
echo "---------------------------------------------------------------------------------"
sleep 3
sudo ls -l -h | grep lshw.html

