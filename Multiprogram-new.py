
print("WELCOME TO LINUX MULTIPROGRAM!, SELECT AN OPERATION MODE AND HIT ENTER TO BEGIN: ")
print("====================================================================================")
import time
time.sleep(2)

loop = 0
while (loop==0):

    print("YOU ARE IN MAIN MENU")
    print("************************************************************************************")
    import time
    time.sleep(1)
    print("BROWSING - OPEN A WEB BROWSER ")
    print("------------------------------------------------------------------------------------")
    print(" g - OPENS GOOGLE CHROME - f - OPENS MOZILLA FIREFOX  - c - OPENS CHROMIUM BROWSER")
    print("------------------------------------------------------------------------------------")
    print("ACCESS SYSTEM MODES AND CONTROL LINUX SYSTEM")
    print("------------------------------------------------------------------------------------")
    print("Mode 0 - ACCESSES UNIT CONVERSION MODES - DECIMAL TO BINARY NUMBERS AND OTHERS")
    print("Mode 1 - RUNS A GNOME TERMINAL")
    print("Mode 2 - RUNS GNOME CALCULATOR  ")
    print("Mode 3 - GETS LINUX SYSTEM DETAILED REPORT")
    print("Mode 4 - DEBUGS USB PLUG AND PLAY DEVICES")
    print("Mode 5 - ACCESSES LINUX UPDATE MODES")
    print("Mode 6 - MONITORING MODES - VIEW PROCESSES, SERVICES STATUS AND LOGS")
    print("Mode 7 - STARTS THIS PROGRAM IN ANOTHER TERMINAL")
    print("------------------------------------------------------------------------------------")
    print("NETWORK CONTROL MODE OPERATIONS")
    print("------------------------------------------------------------------------------------")
    print("Mode 8 - RELOADS ALL NETWORK INTERFACES AND LOGS INFO TO A FILE")
    print("Mode 9 - DISPLAYS CURRENT IP CONFIGURATION AND LOGS INFO TO A FILE")
    print("Mode 10 - SCANS YOUR LAN WITH IPSCAN TOOL")
    print("Mode 11 - MONITORS LAN NETWORK BANDWIDTH")
    print("Mode 12 - ACCESSES A CISCO DEVICE ROUTER/L3 DEVICE TO OBTAIN ACTUAL NETWORK STATUS")
    print("------------------------------------------------------------------------------------")
    print("Mode 13 - SYSTEM REBOOT OR SHUTDOWN MENU - SHUTS DOWN OR RESTARTS SYSTEM")		
    print("------------------------------------------------------------------------------------")
    print("When inside a Mode, Type (m) and hit enter to get back to main menu...")
    print("------------------------------------------------------------------------------------")
    print("TO EXIT THIS PROGRAM JUST TYPE: exit, AND HIT ENTER")
    print("####################################################################################")

    modeselection=raw_input("Enter  operation mode (example: for mode 0, type 0) and hit enter: ")
    googlechrome=("g")
    mozillafirefox=("f")
    chromiumwebbrowser=("c")

    conversionmode=("0")
    gnometerminal=("1")
    calculatormode=("2")
    linuxsysteminfo=("3")
    debugsusbplugandplay=("4")
    updatemodes=("5")
    monitoringmodes=("6")
    anotherterminal=("7")
    
    
    reloadnetworkints=("8")
    currentipconfig=("9")
    scansyourlan=("10")
    monitornetwork=("11")
    accessciscodevice=("12")
    
    rebootorshutdown=("13")
    
    backtomenu0=("m")
    backtomainmenu=("m")
    backtomenu1=("m")
    exitprogram=("exit"or"EXIT")

    if modeselection==conversionmode:

        loop = 16
        while (loop==16):

                import os
                os.system('clear')
                print("#####################################")
                print("YOU ARE IN UNIT CONVERSION MODE")
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




    elif modeselection==calculatormode:
        loop = 26
        while (loop==26):
            
            import os
            os.system('clear') 
            import time
            time.sleep(1)
            print("--------------------------------")
            print(" c - TO LAUNCH CALCULATOR NOW...")
            print(" m - TO GET BACK TO MAIN MENU...")
            print("--------------------------------")
            calculatorlaunch=("c")
            returntomainmenu=("m")
            selectchoice=raw_input("LAUNCH CALCULATOR?.....c/m: ")
            try:
                
                if selectchoice==calculatorlaunch:
                                       import os
                                       os.system('gnome-calculator')
                                       import os
                                       os.system('clear')
                                       print("RETURNING TO MAIN MENU...")
                                       import time
                                       time.sleep(2)
                                       import os
                                       os.system('clear')
                                       loop = 0

                elif selectchoice==returntomainmenu:
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
                    print("ONLY (c), OR (m) IS ALLOWED...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 26

            except Valuerror:
                import os
                os.system('clear')
                print("ONLY (c), OR (m) IS ALLOWED...")
                import time
                time.sleep(1)
                import os
                os.system('clear')
                loop = 26
            
    
    elif modeselection==linuxsysteminfo:
        loop = 23
        while (loop==23):

            import os
            os.system('clear')
            print("YOU HAVE ACCESSED LINUX SYSTEMINFO MODES...")
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
                    
                
                    
                    
                

    elif modeselection==currentipconfig:
        import os
        os.system('clear')
        loop = 27
        while (loop==27):
            import os
            os.system('clear')
            import time
            time.sleep(1)
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
                    os.system('sudo rm /home/ipconfiguration.txt')
                    import os
                    os.system('sudo touch /home/ipconfiguration.txt')
                    print("DISPLAYING CURRENT IP CONFIGURATION...")
                    print("------------------------------------------------------")
                    import time
                    time.sleep(2)
                    import os
                    os.system('ifconfig -a')
                    print("------------------------------------------------------")
                    import os
                    os.system('uptime | sudo tee /home/ipconfiguration.txt')
                    print("------------------------------------------------------")
                    os.system('echo "------------------------------------------" ')
                    os.system('ifconfig | sudo tee /home/ipconfiguration.txt')
                    os.system('echo "------------------------------------------" ')
                    os.system('date | sudo tee /home/ipconfiguration.txt')
                    os.system('echo "------------------------------------------" ')
                    print("ipconfiguration.txt was created, you can see output of this command in this file at any time")
                    print("-------------------------------------------------------------------------------------")
                    import time
                    time.sleep(3)
                    print("located at your /home directory ")
                    print("-------------------------------------------------------------------------------------")
                    os.system('ls -l -a -h | grep ipconfiguration.txt')
                    print("-------------------------------------------------------------------------------------")
                    os.system('cat /home/ipconfiguration.txt')
                    print("-------------------------------------------------------------------------------------")
                    raw_input("Hit enter to get back to main menu...")
                    import time
                    time.sleep(2)
                    import os
                    os.system('clear')
                    loop = 0

                elif selectchoice==returntomainmenu:
                    import os
                    os.system('clear')
                    print("RETURNING TO MAIN MENU...")
                    import time
                    time.sleep(2)
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
            print("MONITORING MODES ACCESSED...")
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
                os.system('gnome-terminal -e "sudo bash /home/viewservices.sh"')

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
            print("RELOAD NETWORK INTERFACES MODE ACCESSED")
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

    elif modeselection==anotherterminal:
        
        import os
        os.system('gnome-terminal --window --maximize -e')
        os.system('bash /home/Multiprogram.sh')

    elif modeselection==rebootorshutdown:

        loop = 21
        while (loop==21):

            import os
            os.system('clear')
            print("SYSTEM CONTROL MENU")
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
            print("DEBUG USB PLUG AND PLAY MODE...")
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
        print("YOU ARE ABOUT TO EXIT THE PROGRAM")
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

        import time
        time.sleep(1)
        print("INSTALLING IPSCAN SCANNER...")
        time.sleep(1)
        import os
        os.system('sudo dpkg -i ipscan_3.4_amd64.deb')
        time.sleep(2)
        import os
        os.system('sudo ipscan')
        print("--------------------------------------------------------")
        print("APPLICATION TERMINATED, RETURNING TO MAIN MENU...")
        import os
        os.system('clear')
        loop = 0
        
    elif modeselection==monitornetwork:
        import time
        time.sleep(1)
        import os
        os.system('clear')
        print("INSTALLING NETWORK MONITOR...")
        import os
        os.system('sudo apt-get install speedometer')
        print("------------------------------------------------------")
        print("STARTING TO MONITOR LINUX eth0 AND wlan0 INTERFACES...")
        import time
        time.sleep(2)
        import os
        os.system('gnome-terminal --window --maximize -e "speedometer -i 0.25 -k 256 -t eth0 -r eth0 -t wlan0 -r wlan0"')
       
        loop = 0
            
        
    elif modeselection==accessciscodevice:
        loop = 29
        while (loop==29):
            import time
            time.sleep(1)
            import os
            os.system('clear')
            print("----------------------------------------------------------------------------------")
            print("CISCO DEVICE ACCESS MODE ENTERED...")
            print("----------------------------------------------------------------------------------")
            print("Mode 0 - TELNET TO OBTAIN NETWORK STATUS REPORT FROM CISCO ROUTER")
            print("Mode 1 - SSH TO OBTAIN NETWORK STATUS REPORT FROM CISCO ROUTER")
            print("----------------------------------------------------------------------------------")
            print("Mode 2 - TELNET TO RETRIEVE RUNNING CONFIG FROM ROUTER TO TXT FILE")
            print("Mode 3 - SSH TO RETRIEVE RUNNING CONFIG FROM ROUTER TO TXT FILE")
            print("----------------------------------------------------------------------------------")
            print("Mode 4 - INSTALL GNS3 NETWORK EMULATOR")
            print("----------------------------------------------------------------------------------")
            print("Mode 5 - CREATE BRIDGE AND TAP INTERFACES IN LINUX SYSTEM")
            print("Mode 6 - DELETE BRIDGE AND TAP INTERFACES IN LINUX SYSTEM")
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
                os.system('sudo bash /home/telnet-cisco-access.sh')
            
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
                os.system('sudo bash /home/ssh-cisco-access.sh')

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
                os.system('sudo bash /home/telnet-running-config.sh')

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
                os.system('sudo bash /home/ssh-running-config.sh')

                loop = 29



            elif selectoption==create:
                
                import time
                time.sleep(1)
                import os
                os.system('clear')
                print("----------------------------------------------------------------------------")
                print("CREATE BRIDGE AND TAP INTERFACES MODE ACCESSED...")
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
                print("DELETE BRIDGE AND TAP INTERFACES MODE ACCESSED...")
                print("----------------------------------------------------------------------------")
                print("running script now...")
                time.sleep(1)
                os.system('sudo bash /home/delete-bridge-interfaces.sh')

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
  
        

    elif modeselection==googlechrome:
        
        import os
        os.system('clear')                
        print("OPENING GOOGLE CHROME...")
        import time
        time.sleep(2)  
        import os
        os.system('gnome-terminal -e google-chrome')
        loop = 0

    elif modeselection==mozillafirefox:

        import os
        os.system('clear')                
        print("OPENING MOZILLA FIREFOX...")
        import time
        time.sleep(2)  
        import os
        os.system('gnome-terminal -e firefox')
        loop = 0

    elif modeselection==chromiumwebbrowser:
                                
        import os
        os.system('clear')                
        print("OPENING CHROMIUM BROWSER...")
        import time
        time.sleep(2)  
        import os
        os.system('gnome-terminal -e chromium-browser')
        loop = 0


            
    elif modeselection==backtomenu0:
        import os
        os.system('clear')
        print("YOU ALREADY ARE IN MAIN MENU!, USE THIS WHEN IN SUBMENUES")
        import time
        time.sleep(3)
        import os
        os.system('clear')
        loop = 0

    elif modeselection==gnometerminal:
        import os
        os.system('clear')                  
        import os
        os.system('gnome-terminal')
        loop = 0

    else:
        import os
        os.system('clear')
        print("------------------------------------------------------------")
        print("REMEMBER TO ENTER VALID OPTIONS TO OPERATE THE PROGRAM...")
        print("------------------------------------------------------------")
        import time
        time.sleep(2)
        import os
        os.system('clear')
        loop = 0
        

            


