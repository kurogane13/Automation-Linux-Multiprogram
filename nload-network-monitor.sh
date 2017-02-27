if which nload >/dev/null; then
    echo "-------------------------------------------------------------"
    gnome-terminal -e "nload -m wlan0 eth0"
    
else
    echo nload application is not installed in your system...
    echo "-------------------------------------------------------------"
    echo This application will be used to measure LAN bandwidth,
    echo "-------------------------------------------------------------"
    read -p "HIT ENTER TO INSTALL IT NOW, OR PRESS CTRL+C TO ABORT... " -n1 -s
    sudo apt-get install nload
    gnome-terminal -e "nload -m wlan0 eth0"
fi
