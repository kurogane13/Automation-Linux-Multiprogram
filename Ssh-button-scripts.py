loop = 101
while(loop==101):
    
    import os
    os.system('clear')
    print("SSH SCRIPTS MODE ACCESSED")
    print("----------------------------------------------------------------------------------------------------------------")
    print("0 - TO RUN ONLY A SPECIFIC SCRIPT")
    print("1 - TO RUN MORE THAN 1 SCRIPT, OR MULTIPLE SCRIPTS (UP TO 10 SCRIPTS SUPPORTED) ")
    print("2 - TO RUN ALL SCRIPTS SAVED")
    print("----------------------------------------------------------------------------------------------------------------")
    print("CTRL+C - TO TERMINATE PROGRAM")
    print("----------------------------------------------------------------------------------------------------------------")
    runallsshscriptsornot=raw_input("SELECT A MODE, ENTER NUMBER AND HIT ENTER: ")
    sshrunspecific=("0")
    sshrunmorethanone=("1")
    sshrunallscripts=("2")
    if runallsshscriptsornot==sshrunspecific:
        loop = 102
        while(loop==102):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 0")
            print("----------------------------------------------------------------------------------------------------------------")
            print("LIST OF ALL SCRIPTS IN FOLDER:")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system("ls -f -l -s -h -t /home/cisco-ssh-access-scripts-logs | grep .sh")
            print("----------------------------------------------------------------------------------------------------------------")
            ssh_enternameofscript=raw_input("COPY AND PASTE, OR ENTER MANUALLY A SCRIPT TO BE EXECUTED: ")
            os.system('sudo bash /home/cisco-ssh-access-scripts-logs/'+ssh_enternameofscript)
            print("----------------------------------------------------------------------------------------------------------------")
            loop = 103
            while(loop==103):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO SSH SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                ssh_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                ssh_relaunch_yes=("0")
                ssh_get_back_to_menu_modes=("1")
                if ssh_relaunch_mode_or_not==ssh_relaunch_yes:
                    import os
                    os.system('clear')
                    loop = 102
                elif ssh_relaunch_mode_or_not==ssh_get_back_to_menu_modes:
                    import os
                    os.system('clear')
                    loop = 101
                else:
                    import os
                    os.system('clear')
                    print("PLEASE ENTER EITHER '0' OR '1'...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 103

    

    elif runallsshscriptsornot==sshrunmorethanone:
        loop = 104
        while(loop==104):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 1")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system('sudo bash /home/cisco-ssh-access-scripts-logs/ssh-scriptmultiple.sh')
            loop = 105
            while(loop==105):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO TELNET SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                ssh_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                ssh_relaunch_yes=("0")
                ssh_get_back_to_menu_modes=("1")
                if ssh_relaunch_mode_or_not==ssh_relaunch_yes:
                      import os
                      os.system('clear')
                      loop = 104
                elif ssh_relaunch_mode_or_not==ssh_get_back_to_menu_modes:
                      import os
                      os.system('clear')
                      loop = 101
                else:
                      import os
                      os.system('clear')
                      print("PLEASE ENTER EITHER '0' OR '1'...")
                      import time
                      time.sleep(2)
                      import os
                      os.system('clear')
                      loop = 105

    elif runallsshscriptsornot==sshrunallscripts:
        
        loop = 106
        while(loop==106):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 2")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system('sudo bash /home/runscripts-ssh-telnet-access-scripts-logs.sh')
            loop = 107
            while(loop==107):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO SSH SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                ssh_all_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                ssh_all_relaunch_yes=("0")
                ssh_all_get_back_to_menu_modes=("1")
                if ssh_all_relaunch_mode_or_not==ssh_all_relaunch_yes:
                    import os
                    os.system('clear')
                    loop = 106
                elif ssh_all_relaunch_mode_or_not==ssh_all_get_back_to_menu_modes:
                    import os
                    os.system('clear')
                    loop = 101
                else:
                    import os
                    os.system('clear')
                    print("PLEASE ENTER EITHER '0' OR '1'...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 107
            
        
