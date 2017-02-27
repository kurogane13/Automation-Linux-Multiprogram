for SCRIPT in /home/cisco-telnet-access-scripts-logs/*
	do
		if [ -f $SCRIPT -a -x $SCRIPT ]
		then
			$SCRIPT
		fi
	done
