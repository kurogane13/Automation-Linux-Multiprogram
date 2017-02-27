

touch /home/telnet-tkinter-router/telnet-tkinter-running-config.txt

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
sleep 1 ) | script -c telnet | tee /home/telnet-tkinter-router/telnet-tkinter-running-config.txt

firefox /home/telnet-tkinter-router/telnet-tkinter-running-config.txt
