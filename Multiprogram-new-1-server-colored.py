import sys
from termcolor import colored

import os
os.system('clear')
green = colored("WELCOME TO LINUX MULTIPROGRAM!, SELECT AN OPERATION MODE AND HIT ENTER TO BEGIN: ", 'green', attrs=['bold'])
print green
print("====================================================================================")


loop = 0
while (loop==0):
    yellow = colored("ACCESS SYSTEM MODES AND CONTROL LINUX SYSTEM", 'yellow', attrs=['bold'])
    green = colored("YOU ARE IN MAIN MENU", 'green', attrs=['bold'])
    redshutres = colored("Mode 17 - SYSTEM REBOOT OR SHUTDOWN MENU - SHUTS DOWN OR RESTARTS SYSTEM", 'red', attrs=['bold'])
    bluenetwork = colored("NETWORK CONTROL MODE OPERATIONS", 'cyan', attrs=['bold'])
    mode0 = colored("Mode 0 - ACCESSES UNIT CONVERSION MODES - DECIMAL TO BINARY NUMBERS AND OTHERS", 'yellow')
    mode1 = colored("Mode 1 - INVOKE LINUX TERMINAL FROM THIS MODE", 'yellow')
    mode2 = colored("Mode 2 - MANAGE FILES AND FOLDERS ", 'yellow')
    mode3 = colored("Mode 3 - FIND REGULAR EXPRESSIONS IN FILES ", 'yellow')
    mode4 = colored("Mode 4 - COPY THIS ENTIRE PROGRAM AND FILES, TO A LOCAL DIRECTORY OR A REMOTE HOST VIA SCP", 'yellow')
    mode5 = colored("Mode 5 - TRANSFER FILES/FOLDERS TO A REMOTE HOST VIA SCP PROTOCOL", 'yellow')
    mode6 = colored("Mode 6 - GETS LINUX SYSTEM DETAILED REPORT", 'yellow')
    mode7 = colored("Mode 7 - DEBUGS USB PLUG AND PLAY DEVICES", 'yellow')
    mode8 = colored("Mode 8 - ACCESSES LINUX UPDATE MODES", 'yellow')
    mode9 = colored("Mode 9 - MONITORING MODES - VIEW PROCESSES, SERVICES STATUS AND LOGS", 'yellow')
    mode10 = colored("Mode 10 - RELOADS ALL NETWORK INTERFACES AND LOGS INFO TO A FILE", 'cyan')
    mode11 = colored("Mode 11 - DISPLAYS DETAILED IP NETWORK AND HARDWARE INFO, AND LOGS OUTPUT TO A FILE", 'cyan')
    mode12 = colored("Mode 12 - SCANS YOUR LAN WITH NMAP TOOL", 'cyan')
    mode13 = colored("Mode 13 - MONITORS LAN NETWORK BANDWIDTH", 'cyan')
    mode14 = colored("Mode 14 - CREATE AUTOMATION SCRIPTS TO GET CISCO ROUTERS RUNNING CONFIG AND/OR CHECK NETWORK STATUS", 'cyan')
    mode15 = colored("Mode 15 - RUN SCRIPTS CREATED IN PREVIOUS MODE, OR PLACED IN TELNET OR SSH DIRECTORIES", 'cyan')
    mode16 = colored("Mode 16 - ACCESSES A CISCO LAB DEVICE ROUTER/L3 DEVICE TO OBTAIN ACTUAL NETWORK STATUS", 'cyan')
    print green
    print("====================================================================================")
    print("'l' - TO START LOGGING ALL CURRENT INPUT AND OUTPUT FROM TERMINAL - ")
    print("------------------------------------------------------------------------------------")
    print yellow
    print("------------------------------------------------------------------------------------")
    print mode0
    print mode1
    print mode2
    print mode3
    print mode4
    print mode5
    print mode6
    print mode7
    print mode8
    print mode9
    print("------------------------------------------------------------------------------------")
    print bluenetwork
    print("------------------------------------------------------------------------------------")
    print mode10
    print mode11
    print mode12
    print mode13
    print mode14
    print mode15
    print mode16
    print("------------------------------------------------------------------------------------")
    print redshutres		
    print("------------------------------------------------------------------------------------")
    print("'s' - TO SWITCH THIS PROGRAM TO BLACK AND WHITE MODE - ")
    print("------------------------------------------------------------------------------------")
    print("TO EXIT THIS PROGRAM JUST TYPE: exit, AND HIT ENTER")
    print("####################################################################################")
    inputdatamainprompt = colored("Enter  operation mode (example: for mode 0, type 0) and hit enter -", 'green', 'on_red', attrs=['reverse', 'blink'])
    print  inputdatamainprompt
    greenline = colored("------------------------------------------------------------------------------------", 'green', attrs=['bold'])
    print greenline
    modeselection=raw_input("Waiting for user input... ")
    loggingmode=("l")

    conversionmode=("0")
    runlinuxcommands=("1")
    filesandfolders=("2")
    regularexpression=("3")
    copyprogramlocalorremote=("4")
    transferviascp=("5")
    linuxsysteminfo=("6")
    debugsusbplugandplay=("7")
    updatemodes=("8")
    monitoringmodes=("9")
    
    
    reloadnetworkints=("10")
    currentipconfig=("11")
    scansyourlan=("12")
    monitornetwork=("13")
    createciscorouterscripts=("14")
    runscripts=("15")
    accessciscodevicelab=("16")
    
    rebootorshutdown=("17")
    
    backtomenu0=("m")
    backtomainmenu=("m")
    backtomenu1=("m")
    exitprogram=("exit"or"EXIT")
    switch_to_black_white_terminal=("s")

    if modeselection==conversionmode:

        loop = 16
        while (loop==16):

                import os
                os.system('clear')
                greenconversionmodes = colored("YOU ARE IN UNIT CONVERSION MODE", 'yellow', attrs=['bold'])
                print("#####################################")
                print greenconversionmodes
                print("#####################################")
                import time
                time.sleep(1)
                print("Mode 0 - BINARY TO DECIMAL MODE")
                print("Mode 1 - DECIMAL TO BINARY MODE")
                print("Mode 2 - HEXADECIMAL TO DECIMAL MODE")
                print("Mode 3 - DECIMAL TO HEXADECIMAL MODE")
                print("-------------------------------------")
                print("b - WHEN INSIDE A MODE, gets you back to this menu")
                print("m - to return to MAIN MENU ONLY")
                print("#####################################")
                modeselectionunits=raw_input("Please select unit conversion mode from menu ( 0 - 1 - 2 - 3 )...")
                
                binarymode=("0")
                decimalmode=("1")
                hexadecimalmode=("2")
                decimaltohex=("3")
                backtomenu2="b"
                backtomenu0=("m")
                anyofthese=("0"or"1"or"2"or"3"or"b"or"m")

                if modeselectionunits==backtomainmenu:
                    print("------------------------------")
                    print("RETURNING TO MAIN MENU...")
                    print("------------------------------")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                elif modeselectionunits==backtomenu1:
                    print("-------------------------------")
                    print("YOU ALREADY ARE IN THIS MENU!..")
                    print("-------------------------------")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 16

                elif modeselectionunits==hexadecimalmode:
                    loop = 3
                    while (loop==3):

                        try:
                            print("Mode 2 - HEXADECIMAL TO DECIMAL CONVERSION was selected" )
                            print("-------------------------------------------------------------")
                            number=raw_input("Enter a Hexadecimal number: ")
                            i = int(number,16)

                            number=int()
                            number=("a")or("b")or("c")or("d")or("e")or("f")
                        

                            print("-------------------------------------------------------------")
                            print("The decimal representation of hexadecimal is:" , i)
                            print("-------------------------------------------------------------")
                
                            print("Want to switch modes?, if so hit ( b ) and press enter")
                            print("--------------------------------------------------------------------------------------------")
                            returntomenu=raw_input("To return to main menu hit ( m ) and enter, or just enter to stay in current mode")

                            if returntomenu==backtomenu2:
                                print("RETURNING TO UNIT CONVERSION MENU...")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 16
                                

                            elif returntomenu==backtomainmenu:
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 0

                            else:
                                loop = 3

                        except ValueError:

                            print("NO HEXADECIMAL VALUE ENTERED!")
                            print("-------------------------------")
                            import os
                            os.system('clear')

                            loop = 3



                elif modeselectionunits==decimaltohex:
                    loop = 4
                    while (loop==4):

                        try:
                            print("Mode 3 - DECIMAL TO HEXADECIMAL CONVERSION was selected" )
                            print("-------------------------------------------------------------")
                            dec = int(raw_input("Enter a Decimal number: "))
                            
                            print(hex(dec),"is the representation of ", dec)
                        
                            print("-------------------------------------------------------------")
                    
                            print("Want to switch modes?, if so hit ( b ) and press enter")
                            print("--------------------------------------------------------------------------------------------")
                            returntomenu=raw_input("To return to main menu hit ( m ) and enter, or just enter to stay in current mode")

                            if returntomenu==backtomenu2:
                                print("RETURNING TO UNIT CONVERSION MENU...")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 16

                            elif returntomenu==backtomainmenu:
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 0

                            else:
                                loop = 4

                        except ValueError:

                            print("NO DECIMAL VALUE ENTERED!")
                            print("-------------------------------")
                            import os
                            os.system('clear')

                            loop = 4


                elif modeselectionunits==decimalmode:

                        loop = 2
                        while (loop==2):
                            print("Mode 1 - DECIMAL TO BINARY CONVERSION was selected")
                            print("--------------------------------------------------")

                            def binary(n):
                                if n > 1:
                                    binary(n//2)
                                print n%2,

                            dec=int()
                            dec=()

                                
                            try:

                                dec=int(raw_input("Enter a random number ( ONLY AN INTEGER ) to be converted to binary: "))

                                if dec==backtomenu2:
                                    print("RETURNING TO UNIT CONVERSION MENU...")
                                    print("-----------------------------------------------------")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 16

                                if dec==backtomainmenu:
                                    print("RETURNING TO MAIN MENU...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 0

                                    
                            except ValueError:

                                print("---------------------------------------------------------------------------------------")
                                print("NO NUMBER WAS ENTERED!, INPUT HAS NOT REGISTERED A NUMBER, ONLY INTEGERS ARE ALLOWED:...")
                                print("---------------------------------------------------------------------------------------")
                                import os
                                os.system('clear')
                                loop = 2        

            
                                    
                            else:

                                print"The binary representation of  ",dec, " is " ,
                                binary(dec)
                                print"-----------------------------------------------------------------------"
                                print("Want to switch modes?, if so hit ( b ) and press enter")
                                print("--------------------------------------------------------------------------------------------")
                                returntomenu=raw_input("To return to main menu hit ( m ) and enter, or just enter to stay in current mode: ")

                                if returntomenu==backtomenu2:
                                    print("RETURNING TO UNIT CONVERSION MENU...")
                                    print("-------------------------------------------------------------")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 16

                                elif returntomenu==backtomainmenu:
                                    print("RETURNING TO MAIN MENU...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    
                                    loop = 0

                                else:

                                    loop = 2

                            


                elif modeselectionunits==binarymode:
                    loop = 1
                    while (loop==1):

                        print("Mode 0 - BINARY TO DECIMAL CONVERSION was selected")

                        print("--------------------------------------------------")

                        binary=raw_input("Enter Binary number ( only 0 or 1 ) to convert in Decimal: ")


                        try:
                                

                            if binary==backtomainmenu:
                                print("-----------------------------------")
                                print("RETURNING TO MAIN MENU...")
                                print("-----------------------------------")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 0

                            if binary==backtomenu2:
                                print("-----------------------------------")
                                print("RETURNING TO UNITCONVERSION MENU...")
                                print("-----------------------------------")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 16
                            
                            is_bin = int(binary,2)
                            is_bin = True
                            print("---------------------------------------------------------------------")
                            print("BINARY NUMBER ENTERED IS " + binary)
                            print("---------------------------------------------------------------------")
                            print"The Decimal Representation of ", binary, " is " , int(binary, 2)

                            print"-----------------------------------------------------------------------"

                            print("Want to switch modes?, if so hit ( b ) and press enter")
                            print("--------------------------------------------------------------------------------------------")
                            returntomenu=raw_input("To return to main menu hit ( m ) and enter, or just enter to stay in current mode")

                            if returntomenu==backtomenu2:
                                print("RETURNING TO UNIT CONVERSION MENU...")
                                print("-----------------------------------------------------")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 16

                            if returntomenu==backtomainmenu:
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(2)
                                import os
                                os.system('clear')
                                loop = 0

                            if returntomenu==binarymode:
                                loop = 1
                                

                        except ValueError:
                            is_bin = False
                            print("-----------------------------------------------------")
                            print "THIS IS NOT A BINARY NUMBER!"
                            print("-----------------------------------------------------")
                            import os
                            os.system('clear')
                            loop = 1
                            
                else:
                    import os
                    os.system('clear')
                    print("PLEASE ENTER ONLY VALID OPTIONS FROM THE MENU!")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 16



            
    
    elif modeselection==linuxsysteminfo:
        loop = 23
        while (loop==23):

            import os
            os.system('clear')
            linuxsysteminfomodes = colored("YOU HAVE ACCESSED LINUX SYSTEMINFO MODES...", 'yellow', attrs=['bold'])
            print linuxsysteminfomodes
            print("---------------------------------------------------------")
            print(" 0 - to provide an lshw detailed report in HTML format")
            print(" 1 - to provide a detailed txt report")
            print(" m - to get back to main menu")
            import time
            time.sleep(2)
            htmldetailedreport=("0")
            txtdetailedreport=("1")
            returntomainmenu=("m")
            print("-----------------------------------------------------------------")
            reportchosen=raw_input("PLEASE SELECT EITHER 0, 1 OR (m): ")
            try:
                if reportchosen==htmldetailedreport:
                    loop = 28
                    while (loop==28):
                        
                        import os
                        os.system('clear')
                        import time
                        time.sleep(1)
                        print(" 1 - To open with Ubuntu linux default browser MOZILLA FIREFOX")
                        print("--------------------------------------------------------------")
                        print(" m - to get back to main menu")
                        mozillafirefox=("1")
                        returntomainmenu=("m")
                        import time
                        time.sleep(1)
                        print("-----------------------------------------------------------")
                        selectbrowser=raw_input("WAITING FOR INPUT... ")
                        try:


                            if selectbrowser==mozillafirefox:

                                print("------------------------------------------")
                                import time
                                time.sleep(2)  
                                import os
                                os.system('sudo bash /home/htmlsysteminfofirefox.sh')
                                loop = 0


                            if selectbrowser==returntomainmenu:
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                loop = 0

                        except valuerror:
                            import os
                            os.system('clear')
                            print("PLEASE ONLY ENTER EITHER, 1, 2 OR 3...")
                            import time
                            time.sleep(2)
                            loop = 28
                            

                if reportchosen==txtdetailedreport:
                    import os
                    os.system('clear')
                    print("------------------------------------------")
                    import time
                    time.sleep(2)  
                    import os
                    os.system('sudo bash /home/systeminfo.sh')
                    loop = 0

                if reportchosen==returntomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                

            except Valuerror:
                
                print("ONLY 0 OR 1 IS ALLOWED!")
                import os
                os.system('clear')
                loop = 23
                    
                
                    
                    
                
    elif modeselection==regularexpression:
        import os
        os.system('clear')
        regularexpmode= colored("REGULAR EXPRESSION MODE ACCESSED - ", 'yellow', attrs=['bold'])
        print regularexpmode
        os.system('sudo bash /home/regular-expression-lookup.sh')
        os.system('clear')
        loop = 0
        
    elif modeselection==currentipconfig:
        import os
        os.system('clear')
        loop = 27
        while (loop==27):
            import os
            os.system('clear')
            import time
            time.sleep(1)
            ipconfigurationmode = colored("IPCONFIUGRATION REPORT MODE ACCESSED - ", 'cyan', attrs=['bold'])
            print ipconfigurationmode
            print("----------------------------------------------------------------------------------")
            print(" y - PROCEEDS WITH IPCONFIGURATION REPORT")
            print(" n - RETURNS TO MAIN MENU")
            print("----------------------------------------------------------------------------------")
            proceedwithipconfig=("y")
            returntomainmenu=("n")
            enter=(" ")
            selectchoice=raw_input("PROCEED WITH IPCONFIGURATION REPORT?.....y/n: ")
            try:
                if selectchoice==proceedwithipconfig:
                    
                    print("----------------------------------------------------------------------------------")
                    import os
                    os.system('clear')
                    import os
                    os.system('sudo touch /home/ipconfiguration.txt')
                    print("DISPLAYING DETAILED IP CONFIGURATION AND NETOWRK INFORMATION...")
                    print("------------------------------------------------------")
                    import time
                    time.sleep(2)
                    import os
                    os.system('ifconfig -a')
                    print("------------------------------------------------------")
                    import os
                    os.system('date | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"') 
                    os.system('ifconfig -a | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"')
                    os.system('ip link show | sudo tee -a /home/ipconfiguration.txt')    
                    os.system('echo "----------------------------------------------------------------"')
                    os.system('arp -a | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"')
                    os.system('ip route | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"')
                    os.system('nmcli connection show | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"')
                    print("DISPLAYING NETWORK MANAGER DEVICE INFORMATION: ")
                    os.system('echo "----------------------------------------------------------------"')
                    os.system('nmcli device show | sudo tee -a /home/ipconfiguration.txt')
                    os.system('echo "----------------------------------------------------------------"')
		    print("ipconfiguration.txt was created.")
                    print("--------------------------------------------------------------------------------------------")
                    import time
                    time.sleep(1)
                    print("The file is located at /home/ directory")
                    print("--------------------------------------------------------------------------------------------")
                    import time
                    time.sleep(1)
                    os.system('ls -a -l -t -h /home/ipconfiguration.txt')
                    print("--------------------------------------------------------------------------------------------")
                    print("YOU CAN VIEW THE OUTPUT SAVED IN THIS FILE LATER, BY ENTERING THE COMMAND BELOW: ")
		    import os
                    os.system ('echo "cat /home/ipconfiguration.txt"')
                    print("-------------------------------------------------------------------------------------")
                    raw_input("HIT ENTER TO RETURN TO MAIN MENU..")
                    import os
                    os.system('clear')
                    loop = 0

                elif selectchoice==returntomainmenu:
                    import os
                    os.system('clear')
                    loop = 0                    

                

            except Valuerror:
                print("ONLY (y) OR (n) IS ALLOWED...")
                import time
                time.sleep(2)
                loop = 27
                

    elif modeselection==updatemodes:
        loop = 22
        while (loop==22):
            import os
            os.system('clear')
            linuxupdates = colored("LINUX UPDATE MODE ACCESSED -", 'yellow', attrs=['bold'])
            print linuxupdates
            print("--------------------------------------------------------------------")
            print("Mode 0 - Updates system directly")
            print("Mode 1 - Lists all updates to be installed")
            print("--------------------------------------------------------------------")
            print("m - RETURNS TO MAIN MENU")
            updatedirectly=("0")
            listallpackages=("1")
            backtomainmenu=("m")
            import time
            time.sleep(1)
            print("--------------------------------------------------------------------")
            try:
                selectmode=raw_input("Enter operation mode ( 0 or 1 ) and hit enter...")
                if selectmode==updatedirectly:
                    import os
                    os.system('clear')
                    import os
                    os.system('sudo apt-get update')
                    import time
                    time.sleep(2)
                    print("------------------------------------------------")
                    print("Update script executed, returning to main menu...")
                    loop = 0
                    
                elif selectmode==listallpackages:
                    import os
                    os.system('clear')
                    os.system('touch allpackages.txt')
                    print("LISTING ALL PROGRAM APPLICATION PACKAGES IN YOUR SYSTEM...")
                    print("-------------------------------------------------------------------------------------")
                    import time
                    time.sleep(2)
                    print("THIS LIST WILL BE SAVED IN THE USER DIRECTORY AFTER OUTPUT IS COMPLETED...")
                    import time
                    time.sleep(3)
                    import os
                    os.system('dpkg -l')
                    os.system('dpkg -l | tee -a $HOME/allpackages.txt')
                    print("------------------------------------------------------------")
                    import time
                    time.sleep(2)
                    raw_input("HIT ENTER ONCE YOU ARE DONE VIEWING OUTPUT...")
                    import os
                    os.system('clear')
                    print("OUTPUT FROM PREVIOUS SCREEN WAS SAVED IN allpackages.txt")
                    print("located in the user directory")
                    print("------------------------------------------------------------")
                    import time
                    time.sleep(3)
                    import os
                    os.system('cd')
                    import os
                    os.system('pwd')
                    print("------------------------------------------------------------")
                    print("PROVIDE THE ROOT PASSWORD TO VIEW FILE IN DIRECTORY...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('sudo ls -l -r -a -h | grep allpackages.txt')
                    import time
                    time.sleep(3)
                    print("------------------------------------------------------------")
                    raw_input("HIT ENTER TO RETURN TO MAIN MENU...")
                    import os
                    os.system('clear')
                    
                    loop = 0

                elif selectmode==backtomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0
                    

                

            except Valuerror:
                print("Please a valid option from the menu...")
                loop = 22


    elif modeselection==monitoringmodes:
        loop = 30
        while (loop==30):
            import time
            time.sleep(1)
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------")
            monitoringmodesyellow = colored("MONITORING MODES ACCESSED - ", 'yellow', attrs=['bold'])
            print monitoringmodesyellow
            print("----------------------------------------------------------------------------------")
            print("Mode 0 - MONITOR YOUR LINUX PROCESSES WITH HTOP")
            print("Mode 1 - CHECK SERVICES ACTUAL STATUS")
            print("Mode 2 - VIEW LINUX SYSTEM LOGS")
            print("----------------------------------------------------------------------------------")
            print("m - RETURNS BACK TO MAIN MENU")
            print("----------------------------------------------------------------------------------")
            selectoption=raw_input("SELECT DESIRED MODE AND HIT ENTER: ")
            htop=("0")
            services=("1")
            logs=("2")
            if selectoption==htop:

                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("HTOP MONITORING MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/htop.sh')
            
                loop = 30

            elif selectoption==services:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("SERVICES STATUS MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/viewservices.sh')

                loop = 30

            elif selectoption==logs:
                loop = 31
                while (loop==31):
                    
                    import time
                    time.sleep(1)
                    import os
                    os.system('clear')
                    print("----------------------------------------------------------------------------")
                    print("LINUX LOGS MODE ACCESSED...")
                    print("----------------------------------------------------------------------------")
                    print("MODE 0 - read alternatives.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 1 - read auth.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 2 - read boot.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 3 - read bootstrap.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 4 - read btmp")
                    print("----------------------------------------------------------------------------")
                    print("MODE 5 - read dmesg")
                    print("----------------------------------------------------------------------------")
                    print("MODE 6 - read dpkg.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 7 - read faillog")
                    print("----------------------------------------------------------------------------")
                    print("MODE 8 - read kern.log")
                    print("----------------------------------------------------------------------------")
                    print("MODE 9 - read last")
                    print("----------------------------------------------------------------------------")
                    print("MODE 10 - read preload")
                    print("----------------------------------------------------------------------------")
                    print("MODE 11 - read syslog")      
                    print("----------------------------------------------------------------------------")
                    print("MODE 12 - read wtmp")
                    print("----------------------------------------------------------------------------")
                    print("p - RETURNS TO PREVIOUS MENU")
                    print("m - RETURNS BACK TO MAIN MENU")
                    print("----------------------------------------------------------------------------")
                    selectlog=raw_input("SELECT MODE AND HIT ENTER: ")
                    alternative=("0")
                    auth=("1")
                    boot=("2")
                    bootstrap=("3")
                    btmp=("4")
                    dmesg=("5")
                    dpkg=("6")
                    faillog=("7")
                    kernlog=("8")
                    last=("9")
                    preload=("10")
                    syslog=("11")
                    wtmp=("12")
                    previousmenu=("p")


                    if selectlog==alternative:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/alternatives.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31
                          

                    elif selectlog==auth:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/auth.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31


                    elif selectlog==boot:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/boot.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==bootstrap:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/bootstrap.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==btmp:

                          import os
                          os.system('clear')
                          os.system('sudo last -f /var/log/btmp')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==dmesg:

                          import os
                          os.system('clear')
                          os.system('dmesg')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==dpkg:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/dpkg.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31


                    elif selectlog==faillog:

                          import os
                          os.system('clear')
                          os.system('faillog -a')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==kernlog:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/kern.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==last:

                          import os
                          os.system('clear')
                          os.system('last')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==preload:

                          import os
                          os.system('clear')
                          os.system('sudo cat /var/log/preload.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==syslog:

                          import os
                          os.system('clear')
                          os.system('cat /var/log/alternatives.log')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31

                    elif selectlog==wtmp:

                          import os
                          os.system('clear')
                          os.system('last -f /var/log/wtmp')
                          print("-----------------------------------------------------------------------")
                          raw_input("HIT ENTER TO GET BACK TO MAIN MENU...")
                          loop = 31
                          
                    elif selectlog==previousmenu:

                          print("RETURNING TO PREVIOUS MENU...")
                          import time
                          time.sleep(2)
                          import os
                          os.system('clear')
                          loop = 30

                    elif selectlog==backtomainmenu:

                          print("RETURNING TO MAIN MENU...")
                          import time
                          time.sleep(2)
                          import os
                          os.system('clear')
                          loop = 0

            elif selectoption==backtomainmenu:
            
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(2)
                import os
                os.system('clear')
                loop = 0

        
        
    elif modeselection==reloadnetworkints:
        loop = 23
        while (loop==23):
            
            proceedwithreload=("y")
            backtomenu=("m")
            import os
            os.system('clear')
            reloadints = colored("RELOAD NETWORK INTERFACES MODE ACCESSED - ", 'cyan', attrs=['bold'])
            print reloadints 
            print("-------------------------------------------------------------------")
            print("y - PROCEEDS WITH NETWORK INTERFACES RELOAD")
            print("m - GETS YOU BACK TO MAIN MENU")
            print("-------------------------------------------------------------------")
            selectchoice=raw_input("ENTER (y) TO PROCEED or (m) TO GET BACK TO MENU...")
            try:
                if selectchoice==proceedwithreload:
                    import os
                    os.system('clear')
                    print("ALL NETWORK INTERFACES WILL BE RELOADED..")
                    import time
                    time.sleep(2)  
                    import os
                    os.system('sudo bash /home/networkreload.sh')
                    loop = 0

                elif selectchoice==backtomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                else:
                    import os
                    os.system('clear')
                    print("PLEASE SELECT EITHER (y) OR (m) ONLY")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 23

            except Valuerror:
                import os
                os.system('clear')
                print("PLEASE SELECT EITHER (y) OR (m) ONLY")
                import time
                time.sleep(2)
                import os
                os.system('clear')
                loop = 23


    elif modeselection==rebootorshutdown:

        loop = 21
        while (loop==21):

            import os
            os.system('clear')
            shutdown_restartmodes= colored("SHUTDOWN OR RESTART MODES ACCESSED", 'yellow', attrs=['reverse', 'bold'])
            shutdown_restartmodes= colored("SHUTDOWN OR RESTART MODES ACCESSED", 'yellow', 'on_red')
            print shutdown_restartmodes
            print("---------------------------------------------------------")
            print(" 0 - to shutdown system now")
            print(" 1 - to restart system now")
            print("-------------------------------------------------------------------")
            print("m - GETS YOU BACK TO MAIN MENU")
            import time
            time.sleep(2)
            shutdownnow=("0")
            restartnow=("1")
            returntomainmenu=("m")
            print("-----------------------------------------------------------------")
            systemshutorreboot=raw_input("PLEASE SELECT EITHER 0 OR 1...")
            try:
                if systemshutorreboot==shutdownnow:

                    import os
                    os.system('sudo shutdown now')
                    print("Shutting down system...")


                if systemshutorreboot==restartnow:

                    import os
                    os.system('sudo shutdown -r now')
                    print("Restarting system...")

                if systemshutorreboot==returntomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0
               
            except Valuerror:
                
                print("ONLY 0, 1 or m IS ALLOWED!")
                import os
                os.system('clear')
                loop = 21


    elif modeselection==debugsusbplugandplay:
        loop = 24
        while (loop==24):
            import os
            os.system('clear')
            debugusbplugandplay = colored("DEBUG USB PLUG AND PLAY MODE ACCESSED - ", 'yellow', attrs=['bold'])
	    print debugusbplugandplay
            import time
            time.sleep(1)
            print("---------------------------------------------------------")
            print("y - TO RUN DEBUG NOW")
            print("m - TO GET BACK TO MAIN MENU")
            print("---------------------------------------------------------")
            import time
            time.sleep(1)
            selectchoice=raw_input("SELECT (y) OR (m), WAITING FOR INPUT..")
            proceedwithdebug=("y")
            returnstomainmenu=("m")
            try:
                if selectchoice==proceedwithdebug:
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    print("INITIATING THE PLUG AND PLAY DEBUGGING TEST...")
                    print("----------------------------------------------")
                    import time
                    time.sleep(3)
                    print("WAIT UNTIL THE CURSOR BLINKS UNDER the kernel uevent")
                    print("AND THEN CONNECT YOUR USB DEVICE TO THE USB PORT FOR DEBUGGING")
                    print("--------------------------------------------------------------")
                    import time
                    time.sleep(4)
                    print("ONCE YOU ARE DONE AND HAVE SAFELY REMOVED YOUR DEVICE")
                    print("PRESS Ctrl+c KEYS AND HIT ENTER TO RETURN TO MAIN MENU...")
                    import time
                    time.sleep(4)
                    import os
                    os.system('udevadm monitor')
                    import time
                    time.sleep(2)
                    print("------------------------------------------------------")
                    print("DEBUGGING TEST HAS FINISHED, RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                if selectchoice==returnstomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                

            except Valuerror:
                print("ONLY y, or m IS ALLOWED!")
                import os
                os.system('clear')
                loop = 24
              
             
                                   
    elif modeselection==exitprogram:
        import os
        os.system('clear')
        import time
        time.sleep(1)
        exitprogram=("y")
        donotexit=("n")
        exitingprogram = colored("YOU ARE ABOUT TO EXIT THE PROGRAM", 'red', attrs=['reverse', 'blink'])
        exitingprogram = colored("YOU ARE ABOUT TO EXIT THE PROGRAM", 'red', 'on_yellow')
        print exitingprogram
        import time
        time.sleep(1)
        loop = 25
        while (loop==25):
            
            print("------------------------------------------")
            print("y - TO EXIT NOW")
            print("n - TO ABORT EXIT, AND RETURN TO MAIN MENU")
            print("------------------------------------------")
            selectchoice=raw_input("DO YOU WANT TO EXIT?.....y/n: ")
            exitnow=("y")
            donotexit=("n")
            try:
                if selectchoice==exitnow:
                    
                    print("Exiting program...")
                    import time
                    time.sleep(2)
                    break

                if selectchoice==donotexit:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                else:
                    import os
                    os.system('clear')
                    print("PLEASE SELECT ONLY (y) OR (n)")
                    import time
                    time.sleep(2)
                    loop = 25

            except Valuerror:
                import os
                os.system('clear')
                print("PLEASE SELECT ONLY (y) OR (n)")
                import os
                os.system('clear')
                import time
                time.sleep(2)
                loop = 25
                
    elif modeselection==scansyourlan:

        
        import os
        os.system('clear')
        nmapsweep = colored("NMAP SCAN LAN MODE ACCESSED - ", 'cyan', attrs=['bold'])
        print nmapsweep
        os.system('sudo bash /home/nmap-check.sh')
        os.system('clear')
        print("--------------------------------------------------------")
        print("APPLICATION TERMINATED, RETURNING TO MAIN MENU...")
        import time
        time.sleep(1)
        import os
        os.system('clear')
        loop = 0

    elif modeselection==switch_to_black_white_terminal:
        loop = 124
        while (loop==124):
            import os
            os.system('clear')
            os.system('python /home/Multiprogram-new-1-server.py')
            break
        
    elif modeselection==monitornetwork:
        import os
        os.system('clear')
        nloadmonitor = colored("NLOAD NETOWRK BANDWIDTH MODE ACCESSED -", 'cyan', attrs=['bold'])
        print nloadmonitor
        loop = 123
        while (loop==123):        
	    print("=====================================================")
            print("'1' - TO START SCRIPT ")
            print("'CTRL+C' - TO ABORT PROGRAM WHEN RUNNING")
            print("'ENTER' - TO GET BACK TO MAIN MENU FROM HERE")
            print("=====================================================")
            proceednloadornot= raw_input("WAITING FOR USER INPUT...")
            runnloadscript=("1")
            returntomainmenufromnload=("0")
	    if proceednloadornot==runnloadscript:
	       os.system('sudo bash /home/nload-network-monitor.sh')
	       loop = 123
            elif returntomainmenufromnload:
	       import os
 	       os.system('clear')
               print("RETURNING TO MAIN MENU...")
               import time
               time.sleep(2)
               os.system('clear')
       	       loop = 0
            
        
    elif modeselection==accessciscodevicelab:
        loop = 29
        while (loop==29):
            import time
            time.sleep(1)
            import os
            os.system('clear')
            ciscolabmode = colored("CISCO LAB DEVICE ACCESS MODE ENTERED...", 'cyan', attrs=['bold'])
            print("----------------------------------------------------------------------------------")
            print ciscolabmode
            print("----------------------------------------------------------------------------------")
            print("Mode 0 - TELNET - OBTAIN NETWORK STATUS REPORT FROM CISCO LAB ROUTER")
            print("Mode 1 - SSH - OBTAIN NETWORK STATUS REPORT FROM CISCO LAB ROUTER")
            print("----------------------------------------------------------------------------------")
            print("Mode 2 - TELNET - RETRIEVE RUNNING CONFIG FROM CISCO LAB ROUTER TO TXT FILE")
            print("Mode 3 - SSH - RETRIEVE RUNNING CONFIG FROM CISCO LAB ROUTER TO TXT FILE")
            print("----------------------------------------------------------------------------------")
            print("Mode 4 - INSTALL GNS3 NETWORK EMULATOR")
            print("----------------------------------------------------------------------------------")
            print("Mode 5 - CREATE BRIDGE AND TAP INTERFACES FOR ETH0")
            print("Mode 6 - DELETE BRIDGE AND TAP INTERFACES FOR ETH0")
            print("----------------------------------------------------------------------------------")
            print("Mode 7 - CREATE BRIDGE AND TAP INTERFACES FOR WLAN0")
            print("Mode 8 - DELETE BRIDGE AND TAP INTERFACES FOR WLAN0")
            print("----------------------------------------------------------------------------------")
            print("m - RETURNS BACK TO MAIN MENU")
            print("----------------------------------------------------------------------------------")
            selectoption=raw_input("SELECT DESIRED MODE AND HIT ENTER: ")
            telnet=("0")
            ssh=("1")
            telnet_running_config=("2")
            ssh_running_config=("3")
            gns3=("4")
            create=("5")
            delete=("6")
            createwireless=("7")
            deletewireless=("8")
            if selectoption==telnet:

                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("TELNET MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(2)
                os.system('sudo bash /home/telnet-Tkinter-check-router-network-status.sh')
            
                loop = 29

            elif selectoption==ssh:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("SSH MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/ssh-Tkinter-check-router-network-status.sh')

                loop = 29

            elif selectoption==telnet_running_config:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("TELNET RUNNING CONFIG MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/telnet-Tkinter-retrieve-running-config.sh')

                loop = 29

            elif selectoption==ssh_running_config:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("SSH RUNNING CONFIG MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/ssh-Tkinter-retrieve-running-config.sh')

                loop = 29



            elif selectoption==create:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("CREATE BRIDGE AND TAP INTERFACES FOR ETH0 MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/create-bridge-interfaces.sh')

                loop = 29

            elif selectoption==delete:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("DELETE BRIDGE AND TAP INTERFACES FOR ETH0 MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/delete-bridge-interfaces.sh')

                loop = 29

            elif selectoption==createwireless:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("CREATE BRIDGE AND TAP INTERFACES FOR WLAN0 MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/create-bridge-interfaces-wireless.sh')

                loop = 29

            elif selectoption==deletewireless:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("DELETE BRIDGE AND TAP INTERFACES FOR WLAN0 MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/delete-bridge-interfaces-wireless.sh')

                loop = 29

            elif selectoption==gns3:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("INSTALLING GNS3 NETWORK EMULATOR FOR LINUX...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo add-apt-repository ppa:gns3/ppa')
                os.system('sudo apt-get update')
                os.system('sudo apt-get install gns3-gui')
                os.system('clear')
                print("------------------------------------------------------------------------------------")
                raw_input("GNS3 NETWORK EMULATOR WAS SUCCESSFULLY INSTALLED, HIT ENTER TO RETURN TO MENU...")
                

                loop = 29

            elif selectoption==backtomainmenu:
                
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(2)
                import os
                os.system('clear')
                loop = 0

    elif modeselection==transferviascp:
        
        loop = 60
        while (loop==60):
            
            import os
            os.system('clear')
            scptransferremote = colored("SCP TRANSFER MODE ACCESSED", 'yellow', attrs=['bold'])
            print("##################################################################################################################")
            print scptransferremote
            print("##################################################################################################################")
            print("THIS PROGRAM TRANSFERS FILES AND/OR FOLDERS TO A REMOTE HOST VIA SCP PROTOCOL")
            print("------------------------------------------------------------------------------------------------------------------")
            userentry=raw_input("ENTER '1' TO START PROGRAM, OR '0' TO RETURN TO MAIN MENU...")
            returntomain=("0")
            startprogram=("1")
            if userentry==returntomain:
                
                import os
                os.system('clear')
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(1)
                loop = 0
                
            elif userentry==startprogram:
        
                print("------------------------------------------------------------------------------------------------------------------")
                import os
                os.system('clear')
                print("IN ORDER TO PROCEED, YOU WILL BE REQUESTED TO ENTER THE FOLLOWING MANDATORY INFORMATION: ")
                print("------------------------------------------------------------------------------------------------------------------")
                print("1 - FILE OR FOLDER TO BE TRANSFERED ( IF THE FILE OR FOLDER IS NOT IN THE CURRENT DIRECTORY, ")
                print("YOU WILL NEED TO SPECIFY IT'S COMPLETE PATH TO IT IN THE FOLLOWING FORMAT-")
                print("EXAMPLE: local/path/of/file/or/folder/to_transfer")
                print("------------------------------------------------------------------------------------------------------------------")
                print("2 - USERNAME AND IP ADDRESS/HOST WHERE TO TRANSFER THE DATA IN THE FOLLOWING FORMAT: ")
                print("EXAMPLE: username@remote_host_ipaddress or username@remote_host_name - ")
                print("------------------------------------------------------------------------------------------------------------------")
                print("3 - REMOTE DIRECTORY OR FOLDER OF HOST WERE THE DATA FILES/FOLDERS WILL BE PLACED - ")
                print("EXAMPLE: remote/path/to/place/file/or/folder/")
                print("------------------------------------------------------------------------------------------------------------------")
                print("IF YOU WANT TO GET BACK TO MAIN MENU, HIT '0', AND ENTER TO RETURN - ")
                print("------------------------------------------------------------------------------------------------------------------")
                loop = 63
                while (loop==63):

                    print("------------------------------------------------------------------------------------------------------------------")
                    print("STEP 1 - ENTER NOW LOCAL PATH OF FILE/FOLDER TO TRANSFER - ")
                    localpath=raw_input("( FORMAT EXAMPLE: local/path/of/file_or_folder ): ")
                    returntomain=("0")
                    if localpath==returntomain:
                        
                        import os
                        os.system('clear')
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 0
                    
                    else:
                        
                        print("------------------------------------------------------------------------------------------------------------------")
                        print("IF YOU MADE A MISTAKE AN NEED TO GET BACK TO STEP 1, ENTER '1' AT THE PROMPT TO RETURN")
                        print("------------------------------------------------------------------------------------------------------------------")
                        loop = 64
                        while (loop==64):

                            print("------------------------------------------------------------------------------------------------------------------")
                            print("STEP 2 - ENTER USERNAME@REMOTE_IP_ADDRESS OR USERNAME@REMOTE_HOSTNAME ")
                            remotehostuserip=raw_input("FORMAT EXAMPLE: ( USERNAME@REMOTE_IP_ADDRESS ) OR ( USERNAME@REMOTE_HOSTNAME ): ")
                            backtostep1=("1")
                            returntomain0=("0")
                            if remotehostuserip==returntomain0:
                            
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(1)
                                loop = 0

                            elif remotehostuserip==backtostep1:

                                loop = 63
                                

                            else:

                                
                                print("------------------------------------------------------------------------------------------------------------------")
                                print("IF YOU MADE A MISTAKE AN NEED TO GET BACK TO STEP 2, ENTER '2' AT THE PROMPT TO RETURN")
                                print("------------------------------------------------------------------------------------------------------------------")

                                loop = 65
                                while (loop==65):
                                    
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    print("STEP 3 - ENTER REMOTE HOST PATH TO PLACE DIRECTORY ")
                                    remotepath=raw_input("FORMAT EXAMPLE: remote/path/of/file_or_folder): ")
                                    backtostep2=("2")
                                    returntomain1=("0")
                                    if remotepath==returntomain1:
                                        
                                        import os
                                        os.system('clear')
                                        print("RETURNING TO MAIN MENU...")
                                        import time
                                        time.sleep(1)
                                        loop = 0

                                    elif remotepath==backtostep2:

                                        loop = 64

                                    else:
                                        print("-------------------------------------------------------------------------------------------------------------------")
                                        step3proccedornot=raw_input("IF YOU NEED TO CORRECT STEP 3, ENTER '3' TO DO SO NOW, IF NO CORRECTIONS ARE NEEDED, HIT ENTER TO RUN SCRIPT NOW: ")
                                        backtostep3=("3")
                                        returntomain2=("0")
                                        if step3proccedornot==returntomain2:

                                            import os
                                            os.system('clear')
                                            print("RETURNING TO MAIN MENU...")
                                            import time
                                            time.sleep(1)
                                            loop = 0
                                        
                                        elif step3proccedornot==backtostep3:

                                            loop == 65

                                        else:
                                            
                                            print("------------------------------------------------------------------------------------------------------------------")
                                            print("ATTEMPTING TO TRANSFER FILES NOW...")
                                            print("------------------------------------------------------------------------------------------------------------------")
                                            space=(" ")
                                            colon=(":")
                                            os.system('sudo scp -r' + space + localpath + space + remotehostuserip + colon + remotepath )
                                            print("------------------------------------------------------------------------------------------------------------------")
                                            print("SCRIPT WAS EXECUTED, IF THE DATA WAS CORRECTLY TRANSFERRED, YOU SHOULD SEE IT ABOVE THIS LINE, ")
                                            print("------------------------------------------------------------------------------------------------------------------") 
                                            raw_input("THE SCRIPT WAS EXECUTED AND THE PROGRAM NOW ENDS HERE, HIT ENTER TO CONTINUE TO READ FURTHER...")
                                            os.system('clear')
                                            print("##################################################################################################################")
                                            print("PROGRAM TERMINATED, IF THERE WAS AN ERROR CONNECTING OR TRANSFERING THE DATA, AND YOU DID NOT SEE ANYTHING, ")
                                            print("PLEASE RECHECK AND CONFIRM REACHABILITY TO HOST, CHECK THAT THE CORRECT CREDENTIALS WERE ENTERED, ")
                                            print("AND YOU CAN ACCESS VIA SSH TO REMOTE HOST. YOU CAN RE-LAUNCH THIS PROGRAM AGAIN BY RETURNING TO MAIN MENU. ")
                                            print("##################################################################################################################")
                                            raw_input("HIT ENTER TO NOW TO RETURN TO MAIN MENU...")
                                            import os
                                            os.system('clear')
                                            print("RETURNING TO MAIN MENU...")
                                            import time
                                            time.sleep(1)
                                            loop = 0

            else:
                
                import os
                os.system('clear')
                print("------------------------------------------------------------------------------------------------------------------")
                print("PLEASE ONLY ENTER EITHER '1', TO INITIATE PROGRAM, OR '0' TO RETURN TO MAIN MENU...")
                import time
                time.sleep(3)
                import os
                os.system('clear')
                loop = 60
                

    
    elif modeselection==filesandfolders:
        
        loop = 40
        while (loop==40):
            
            import os
            os.system('clear')
            filesandfoldersmode = colored("FILES AND FOLDERS MENU ACCESSED..", 'yellow', attrs=['bold'])
            print("***************************************************************************")
            print filesandfoldersmode
            print("***************************************************************************")
            print("MODE 0 - LIST ALL FILES AND FOLDERS IN CURRENT DIRECTORY")
            print("===========================================================================")
            print("MODE 1 - LIST ALL FILES AND FOLDERS IN ANOTHER DIRECTORY")
            print("===========================================================================")
            print("MODE 2 - CREATES A NEW FOLDER OR DIRECTORY")
            print("===========================================================================")
            print("MODE 3 - DELETES AN EXISTING FOLDER OR DIRECTORY")
            print("===========================================================================")
            print("MODE 4 - CREATES A NEW FILE")
            print("===========================================================================")
            print("MODE 5 - DELETES AN EXISTING FILE")
            print("===========================================================================")
            print("MODE 6 - COPIES AN EXISTING DIRECTORY TO ANOTHER DIRECTORY")
            print("===========================================================================")
            print("MODE 7 - MOVES AN EXISTING DIRECTORY TO ANOTHER DIRECTORY")
            print("===========================================================================")
            print("MODE 8 - COPIES AN EXISTING FILE TO ANOTHER DIRECTORY")
            print("===========================================================================")
            print("MODE 9 - MOVES AN EXISTING FILE TO ANOTHER DIRECTORY")
            print("***************************************************************************")
            print("ENTER '10' TO RETURN TO MAIN MENU - ( WHEN YOUR ARE INSIDE A MODE )")
            print("***************************************************************************")
            print("***************************************************************************")
            print("ENTER '11' TO RETURN TO MULTIPROGRAM MAIN MENU FROM HERE")
            print("***************************************************************************")
            selection=raw_input("SELECT OPERATION MODE AND HIT ENTER: ")
            print("---------------------------------------------------------------------------------------------------")
            listfilesandfolders=("0")
            listinanotherdirectory=("1")
            createsnewfolder=("2")
            deletesfolder=("3")
            createsnewfile=("4")
            deletesfile=("5")
            copiesdirectory=("6")
            movesdirectory=("7")
            copiesfile=("8")
            movesfile=("9")
            returntomainmenu=("10")
            returntomultiprogram=("11")

            if selection==listfilesandfolders:
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("LISTING FILES AND FOLDERS IN CURRENT DIRECTORY: ")
                print("----------------------------------------------------------------------------")
                import os
                os.system('ls -a -s -l -h')
                print("----------------------------------------------------------------------------")
                print("ABOVE ARE AL THE FILES AND FOLDERS LISTED IN THE CURRENT DIRECTORY: ")
                print("----------------------------------------------------------------------------")
                os.system('pwd')
                print("----------------------------------------------------------------------------")
                raw_input("HIT ENTER TO RETURN TO MAIN MENU --->")
                loop = 40

            elif selection==listinanotherdirectory:
                import os
                os.system('clear')
                print("-----------------------------------------------------------------------")
                print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                print("-----------------------------------------------------------------------")
                print("ENTER FULL PATH OF DIRECTORY TO VIEW FILES AND FOLDERS, ")
                specifieddirectory=raw_input("IF NO ENTRY IS DETECTED WHEN HITTING ENTER, CURRENT DIRECTORY WILL BE LISTED: ")
                returntomainmenu=("10")
                if specifieddirectory==returntomainmenu:
                    
                    import os
                    os.system('clear')
                    print("------------------------------------------------------------------------")
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(1)
                    loop = 40

                
                else:
                    
                    space=(" ")
                    print("----------------------------------------------------------------------------")
                    print("LISTING FILES AND FOLDERS IN SPECIFIED DIRECTORY: ")
                    print("----------------------------------------------------------------------------")
                    import os
                    os.system('ls -a -s -l -h' + space + specifieddirectory)
                    print("----------------------------------------------------------------------------")
                    print("ABOVE ARE AL THE FILES AND FOLDERS LISTED IN THE SPECIFIED DIRECTORY: " + specifieddirectory)
                    print("----------------------------------------------------------------------------")
                    print("CURRENT DIRECTORY IS: ")
                    print("----------------------------------------------------------------------------")
                    os.system('pwd')
                    print("----------------------------------------------------------------------------")
                    raw_input("HIT ENTER TO RETURN TO MAIN MENU --->")
                    loop = 40
            
            elif selection==createsnewfolder:

                loop = 41
                while (loop==41):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    print("ENTER NEW DIRECTORY OR FOLDER NAME  TO BE CREATED, ")
                    newfolderentered=raw_input("( YOU CAN SPECIFY A PATH TO CREATE IT IN ANOTHER DIRECTORY ): ")
                    print("-----------------------------------------------------------------------")
                    returntomainmenu=("10")
                    if newfolderentered==returntomainmenu:

                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40


                    else:
                        
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("THE NAME OF THE NEW FOLDER IS: " + newfolderentered)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        import os
                        os.system('sudo mkdir ' + newfolderentered)
                        print("FOLDER CREATED IN: ")
                        space=(" ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('ls . ' + space + newfolderentered)
                        print("---------------------------------------------------------------------------------------------------------------------")
                   
                    
                        loop = 42
                        while (loop==42):
                            
                            createanotherfolder=raw_input("DO YOU WANT TO CREATE ANOTHER FOLDER? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if createanotherfolder==yes:

                                loop = 41

                            elif createanotherfolder==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                import time
                                time.sleep(2)
                                loop = 42

            elif selection==deletesfolder:

                loop = 43
                while (loop==43):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    print("ENTER EXISTING DIRECTORY OR FOLDER TO BE DELETED, ")
                    deletesfolder=raw_input("YOU MUST SPECIFY A PATH IF IT IS NOT IN CURRENT DIRECTORY ): ")
                    reutrntomainmenu=("10")
                    print("-----------------------------------------------------------------------")
                    if deletesfolder==returntomainmenu:

                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:
                        
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("THE NAME OF THE DIRECTORY TO BE DELETED IS: " + deletesfolder)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILES CONTAINED IN THE DIRECTORY TO BE DELETED: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system( 'ls ' + deletesfolder)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("CURRENT DIRECTORY IS: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        import os
                        os.system("pwd")
                        space=(" ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('sudo rm -R' + space + deletesfolder)
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                        loop = 44
                        while (loop==44):
                            
                            deleteanotherfolder=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if deleteanotherfolder==yes:

                                loop = 43

                            elif deleteanotherfolder==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU IN 2 SECONDS...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 44
                        
                    
            if selection==createsnewfile:

                loop = 45
                while (loop==45):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    print("ENTER NEW FILE NAME TO BE CREATED, ")
                    newfilentered=raw_input("( YOU CAN SPECIFY A PATH TO CREATE IT IN ANOTHER DIRECTORY ): ")
                    returntomainmenu=("10")
                    if newfilentered==returntomainmenu:

                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:
                        
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("THE NAME OF THE NEW FILE IS: " + newfilentered)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        import os
                        os.system('sudo touch ' + newfilentered)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("CURRENT DIRECTORY: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('pwd')
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILE CREATED IS: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('ls ' + newfilentered)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        
                    
                        loop = 46
                        while (loop==46):
                            
                            createanotherfile=raw_input("DO YOU WANT TO CREATE ANOTHER FILE? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if createanotherfile==yes:

                                loop = 45

                            elif createanotherfile==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU IN 2 SECONDS...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                import time
                                time.sleep(2)
                                loop = 46

            elif selection==deletesfile:

                loop = 47
                while (loop==47):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    print("ENTER EXISTING FILE TO BE DELETED, ")
                    deletesfile=raw_input("SPECIFY FULL PATH, IF THE FILE IS NOT IN THIS DIRECTORY: ")
                    returntomainmenu=("10")
                    if deletesfile==returntomainmenu:
                        
                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:
                        
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("THE NAME OF THE FILE TO DELETE IS: " + deletesfile)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("CURRENT DIRECTORY IS: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('pwd')
                        import os
                        os.system( 'ls | grep ' + deletesfile)
                        os.system('sudo rm -r ' + deletesfile)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        
                    
                        loop = 48
                        while (loop==48):
                            
                            deleteanotherfile=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if deleteanotherfile==yes:

                                loop = 47

                            elif deleteanotherfile==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU IN 2 SECONDS...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 48


            elif selection==copiesdirectory:

                loop = 49
                while (loop==49):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    copiesdirectory=raw_input("ENTER EXISTING FULL PATH WITH DIRECTORY TO BE COPIED: ")
                    returntomainmenu=("10")
                    if copiesdirectory==returntomainmenu:
                        
                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:

                
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("DIRECTORY TO BE COPIED IS: ")
                        os.system('ls . -a -s -t -l -h ' + copiesdirectory )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        destination=raw_input("ENTER OR COPY AND PASTE FULL DESTINATION PATH INCLUDING DIRECTORY...")
                        space=(" ")
                        os.system('sudo cp -R ' + copiesdirectory  + space  + destination )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('ls . -a -s -t -l -h ' + destination )
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                        loop = 50
                        while (loop==50):
                            
                            copyanotherdirectory=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if copyanotherdirectory==yes:

                                loop = 49

                            elif copyanotherdirectory==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU IN 2 SECONDS...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 50



            elif selection==movesdirectory:

                loop = 51
                while (loop==51):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    directorytomove=raw_input("ENTER EXISTING FULL PATH WITH DIRECTORY TO BE MOVED: ")
                    returntomainmenu=("10")
                    if directorytomove==returntomainmenu:
                        
                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:

                        
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("DIRECTORY TO BE MOVED IS: ")
                        space=(" ")
                        os.system('ls . -l -h' + space + directorytomove)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        destinationdirectory=raw_input("ENTER DESTINATION DIRECTORY WHERE IT WILL BE MOVED: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("DIRECTORY WILL BE MOVED TO: ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        space=(" ")
                        os.system('ls . -l -h' + space + destinationdirectory)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('sudo mv '+ space + directorytomove + space + destinationdirectory)
                        os.system('ls -a -s -t -l -h' + space + destinationdirectory)
                        print("---------------------------------------------------------------------------------------------------------------------")
                        
                    
                        loop = 52
                        while (loop==52):
                            
                            moveanotherdirectory=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if moveanotherdirectory==yes:

                                loop = 51

                            if moveanotherdirectory==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 52


            elif selection==copiesfile:

                loop = 53
                while (loop==53):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    filetocopy=raw_input("ENTER EXISTING FULL PATH WITH FILE TO BE COPIED: ")
                    returntomainmenu=("10")
                    if filetocopy==returntomainmenu:
                        
                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:

                
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILE TO BE COPIED IS: ")
                        space=(" ")
                        os.system('find ' + space + filetocopy )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        destination=raw_input("ENTER OR COPY AND PASTE FULL DESTINATION PATH INCLUDING THE FILE TO BE COPIED...")
                        space=(" ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILE WILL BE COPIED TO: ")
                        space=(" ")
                        os.system('find ' + space + destination )
                        os.system('sudo cp ' + filetocopy  + space  + destination )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('ls . -a -s -t -l -h ' + space + destination )
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                        loop = 54
                        while (loop==54):
                            
                            copyanotherfile=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if copyanotherfile==yes:

                                loop = 53

                            elif copyanotherfile==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU IN 2 SECONDS...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 54

            elif selection==returntomultiprogram:

                import os
                os.system('clear')
                print("RETURNING TO MULTIPROGRAM MAIN MENU...")
                import time
                time.sleep(1)
                import os
                os.system('clear')
                loop = 0



            elif selection==movesfile:

                loop = 55
                while (loop==55):

                    import os
                    os.system('clear')
                    print("-----------------------------------------------------------------------")
                    print("IF YOU WISH TO RETURN TO MAIN MENU ENTER NUMBER '10'...")
                    print("-----------------------------------------------------------------------")
                    filetomove=raw_input("ENTER EXISTING FULL PATH WITH FILE TO BE MOVED: ")
                    returntomainmenu=("10")
                    if filetomove==returntomainmenu:
                        
                        import os
                        os.system('clear')
                        print("------------------------------------------------------------------------")
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 40

                    else:

                
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILE TO BE MOVED IS: ")
                        space=(" ")
                        os.system('find ' + space + filetomove )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        destinationtomovefile=raw_input("ENTER OR COPY AND PASTE FULL DESTINATION PATH INCLUDING THE FILE TO BE MOVED: ")
                        space=(" ")
                        print("---------------------------------------------------------------------------------------------------------------------")
                        print("FILE WILL BE MOVED TO: ")
                        space=(" ")
                        os.system('find ' + space + destinationtomovefile )
                        os.system('sudo mv ' + filetomove  + space  + destinationtomovefile )
                        print("---------------------------------------------------------------------------------------------------------------------")
                        os.system('ls . -a -s -t -l -h ' + space + destinationtomovefile )
                        print("---------------------------------------------------------------------------------------------------------------------")
                    
                        loop = 56
                        while (loop==56):
                            
                            moveanotherfile=raw_input("DO YOU WANT TO REPEAT THE PROCESS? ( y / n ) ")
                            print("------------------------------------------------------------------------")
                            yes=("y")
                            no=("n")
                            if moveanotherfile==yes:

                                loop = 55

                            elif moveanotherfile==no:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(1)
                                loop = 40

                            else:
                                
                                import os
                                os.system('clear')
                                print("PLEASE ENTER EITHER 'y' OR 'n' AS REQUESTED...")
                                print("----------------------------------------------")
                                import time
                                time.sleep(2)
                                loop = 56

        
            
    elif modeselection==copyprogramlocalorremote:

        loop = 70
        while (loop==70):
            
            import os
            os.system('clear')
            copylocalorremotemode = colored("COPY MULTIPROGRAM FILES MODE ACCESSED - ", 'yellow', attrs=['bold'])
            print copylocalorremotemode
            print("###############################################################################################")
            print("THIS PROGRAM COPIES AND TRANSFERS ALL 'MULTIPROGRAM COMMAND LINE' AND 'BUTTON CONSOLE'  ")
            print("FILES LOCATED IN YOUR HOME DIRECTORY, TO A FOLDER NAMED MULTIPROGRAM IN SPECIFIED LOCAL")
            print("DIRECTORY, OR A REMOTE FOLDER VIA SCP")
            print("-----------------------------------------------------------------------------------------------")
            print("IT AUTOMATICALLY SAVES A COPY OF ALL THE FILES IN THE THE LOCAL OR REMOTE HOME DIRECTORY BY DEFAULT,")
            print("WHERE THEY NEED TO BE FOR THE PROGRAM TO RUN AND WORK PROPERLY")
            print("#############################################################################################")
            print("MODE 1 - TRANSFERS IT TO A SPECIFIED LOCAL DIRECTORY: ")
            print("---------------------------------------------------------------------------------------------")
            print("MODE 2 - TRANSFERS IT TO A REMOTE DIRECTORY: ")
            print("---------------------------------------------------------------------------------------------")
            print("- TO GET BACK TO MAIN MENU TYPE '0', AND HIT ENTER -")
            print("---------------------------------------------------------------------------------------------")
            scporlocal=raw_input("PLEASE SELECT A MODE AND HIT ENTER: ")
            local=("1")
            scpremote=("2")
            returntomainmenu_01=("0")
            
            if scporlocal==local:
                
                loop = 75
                while (loop==75):

                    import os
                    os.system('clear')
                    print("MODE 1 SELECTED...")
                    print("---------------------------------------------------------------------------------------------")
                    print("CREATING FOLDER AND COPYING PROGAM FILES TO IT...")
                    print("---------------------------------------------------------------------------------------------")
                    os.system('sudo mkdir /home/MULTIPROGRAM')
                    os.system('sudo bash /home/copyallmultiprogramfiles.sh')
                    print("---------------------------------------------------------------------------------------------")
                    os.system('ls -a -s -t -l -h | grep MULTIPROGRAM')
                    print("---------------------------------------------------------------------------------------------")
                    os.system('ls -a -h -l -t /home/MULTIPROGRAM')
                    print("---------------------------------------------------------------------------------------------")
                    copylocal=raw_input("SPECIFY FULL LOCAL PATH TO COPY THE FOLDER TO (EXAMPLE FORMAT /PATH/TO/FOLDER/): ")
                    space=(" ")
                    os.system('sudo cp -r /home/MULTIPROGRAM/ ' + space + copylocal)
                    print("---------------------------------------------------------------------------------------------")
                    print("THE SPECIFIED DIRECTORY IS: " + copylocal)
                    print("---------------------------------------------------------------------------------------------")
                    os.system('ls -a -h -l -t' + space + copylocal)
                    print("---------------------------------------------------------------------------------------------")
                    loop = 71
                    while (loop==71):
                        
                        print("---------------------------------------------------------------------------------------------")
                        print("MODE 1 PROGRAM ENDED, HIT '0' TO GET BACK TO MAIN MENU-")
                        print("---------------------------------------------------------------------------------------------")
                        print("HIT '1' TO RELAUNCH THIS MODE AND RE-COPY FOLDER-")
                        print("---------------------------------------------------------------------------------------------")
                        print("OR 2 TO RELAUNCH THE HOLE PROGRAM: ")
                        print("---------------------------------------------------------------------------------------------")
                        relaunchtomainmenuornot=raw_input("WAITING FOR INPUT: ")
                        returntomainmenu02=("0")
                        relaunchmode1=("1")
                        relaunchallprogram=("2")
                        
                        if relaunchtomainmenuornot==returntomainmenu02:
                            
                            import os
                            os.system('clear')
                            print("RETURNING TO MAIN MENU...")
                            import time
                            time.sleep(1)
                            loop = 0

                        elif relaunchtomainmenuornot==relaunchmode1:

                            import os
                            os.system('clear')
                            print("RELAUNCHING MODE 1...")
                            import time
                            time.sleep(1)
                            loop = 75

                        elif relaunchtomainmenuornot==relaunchallprogram:

                            import os
                            os.system('clear')
                            print("RELAUNCHING THE PROGRAM ...")
                            import time
                            time.sleep(1)
                            loop = 70

                        else:

                            import os
                            os.system('clear')
                            print("PLEASE ENTER EITHER '0', '1' OR '2'...")
                            import time
                            time.sleep(1)
                            loop = 71
                
            elif scporlocal==scpremote:
                
                import os
                os.system('clear')
                print("MODE 2 SELECTED...")
                print("---------------------------------------------------------------------------------------------")
                print("SCP TRANSFER MODE ACCESSED")
                print("##################################################################################################################")
                print("THIS PROGRAM TRANSFERS THE EXISTING MULTIPROGRAM FOLDER LOCATED IN THE HOME DIRECTORY CONTAINING ALL PROGRAM FILES,")
                print("TO A REMOTE HOST VIA SCP PROTOCOL -")
                print("##################################################################################################################")
                continueornot=raw_input("HIT ENTER TO INITIATE PROGRAM, OR '0' AND ENTER TO GET BACK TO PREVIOUS SCREEN...")
                previousscreen=("0")
                if continueornot==previousscreen:

                        import os
                        os.system('clear')
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 70

                else:

                    import os
                    os.system('clear')
                    print("IN ORDER TO PROCEED, YOU WILL BE REQUESTED TO ENTER THE FOLLOWING MANDATORY INFORMATION: ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    print("1 - USERNAME AND IP ADDRESS/HOST WHERE TO TRANSFER THE FOLDER IN THE FOLLOWING FORMAT: ")
                    print("EXAMPLE: username@remote_host_ipaddress or username@remote_host_name - ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    print("2 - REMOTE DIRECTORY OR FOLDER OF HOST WERE THE DATA FOLDER WILL BE PLACED - ")
                    print("EXAMPLE: remote/path/to/place/file/or/folder/: ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    print("- TO GET BACK TO MAIN MENU FROM ANY MODE TYPE '0' AND HIT ENTER- ")
                    print("------------------------------------------------------------------------------------------------------------------")
                    
                    
                    loop = 72
                    while (loop==72):
                        
                        print("- '0' TO GET BACK TO MAIN MENU - ")
                        print("------------------------------------------------------------------------------------------------------------------")
                        print("- '1' TO GET BACK TO MODES SCREEN")
                        print("------------------------------------------------------------------------------------------------------------------")
                        print("STEP 1 - ENTER USERNAME@REMOTE_IP_ADDRESS OR USERNAME@REMOTE_HOSTNAME ")
                        remotehostuserip=raw_input("FORMAT EXAMPLE: ( USERNAME@REMOTE_IP_ADDRESS ) OR ( USERNAME@REMOTE_HOSTNAME ): ")
                        returntomain03=("0")
                        relaunchallprogram2=("1")
                      
                        if remotehostuserip==returntomain03:

                            import os
                            os.system('clear')
                            print("RETURNING TO MAIN MENU...")
                            import time
                            time.sleep(1)
                            loop = 0

                        elif remotehostuserip==relaunchallprogram2:

                            import os
                            os.system('clear')
                            print("RELAUNCHING THE PROGRAM ...")
                            import time
                            time.sleep(1)
                            loop = 70

                        

                        else:

                            print("------------------------------------------------------------------------------------------------------------------")
                            print("IF YOU MADE A MISTAKE AN NEED TO GET BACK TO STEP 1, ENTER '1' AT THE PROMPT TO RETURN OR '0' TO RETURN TO MAIN MENU")
                            print("------------------------------------------------------------------------------------------------------------------")
                            print("- '0' TO GET BACK TO MAIN MENU - ")
                            print("------------------------------------------------------------------------------------------------------------------")
                            print("- '2' TO GET BACK TO MODES SCREEN")
                            print("------------------------------------------------------------------------------------------------------------------")
                            loop = 73
                            while (loop==73):

                                print("------------------------------------------------------------------------------------------------------------------")
                                print("STEP 2 - ENTER REMOTE HOST PATH TO PLACE DIRECTORY ")
                                remotepath=raw_input("FORMAT EXAMPLE: remote/path/of/file_or_folder): ")
                                returntomain04=("0")
                                backtostep1=("1")
                                relaunchallprogram3=("2")
                                if remotepath==returntomain04:
                                    
                                    import os
                                    os.system('clear')
                                    print("RETURNING TO MAIN MENU...")
                                    import time
                                    time.sleep(1)
                                    loop = 0

                                elif remotepath==backtostep1:

                                    loop = 72

                                elif remotepath==relaunchallprogram3:

                                    import os
                                    os.system('clear')
                                    print("RELAUNCHING THE PROGRAM ...")
                                    import time
                                    time.sleep(1)
                                    loop = 70

                                else:
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    print("STEP 3 - CHECK ALL ENTERED DATA IS CORRECT, AS ONCE YOU HIT ENTER THE SCRIPT WILL RUN -")
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    print("IF ALL DATA ENTERED IS CORRECT HIT ENTER, ")
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    print("TO GET BACK TO STEP 2, TYPE '2' OR '0' TO RETURN TO MAIN MENU, ")
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    print("OR HIT '1' -TO RELAUNCH THE PROGRAM-")
                                    print("------------------------------------------------------------------------------------------------------------------")
                                    proceedorbacktostep2=raw_input("WAITING FOR USER INPUT: ")
                                    returntomain05=("0")
                                    relaunchallprogram4=("1")
                                    backtostep2=("2")
                                    if proceedorbacktostep2==returntomain05:
                                        
                                        import os
                                        os.system('clear')
                                        print("RETURNING TO MAIN MENU...")
                                        import time
                                        time.sleep(1)
                                        loop = 0

                                    elif proceedorbacktostep2==backtostep2:

                                        loop == 73

                                    elif proceedorbacktostep2==relaunchallprogram4:

                                        import os
                                        os.system('clear')
                                        print("RELAUNCHING THE PROGRAM ...")
                                        import time
                                        time.sleep(1)
                                        loop = 70
                                    
                                    else:
                                        
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        print("ATTEMPTING TO TRANSFER FILES NOW...")
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        homemultiprogram=("/home/MULTIPROGRAM/")
                                        space=(" ")
                                        colon=(":")
                                        os.system('sudo scp -r' + space + homemultiprogram + space + remotehostuserip + colon + remotepath )
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        os.system('clear')
                                        print("PROGRAM TERMINATED, GET BACK TO MAIN MENU, RELAUNCH THIS MODE, OR RELAUNCH PROGRAM?: ")
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        print("'0' OR 'ENTER' TO GET BACK TO MAIN MENU")
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        print("'1' - TO RELAUNCH THE PROGRAM")
                                        print("------------------------------------------------------------------------------------------------------------------")
                                        relaunchoptions=raw_input("WAITING FOR USER INPUT: ")
                                        returntomain05=("0")
                                        relaunchthisprogram=("1")
                                        
                                        if relaunchoptions==returntomain05:
                                            
                                            import os
                                            os.system('clear')
                                            print("RETURNING TO MAIN MENU...")
                                            import time
                                            time.sleep(1)
                                            loop = 0

                                        elif relaunchoptions==relaunchthisprogram:

                                            import os
                                            os.system('clear')
                                            print("RELAUNCHING THE PROGRAM...")
                                            import time
                                            time.sleep(1)
                                            loop = 70

                                        else:
                                            
                                            import os
                                            os.system('clear')
                                            print("RETURNING TO MAIN MENU...")
                                            import time
                                            time.sleep(1)
                                            loop = 0
                                              
                                                             

                
                
            elif scporlocal==returntomainmenu_01:

                import os
                os.system('clear')
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(1)
                loop = 0

            else:
                
                import os
                os.system('clear')
                print("PLEASE ENTER EITHER '1', '2', OR '0'...")
                import time
                time.sleep(1)
                loop = 70
        

                  
            
    elif modeselection==backtomenu0:
        import os
        os.system('clear')
        alreadyinmainmenu = colored("YOU ALREADY ARE IN MAIN MENU!, USE THIS WHEN IN SUBMENUES", 'red', attrs=['bold'])
        print alreadyinmainmenu
        import time
        time.sleep(3)
        import os
        os.system('clear')
        loop = 0


    elif modeselection==createciscorouterscripts:
        loop = 95
        while (loop==95):

            import time
            time.sleep(1)
            import os
            os.system('clear')
            ciscorouterscripts = colored("SHELL SCRIPT CREATION FOR CISCO ROUTERS MODE ACCESSED...", 'cyan', attrs=['bold'])
            print("----------------------------------------------------------------------------------")
            print ciscorouterscripts
            print("----------------------------------------------------------------------------------")
            print("Mode 0 - TELNET - OBTAIN NETWORK STATUS REPORT FROM A CISCO ROUTER")
            print("Mode 1 - SSH - OBTAIN NETWORK STATUS REPORT FROM CISCO ROUTER")
            print("----------------------------------------------------------------------------------")
            print("Mode 2 - TELNET - RETRIEVE RUNNING CONFIG FROM ROUTER TO TXT FILE")
            print("Mode 3 - SSH - RETRIEVE RUNNING CONFIG FROM ROUTER TO TXT FILE")
            print("----------------------------------------------------------------------------------")
            print("m - RETURNS BACK TO MAIN MENU")
            print("----------------------------------------------------------------------------------")
            selectoption1=raw_input("SELECT DESIRED MODE AND HIT ENTER: ")
            telnet_script_check=("0")
            ssh_script_check=("1")
            telnet_running_config_script=("2")
            ssh_running_config_script=("3")
            backtomainmenufromcreatescripts=("m")
            if selectoption1==telnet_script_check:

                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("YOU ARE IN MODE 0")
                print("----------------------------------------------------------------------------")
                os.system('sudo bash /home/create-telnet-script-to-check-router-network-status.sh')
            
                loop = 95

            elif selectoption1==ssh_script_check:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("YOU ARE IN MODE 1")
                print("----------------------------------------------------------------------------")
                os.system('sudo bash /home/create-ssh-script-to-check-router-network-status.sh')

                loop = 95

            elif selectoption1==telnet_running_config_script:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("YOU ARE IN MODE 2")
                print("----------------------------------------------------------------------------")
                os.system('sudo bash /home/create-telnet-script-to-get-running-config.sh')

                loop = 95

            elif selectoption1==ssh_running_config_script:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("YOU ARE IN MODE 3")
                print("----------------------------------------------------------------------------")
                os.system('sudo bash /home/create-ssh-script-to-get-running-config.sh')

                loop = 95

            elif selectoption1==backtomainmenufromcreatescripts:
                
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(2)
                import os
                os.system('clear')
                loop = 0

            else:
                import os
                os.system('clear')
                print("PLEASE ENTER EITHER 0, 1, 2, 3 OR m, TO GET BACK TO MAIN MENU...")
                import time
                time.sleep(3)
                import os
                os.system('clear')
                loop = 95

    elif modeselection==runlinuxcommands:
        import os
        os.system('clear')
        runlinuxcommandsmode = colored("TERMINAL MODE", 'yellow', attrs=['bold'])
        print runlinuxcommandsmode
        os.system('sudo python /home/input-terminal-commands.py')
        os.system('clear')
        loop = 0
        
    elif modeselection==runscripts:
        loop = 118
        while(loop==118):
            
            import os
            os.system('clear')
            runsavedscripts = colored("RUN SCRIPTS MODE ACCESSED", 'cyan', attrs=['bold'])
            print("------------------------------------------------------------------------------------------------")
            print runsavedscripts
            print("------------------------------------------------------------------------------------------------")
            print("0 - TO ENTER TELNET SAVED SCRIPTS MODE")
            print("1 - TO ENTER SSH SAVED SCRIPTS MODE")
            print("------------------------------------------------------------------------------------------------")
            print("m - RETURNS BACK TO MAIN MENU")
            print("----------------------------------------------------------------------------------")
            scriptsmodes=raw_input("SELECT MODE AND HIT ENTER: ")
            telnetrunscripts=("0")
            sshrunscripts=("1")
            backtomainmenufromscriptsmodes=("m")
            if scriptsmodes==telnetrunscripts:
                
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
                    print("p - TO GET BACK TO PREVIOUS SCREEN")
                    print("m - RETURNS BACK TO MAIN MENU")
                    print("----------------------------------------------------------------------------------------------------------------")
                    runalltelnetscriptsornot=raw_input("SELECT A MODE, ENTER NUMBER AND HIT ENTER: ")
                    telnetrunspecific=("0")
                    telnetrunmorethanone=("1")
                    telnetrunallscripts=("2")
                    previousscreen=("p")
                    mainmenu1=("m")
                
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
                                print("m - TO GET BACK TO MAIN MENU 'MULTIPROGRAM'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                telnet_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                telnet_relaunch_yes=("0")
                                telnet_get_back_to_menu_modes=("1")
                                telnet_relaunch_mode_or_not_back_to_main=("m")
                                if telnet_relaunch_mode_or_not==telnet_relaunch_yes:
                                    import os
                                    os.system('clear')
                                    loop = 102
                                elif telnet_relaunch_mode_or_not==telnet_get_back_to_menu_modes:
                                    
                                    import os
                                    os.system('clear')
                                    loop = 101

                                elif telnet_relaunch_mode_or_not==telnet_relaunch_mode_or_not_back_to_main:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                
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
                                print("m - TO GET BACK TO MAIN MENU 'MULTIPROGRAM'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                telnet_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                telnet_relaunch_yes=("0")
                                telnet_get_back_to_menu_modes=("1")
                                telnet_relaunch_mode_or_not_back_to_main2=("m")
                                if telnet_relaunch_mode_or_not==telnet_relaunch_yes:
                                    import os
                                    os.system('clear')
                                    loop = 104
                                elif telnet_relaunch_mode_or_not==telnet_get_back_to_menu_modes:
                                    import os
                                    os.system('clear')
                                    loop = 101

                                elif telnet_relaunch_mode_or_not==telnet_relaunch_mode_or_not_back_to_main2:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                else:
                                    import os
                                    os.system('clear')
                                    print("PLEASE ENTER EITHER '0' OR '1'...")
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
                                print("m - TO GET BACK TO MAIN MENU 'MULTIPROGRAM'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                telnet_all_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                telnet_all_relaunch_yes=("0")
                                telnet_all_get_back_to_menu_modes=("1")
                                telnet_relaunch_mode_or_not_back_to_main3=("m")
                                if telnet_all_relaunch_mode_or_not==telnet_relaunch_yes:
                                    import os
                                    os.system('clear')
                                    loop = 106
                                elif telnet_all_relaunch_mode_or_not==telnet_get_back_to_menu_modes:
                                    import os
                                    os.system('clear')
                                    loop = 101
                                elif telnet_all_relaunch_mode_or_not==telnet_relaunch_mode_or_not_back_to_main3:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                else:
                                    import os
                                    os.system('clear')
                                    print("PLEASE ENTER EITHER '0' OR '1'...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 107


                    elif runalltelnetscriptsornot==previousscreen:
                        import os
                        os.system('clear')
                        loop = 118
                        
                    elif runalltelnetscriptsornot==mainmenu1:
                        import os
                        os.system('clear')
                        loop = 0

                    
            
        

            if scriptsmodes==sshrunscripts:

                loop = 108
                while(loop==108):

                    import os
                    os.system('clear')
                    print("SSH SCRIPTS MODE ACCESSED")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("0 - TO RUN ONLY A SPECIFIC SCRIPT")
                    print("1 - TO RUN MORE THAN 1 SCRIPT, OR MULTIPLE SCRIPTS (UP TO 10 SCRIPTS SUPPORTED) ")
                    print("2 - TO RUN ALL SCRIPTS SAVED")
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("p - TO GET BACK TO PREVIOUS SCREEN")
                    print("m - RETURNS BACK TO MAIN MENU")
                    print("----------------------------------------------------------------------------------------------------------------")
                    runallsshscriptsornot=raw_input("SELECT A MODE, ENTER NUMBER AND HIT ENTER: ")
                    sshrunspecific=("0")
                    sshrunmorethanone=("1")
                    sshrunallscripts=("2")
                    previousscreen=("p")
                    mainmenu=("m")
                    if runallsshscriptsornot==previousscreen:
                        import os
                        os.system('clear')
                        loop = 118
                        
                    elif runallsshscriptsornot==mainmenu:
                        import os
                        os.system('clear')
                        loop = 0

                    
                    if runallsshscriptsornot==sshrunspecific:
                        loop = 109
                        while(loop==109):
                            
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
                            loop = 110
                            while(loop==110):
                                
                                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO SSH SCRIPTS MODES?")
                                print("----------------------------------------------------------------------------------------------------------------")
                                print("0 - TO RELAUNCH THIS MODE")
                                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                                print("m - TO GET BACK TO MAIN MENU 'MULTIPROGRAM'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                ssh_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                ssh_relaunch_yes=("0")
                                ssh_get_back_to_menu_modes=("1")
                                ssh_relaunch_mode_or_not_back_to_main=("m")
                                if ssh_relaunch_mode_or_not==ssh_relaunch_yes:
                                    import os
                                    os.system('clear')
                                    loop = 109
                                elif ssh_relaunch_mode_or_not==ssh_get_back_to_menu_modes:
                                    import os
                                    os.system('clear')
                                    loop = 108
                                elif ssh_relaunch_mode_or_not==ssh_relaunch_mode_or_not_back_to_main:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                else:
                                    import os
                                    os.system('clear')
                                    print("PLEASE ENTER EITHER '0' OR '1'...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 110

                    

                    elif runallsshscriptsornot==sshrunmorethanone:
                        loop = 112
                        while(loop==112):
                            
                            import os
                            os.system('clear')
                            print("----------------------------------------------------------------------------------------------------------------")
                            print("YOU ARE IN MODE 1")
                            print("----------------------------------------------------------------------------------------------------------------")
                            os.system('sudo bash /home/cisco-ssh-access-scripts-logs/ssh-scriptmultiple.sh')
                            loop = 113
                            while(loop==113):
                                
                                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO TELNET SCRIPTS MODES?")
                                print("----------------------------------------------------------------------------------------------------------------")
                                print("0 - TO RELAUNCH THIS MODE")
                                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                                print("m - TO GET BACK TO MAIN MENU 'MULTIPROGRAM'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                ssh_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                ssh_relaunch_yes=("0")
                                ssh_get_back_to_menu_modes=("1")
                                ssh_relaunch_mode_or_not_back_to_main=("m")
                                if ssh_relaunch_mode_or_not==ssh_relaunch_yes:
                                    
                                    import os
                                    os.system('clear')
                                    loop = 112
                                elif ssh_relaunch_mode_or_not==ssh_get_back_to_menu_modes:

                                    import os
                                    os.system('clear')
                                    loop = 108
                                elif ssh_relaunch_mode_or_not==ssh_relaunch_mode_or_not_back_to_main:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                    
                                else:
                                    import os
                                    os.system('clear')
                                    print("PLEASE ENTER EITHER '0' OR '1'...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 113

                    elif runallsshscriptsornot==sshrunallscripts:
                        
                        loop = 114
                        while(loop==114):
                            
                            import os
                            os.system('clear')
                            print("----------------------------------------------------------------------------------------------------------------")
                            print("YOU ARE IN MODE 2")
                            print("----------------------------------------------------------------------------------------------------------------")
                            os.system('sudo bash /home/runscripts-cisco-ssh-access-scripts-logs.sh')
                            loop = 115
                            while(loop==115):
                                
                                print("SCRIPT EXECUTED, RELAUNCH THIS MODE?, OR GO BACK TO SSH SCRIPTS MODES?")
                                print("----------------------------------------------------------------------------------------------------------------")
                                print("0 - TO RELAUNCH THIS MODE")
                                print("1 - TO GET BACK TO MAIN MENU 'SSH SCRIPTS MODE'")
                                print("----------------------------------------------------------------------------------------------------------------")
                                ssh_all_relaunch_mode_or_not=raw_input("SELECT EITHER '0' OR '1'")
                                ssh_all_relaunch_yes=("0")
                                ssh_all_get_back_to_menu_modes=("1")
                                ssh_relaunch_mode_or_not_back_to_main=("m")
                                if ssh_all_relaunch_mode_or_not==ssh_all_relaunch_yes:
                                    import os
                                    os.system('clear')
                                    loop = 114
                                elif ssh_all_relaunch_mode_or_not==ssh_all_get_back_to_menu_modes:
                                    import os
                                    os.system('clear')
                                    loop = 108

                                elif ssh_all_relaunch_mode_or_not==ssh_relaunch_mode_or_not_back_to_main:
                                    import os
                                    os.system('clear')
                                    loop = 0
                                else:
                                    import os
                                    os.system('clear')
                                    print("PLEASE ENTER EITHER '0' OR '1'...")
                                    import time
                                    time.sleep(2)
                                    import os
                                    os.system('clear')
                                    loop = 115


                    elif runallsshscriptsornot==previousscreen:
                        import os
                        os.system('clear')
                        loop = 118
                        
                    elif runallsshscriptsornot==mainmenu:
                        import os
                        os.system('clear')
                        loop = 0

                    else:
                        import os
                        os.system('clear')
                        print("-----------------------------------------------------------------------------------------------")
                        print("PLEASE SELECT OPTIONS FROM THE MENU,...")
                        import time
                        time.sleep(2)
                        loop = 0
            
                
            elif scriptsmodes==backtomainmenufromscriptsmodes:
                import os
                os.system('clear')
                print("RETURNING TO MAIN MENU...")
                import time
                time.sleep(2)
                import os
                os.system('clear')
                loop = 0

            
            
    elif modeselection==loggingmode:

        loop = 80
        while (loop==80):
            
            import os
            os.system('clear')
            print("------------------------------------------------------------------------------------------------")
            print("LOGGING MODE ACCESED, ALL INPUT AND OUTPUT FROM TERMINAL WILL BE LOGGEED, AND SENT TO")
            print("'loggingfromterminal.log' FILE LOCATED IN /HOME/$USER/ DIRECTORY")
            print("------------------------------------------------------------------------------------------------")
            print("'0' - TO RETURN TO MAIN MENU - ")
            print("------------------------------------------------------------------------------------------------")
            print("'exit' - TO STOP LOGGING MODE - ")
            print("------------------------------------------------------------------------------------------------")
            all_loging=raw_input("HIT '1' AND ENTER TO BEGIN LOGGING EVERYTHING NOW: ")
            returntomainmenuornot=("0")
            startlogging=("1")
            if all_loging==returntomainmenuornot:
                
                  import os
                  os.system('clear')
                  print("RETURNING TO MAIN MENU...")
                  import time
                  time.sleep(1)
                  loop = 0

            elif all_loging==startlogging:
                
                  import os
                  os.system('clear')
                  print("------------------------------------------------------------------------------------------------")
                  import os
                  os.system('sudo script loggingfromterminal.log')
                  print("------------------------------------------------------------------------------------------------")
                  print("ALL LOGGING WAS STOPPED - ")
                  print("------------------------------------------------------------------------------------------------")
                  print("ALL INPUT AND OUTPUT WAS SAVED TO FILE 'loggingfromterminal.log' LOCATED AT: ")
                  print("------------------------------------------------------------------------------------------------")
                  os.system('ls -t -l -h /home/loggingfromterminal.log')
                  print("------------------------------------------------------------------------------------------------")
                  viewloggingfileornot=raw_input("DO YOU WISH TO SEE THE LOG FILE NOW? ( y / n ): ")
                  viewlogfilenow=("y")
                  donotviewlogfile=("n")
                  
                  if viewloggingfileornot==donotviewlogfile:

                      import os
                      os.system('clear')
                      loop = 82
                      while (loop==82):
                          print("------------------------------------------------------------------------------------------------------------")
                          wanttoreturntomain2=raw_input("DO YOU WANT TO RETURN TO MAIN MENU, OR RELAUNCH LOGGING PROGRAM?: ( 'l' to re-log / 'm' for main menu ) ")
                          returntomainmenunow2=("m")
                          relog2=("l")
                          if wanttoreturntomain2==returntomainmenunow2:
                              
                              import os
                              os.system('clear')
                              print("RETURNING TO MAIN MENU...")
                              import time
                              time.sleep(1)

                              loop = 0

                          elif wanttoreturntomain2==relog2:
                              
                              import os
                              os.system('clear')
                              print("RELAUNCHING LOGGING PROGRAM...")
                              import time
                              time.sleep(1)
                          
                              loop = 80

                          else:
                              
                              import os
                              os.system('clear')
                              print("PLEASE ENTER EITHER 'l', OR 'm'...")
                              import time
                              time.sleep(2)
                              loop = 82
                                
                  elif viewloggingfileornot==viewlogfilenow:
                      
                      import os
                      os.system('clear')
                      os.system('cat /home/loggingfromterminal.log')
                      import time
                      time.sleep(1)
                      loop = 81
                      while (loop==81):
                          print("------------------------------------------------------------------------------------------------------------")
                          wanttoreturntomain1=raw_input("DO YOU WANT TO RETURN TO MAIN MENU, OR RELAUNCH LOGGING PROGRAM?: ( 'l' to re-log / 'm' for main menu )")
                          returntomainmenunow1=("m")
                          relog1=("l")
                          if wanttoreturntomain1==returntomainmenunow1:
                              
                              import os
                              os.system('clear')
                              print("RETURNING TO MAIN MENU...")
                              import time
                              time.sleep(1)

                              loop = 0

                          elif wanttoreturntomain1==relog1:
                              
                              import os
                              os.system('clear')
                              print("RELAUNCHING LOGGING PROGRAM...")
                              import time
                              time.sleep(1)
                              
                              loop = 80

                          else:
                              import os
                              os.system('clear')
                              print("PLEASE ENTER EITHER 'l', OR 'm'...")
                              import time
                              time.sleep(2)
                              loop = 81
                              

                     
                     
                     
                      
            else:

                import os
                os.system('clear')
                print("PLEASE ENTER EITHER '1', OR '0'...")
                import time
                time.sleep(2)
                loop = 80
          
    
    
    

        

    else:
        import os
        os.system('clear')
        entervalidoptions = colored("ENTER VALID OPTIONS TO OPERATE THE PROGRAM...", 'red', attrs=['bold'])
        print("------------------------------------------------------------")
        print entervalidoptions
        print("------------------------------------------------------------")
        import time
        time.sleep(2)
        import os
        os.system('clear')
        loop = 0
        

            


