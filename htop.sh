if which htop >/dev/null; then
    echo "-------------------------------------------------------------"
    gnome-terminal -e "htop"
    
else
    echo htop is not installed in your system...
    echo "-------------------------------------------------------------"
    echo Proceeding to install htop...
    echo "-------------------------------------------------------------"
    sudo apt-get install htop
    gnome-terminal -e "htop"
fi
