loop = 101
while(loop==101):
    
    import os
    os.system('clear')
    print("TELNET SCRIPTS MODE ACCESSED")
    print("----------------------------------------------------------------------------------------------------------------")
    print("0 - TO RUN ONLY A SPECIFIC SCRIPT")
    print("1 - TO RUN MORE THAN 1 SCRIPT, OR MULTIPLE SCRIPTS (UP TO 10 SCRIPTS SUPPORTED) ")
    print("2 - TO RUN ALL SCRIPTS SAVED")
    print("----------------------------------------------------------------------------------------------------------------")
    print("CTRL+C - TO TERMINATE PROGRAM")
    print("----------------------------------------------------------------------------------------------------------------")
    runalltelnetscriptsornot=raw_input("SELECT A MODE, ENTER NUMBER AND HIT ENTER: ")
    telnetrunspecific=("0")
    telnetrunmorethanone=("1")
    telnetrunallscripts=("2")
    if runalltelnetscriptsornot==telnetrunspecific:
        loop = 102
        while(loop==102):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 0")
            print("----------------------------------------------------------------------------------------------------------------")
            print("LIST OF ALL SCRIPTS IN FOLDER:")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system("ls -f -l -s -h -t /home/cisco-telnet-access-scripts-logs | grep .sh")
            print("----------------------------------------------------------------------------------------------------------------")
            telnet_enternameofscript=raw_input("COPY AND PASTE, OR ENTER MANUALLY A SCRIPT TO BE EXECUTED: ")
            os.system('sudo bash /home/cisco-telnet-access-scripts-logs/'+telnet_enternameofscript)
            print("----------------------------------------------------------------------------------------------------------------")
            loop = 103
            while(loop==103):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO TELNET SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'TELNET SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                telnet_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                telnet_relaunch_yes=("0")
                telnet_get_back_to_menu_modes=("1")
                if telnet_relaunch_mode_or_not==telnet_relaunch_yes:
                    import os
                    os.system('clear')
                    loop = 102
                elif telnet_get_back_to_menu_modes:
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

    

    elif runalltelnetscriptsornot==telnetrunmorethanone:
        loop = 104
        while(loop==104):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 1")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system('sudo bash /home/cisco-telnet-access-scripts-logs/telnet-scriptmultiple.sh')
            loop = 105
            while(loop==105):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO TELNET SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'TELNET SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                telnet_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1': ")
                telnet_relaunch_yes=("0")
                telnet_get_back_to_menu_modes=("1")
                if telnet_relaunch_mode_or_not==telnet_relaunch_yes:
                    import os
                    os.system('clear')
                    loop = 104
                elif telnet_relaunch_mode_or_not==telnet_get_back_to_menu_modes:
                    import os
                    os.system('clear')
                    loop = 101
                else:
                    import os
                    os.system('clear')
                    print("PLEASE ENTER EITHER '0' OR '1'... ")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 105

    elif runalltelnetscriptsornot==telnetrunallscripts:
        
        loop = 106
        while(loop==106):
            
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------------------------------------")
            print("YOU ARE IN MODE 2")
            print("----------------------------------------------------------------------------------------------------------------")
            os.system('sudo bash /home/runscripts-cisco-telnet-access-scripts-logs.sh')
            loop = 107
            while(loop==107):
                
                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO TELNET SCRIPTS MODES?")
                print("----------------------------------------------------------------------------------------------------------------")
                print("0 - TO RELAUNCH THIS MODE")
                print("1 - TO GET BACK TO MAIN MENU 'TELNET SCRIPTS MODE'")
                print("----------------------------------------------------------------------------------------------------------------")
                telnet_all_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                telnet_all_relaunch_yes=("0")
                telnet_all_get_back_to_menu_modes=("1")
                if telnet_all_relaunch_mode_or_not==telnet_all_relaunch_yes:
                    import os
                    os.system('clear')
                    loop = 106
                elif telnet_all_relaunch_mode_or_not==telnet_all_get_back_to_menu_modes:
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
            
        
