#!/bin/bash/

echo "#######################################################################################"
echo "USAGE EXAMPLE NOTE: TO FIND AN EXPRESSION IN THE FILE 'SAMPLE.TXT', LOCATED IN '/home/'"
echo "DIRECTORY, FIRST ENTER '/home/SAMPLE.TXT' IN THE FIRST PROMPT, AND IN THE SECOND PROMPT"
echo "THE EXPRESSION TO BE MATCHED"
echo "#######################################################################################"
echo "======================================================================================="
echo "ENTER FILE WHERE YOU WANT TO FIND A REGULAR EXPRESSION, WE WILL LOOK FOR IT: "
read filepath
echo "---------------------------------------------------------------------------------------"
locate $filepath
echo "---------------------------------------------------------------------------------------"
echo "COPY AND PASTE THE FILE AND PATH, IF IT IS IN THE LIST ABOVE, OR ENTER EXACT FILE PATH:"
read enteragain
echo "---------------------------------------------------------------------------------------"
echo "ENTERED FILE TO MATCH AN EXPRESSION IS SHOWN: "
echo "---------------------------------------------------------------------------------------"
ls -l -h $enteragain
echo "======================================================================================="
echo "ENTER A REGULAR EXPRESSION TO FIND IN ABOVE FILE PATH: "
read expression
echo "======================================================================================="
clear
echo "ENTERED EXPRESSION IS: "
echo $expression
echo "---------------------------------------------------------------------------------------"
echo "FOUND EXPRESSION IN: "
ls -l -h $enteragain
echo "---------------------------------------------------------------------------------------"
sudo touch /home/$expression.txt
sudo grep -n $expression $enteragain | sudo tee -a /home/$expression.txt
echo "---------------------------------------------------------------------------------------"
sudo mv /home/$expression.txt /home/gus/regular-expressions/
echo "OUTPUT IS PLACED IN: "
echo "---------------------------------------------------------------------------------------"
ls -l -h /home/gus/regular-expressions/$expression.txt
echo "---------------------------------------------------------------------------------------"
echo "YOU CAN VIEW THE FILE VIA COMMAND LINE, ENTERING THE COMMAND BELOW: "
echo "cat /home/gus/regular-expressions/$expression.txt"
echo "---------------------------------------------------------------------------------------"

sudo touch eth0.txt
cat /dev/null | sudo tee eth0.txt
ifconfig eth0 | sudo > /dev/null tee eth0.txt
sleep 1
echo "YOU CAN VIEW THE FILE REMOTELY USING AN AVAILABLE IP ADDRESS BELOW:"
echo "---------------------------------------------------------------------------------------"
sudo grep -n "r:[^<>]*B" eth0.txt | >> /dev/null sudo tee eth0.txt
sed 's/......................//' eth0.txt | sudo >> /dev/null tee eth0.txt
sed -r 's/.{40}$//' eth0.txt | sudo >> /dev/null tee eth0.txt 
sleep 1
echo "ftp://$(cat eth0.txt)/regular-expressions/"$expression.txt | sudo >> /dev/null tee eth0.txt
sed 's/ //' eth0.txt

sudo touch wlan0.txt
cat /dev/null | sudo tee wlan0.txt
ifconfig wlan0 | sudo >> /dev/null tee wlan0.txt
sleep 1
sudo grep -n "r:[^<>]*B" wlan0.txt | >> /dev/null sudo tee wlan0.txt
sed 's/......................//' wlan0.txt | sudo >> /dev/null tee wlan0.txt
sed -r 's/.{40}$//' wlan0.txt | sudo >> /dev/null tee wlan0.txt 
sleep 1
echo "ftp://$(cat wlan0.txt)/regular-expressions/"$expression.txt | sudo >> /dev/null tee wlan0.txt
sed 's/ //' wlan0.txt



echo "---------------------------------------------------------------------------------------"
echo "YOU CAN VIEW THE FILE LOCALLY IN YOUR WEB BROWSER AND ACCESS: "
echo "ftp://127.0.0.1/regular-expressions/$expression.txt"
echo "......................................................................................."
echo "PASTE 'cat /home/gus/regular-expressions/$expression.txt' IF YOU WISH, OR JUST HIT ENTER: "
read enterexpected
cat /home/gus/regular-expressions/$expression.txt
echo "---------------------------------------------------------------------------------------"
echo "ABOVE IS THE OUTPUT OF THE FILE -"
echo "---------------------------------------------------------------------------------------"
echo "PROGRAM ENDED, HIT ENTER TO KILL PROGRAM NOW..."
read killprogram

done

