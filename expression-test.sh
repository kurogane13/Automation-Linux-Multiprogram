echo "ENTER A REGULAR EXPRESSION TO FIND IN ABOVE FILE PATH: "
read expression
echo "ENTERED EXPRESSION IS: "
echo $expression
echo "---------------------------------------------------------------------------------------"
echo "FOUND EXPRESSION IN: "
ls -l -h expression
echo "---------------------------------------------------------------------------------------"
sudo touch /home/$expression.txt
echo "---------------------------------------------------------------------------------------"
echo "OUTPUT IS PLACED IN: "
echo "---------------------------------------------------------------------------------------"
ls /home/$expression.txt
