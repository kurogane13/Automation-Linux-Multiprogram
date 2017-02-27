
#sudo apt-get install sshpass

#Remember to enter these lines at the bottom in /etc/ssh/ssh_config
#with the following commands, to avoid ssh-key warning!!

#sudo nano /etc/ssh/ssh_config

#nosshcheck="StrictHostKeyChecking no"
#knownsshhost="UserKnownHostsFile=/dev/null"

touch /home/ssh-tkinter-router/ssh-tkinter-running-config.txt

host=192.168.0.21
user=cisco
pass=cisco12345
enable=ena
enablepass=cisco12345
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
sleep 1 ) | sshpass -p $pass ssh $user@$host | tee /home/ssh-tkinter-router/ssh-tkinter-running-config.txt

libreoffice /home/ssh-tkinter-router/ssh-tkinter-running-config.txt
