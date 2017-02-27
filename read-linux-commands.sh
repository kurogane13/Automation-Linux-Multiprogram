echo "Input command to run: "

read commands

for file in 1.sh ; do cp -r -pi /home/run-linux-commands.sh $commands ; done

sudo mv $commands $commands.sh

sed -i "s/\(^commands=\).*/\1$commands/" $INPUT /home/$commands.sh


