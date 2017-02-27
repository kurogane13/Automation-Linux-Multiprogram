if which nmap >/dev/null; then
    sudo touch /home/nmaplogs.log
    echo "------------------------------------------------------------------"
    echo "Nmap is installed in this system , in order to start scanning your lan, "
    echo "Enter your lan ip network segment in the following format: x.x.x.x/xx"
    echo "------------------------------------------------------------------"
    read  enteripaddressrange0
    echo "------------------------------------------------------------------"
    echo "You entered: " 
    echo  $enteripaddressrange0
    space=" "
    echo "------------------------------------------------------------------"
    echo "HIT ENTER TO START SCANNING YOUR LAN NOW..."
    read startscannow
    nmap -sT $space $enteripaddressrange0 | tee -a /home/nmaplogs.log
    echo "=================================================================="
    echo "LOG FILE IS 'nmaplog.log', AND IS LOCATED AT /home/nmaplogs.log"
    ls -a -h -t -l /home/nmaplogs.log
    echo "------------------------------------------------------------------"
    echo "YOU CAN VIEW IT THEN USING THE FOLLOWING COMMAND: "
    echo "cat /home/nmaplogs.log"
    echo "------------------------------------------------------------------"
    echo "##################################################################"
    echo "SCAN COMPLETED HIT ENTER TO RETURN TO MAIN MENU"
    read scancompleted

    
    
else
    sudo touch /home/nmaplogs.log
    echo "##############################################################"
    echo "NMAP IS NOT INSTALLED IN YOUR SYSTEM..."
    echo "#############################################################"
    echo "-------------------------------------------------------------"
    echo "IT MUST BE INSTALLED FIRST, IN ORDER TO PROCEED. "
    echo "-------------------------------------------------------------"
    echo "HIT ENTER TO INSTALL IT NOW, OR PRESS CTRL+C TO ABORT... " 
    read installnmap
    sudo apt-get install nmap
    echo "-------------------------------------------------------------"
    echo "Enter your lan ip network segment in the following format: x.x.x.x/xx"
    read  enteripaddress1
    echo "------------------------------------------------------------"
    echo "You entered: " 
    echo  $enteripaddress1
    space=" "
    echo "------------------------------------------------------------"
    echo "HIT ENTER TO START SCANNING YOUR LAN NOW..."
    read startscannow1
    nmap -sT $space $enteripaddress1 | tee -a /home/nmaplogs.log
    echo "=================================================================="
    echo "LOG FILE IS 'nmaplog.log', AND IS LOCATED AT /home/nmaplogs.log"
    ls -a -h -t -l /home/nmaplogs.log
    echo "------------------------------------------------------------------"
    echo "YOU CAN VIEW IT THEN USING THE FOLLOWING COMMAND: "
    echo "cat /home/nmaplogs.log"
    echo "------------------------------------------------------------------"
    echo "##################################################################"
    echo "SCAN COMPLETED HIT ENTER TO RETURN TO MAIN MENU"
    read scancompleted1

fi
