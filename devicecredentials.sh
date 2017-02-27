#!/bin/bash

echo "Enter ip address of host: "

read ipaddress

sed -i "s/\(^host=\).*/\1$ipaddress/" $INPUT /home/test/ssh-running-config.sh

echo "Username: "

read user

sed -i "s/\(^user=\).*/\1$user/" $INPUT /home/test/ssh-running-config.sh

echo "Password: "

read -s pass

sed -i "s/\(^pass=\).*/\1$pass/" $INPUT /home/test/ssh-running-config.sh

echo "Enable password: "

read -s enablepass 

sed -i "s/\(^enablepass=\).*/\1$enablepass/" $INPUT /home/test/ssh-running-config.sh

#openssl aes-256-cbc -salt -in /home/test/ssh-running-config.sh -out /home/test/ssh-running-config.sh.enc -pass file:/home/test/ssh-running-config.sh

#openssl aes-256-cbc -d -salt -in /home/test/ssh-running-config.sh.enc -out /home/test/ssh-running-config.sh.dec -pass file:/home/test/ssh-running-config.sh

