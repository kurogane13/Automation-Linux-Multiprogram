for SCRIPT in /home/cisco-ssh-access-scripts-logs/*
	do
		if [ -f $SCRIPT -a -x $SCRIPT ]
		then
			$SCRIPT
		fi
	done
