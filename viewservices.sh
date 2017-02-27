
echo "-------------------------------------------------------------------------------"
echo "YOU ARE ABOUT TO VIEW SERVICES STATUS, ONCE YOU ARE DONE VIEWING HIT CTRL+C,"
echo "TO RETURN TO MAIN MENU"
echo "-------------------------------------------------------------------------------"
sleep 6
sudo systemctl -r --type service --all
