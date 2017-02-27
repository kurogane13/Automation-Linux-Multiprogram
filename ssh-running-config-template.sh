
#sudo apt-get install sshpass

#Remember to enter these lines at the bottom in /etc/ssh/ssh_config
#with the following commands, to avoid ssh-key warning!!

#sudo nano /etc/ssh/ssh_config

#nosshcheck="StrictHostKeyChecking no"
#knownsshhost="UserKnownHostsFile=/dev/null"

namedfile=

touch /home/cisco-ssh-access-scripts-logs/running-configs/$namedfile-running-config.txt

host=
user=
pass=
enable=ena
enablepass=
port=22
termlength="terminal length 0"
exitdevice="exit"
showrun="show run"

 
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
echo ${showrun}
sleep 1
echo ${exitdevice}
sleep 1 ) | sshpass -p $pass ssh $user@$host | tee /home/cisco-ssh-access-scripts-logs/running-configs/$namedfile-running-config.txt
echo "----------------------------------------------------------------------------------------------"
echo "SCRIPT EXECUTION FINISHED"
echo "----------------------------------------------------------------------------------------------"
echo "YOU CAN VIEW THE OUTPUT LOGGED IN THE FILE HERE: "
ls -a -l -h /home/cisco-ssh-access-scripts-logs/running-configs/$namedfile-running-config.txt
echo "----------------------------------------------------------------------------------------------"
echo "TO VIEW IT, USE THE FOLLOWING COMMAND: "
echo "cat /home/cisco-ssh-access-scripts-logs/name_of_your_file.txt"
echo "----------------------------------------------------------------------------------------------"
echo "DO YOU WISH TO VIEW THE FILE NOW?  HIT ENTER TO VIEW/CTRL+C TO ABORT AND RETURN TO MAIN MENU..."
read -s selectedchoice
cat /home/cisco-ssh-access-scripts-logs/running-configs/$namedfile-running-config.txt
echo "----------------------------------------------------------------------------------------------"
echo "HIT ENTER TO GET BACK TO PREVIOUS SCREEN..."
read -s entertogetbacktomain

