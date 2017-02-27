# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import Tkinter

print("APPLICATION CONSOLE LAUNCHED, WAITING FOR INSTRUCTIONS...")

root = Tk()
root.title('MAIN LINUX BUTTON CONSOLE ADMINISTRATOR')



def multiprogram():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Multiprogram.py"')

button1 = Button(root, text="MODE 0 - LAUNCH COMMAND LINE INTERFACE LINUX MULTIPROGRAM", fg="white", bg="black", width=75, command=multiprogram)
button1.pack()

def managelinux():

    #Mode 1 - RUNS A GNOME TERMINAL
    root = Tk()
    root.title('MANAGE YOUR LINUX SYSTEM')
    def runsgnometerm():
        import os
        os.system('gnome-terminal')
        
    
    button2 = Button(root, text="RUN A GNOME TERMINAL", fg="white", bg="black", width=50, command=runsgnometerm)
    button2.pack()

    #Mode 2 - GETS LINUX SYSTEM DETAILED REPORT
    def detailedreport():

        #" 0 - to provide an lshw detailed report in HTML format"
        root = Tk()
        def htmlreport():
            import time
            time.sleep(1)
            import os
            os.system('gnome-terminal --window --maximize -e "sudo bash htmlsysteminfofirefox.sh"')
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button1 = Button(root, text="LINUX SYSTEM HARDWARE REPORT IN HTML FORMAT ", fg="orange", bg="black", width=55, command=htmlreport)
        button1.pack()
            
        
        #" 1 - to provide a detailed txt report"
        def txtreport():
            import time
            time.sleep(1)
            import os
            os.system('sudo apt-get install inxi')
            import os
            print("----------------------------------------------------------------------")
            import os
            os.system('sudo touch linuxsysteminfo.txt')
            os.system('inxi -Fx | sudo tee -a /home/linuxsysteminfo.txt')
            os.system('clear')
            os.system('cat /home/linuxsysteminfo.txt')
            print("----------------------------------------------------------------------------")
            print("YOU CAN VIEW THE OUTPUT OF THIS FILE AT ANY TIME USING THE FOLLOWING COMMAND")
            print("----------------------------------------------------------------------------")
            print("cat /home/linuxsysteminfo.txt")
            import time
            time.sleep(4)
            os.system('clear')
            print("----------------------------------------------------------------------------")
            print("PRINTING THE OUTPUT OF THE COMMAND TO READ SAVED REPORT...")
            time.sleep(4)
            os.system('clear')
            os.system('cat /home/linuxsysteminfo.txt')
            import time
            time.sleep(2)
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")            
            

        button2 = Button(root, text="LINUX SYSTEM HARDWARE REPORT IN TXT FORMAT", fg="white", bg="black", width=55, command=txtreport)
        button2.pack()

        def systemstatus():
            import time
            time.sleep(1)
            print("----------------------------------------------------------------------")
            import os
            os.system('sudo bash /home/systeminfo.sh')
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button3 = Button(root, text="LINUX SYSTEM ACTUAL STATUS CUSTOMIZED REPORT", fg="yellow", bg="black", width=55, command=systemstatus)
        button3.pack()
            
    
    button3 = Button(root, text="GET LINUX SYSTEM HARDWARE SPECS", fg="green", bg="black", width=50, command=detailedreport)
    button3.pack()

    #Mode 3 - DEBUGS USB PLUG AND PLAY DEVICES
    def plugandplay():
        print("INITIATING THE PLUG AND PLAY DEBUGGING TEST TO CHECK IF DEVICE IS RECOGNIZED...")
        print("----------------------------------------------")
        import time
        time.sleep(3)
        print("WAIT UNTIL THE CURSOR BLINKS UNDER the kernel uevent")
        print("AND THEN CONNECT YOUR USB DEVICE TO THE USB PORT FOR DEBUGGING")
        print("--------------------------------------------------------------")
        import time
        time.sleep(2)
        print("ONCE YOU ARE DONE AND HAVE SAFELY REMOVED YOUR DEVICE")
        import time
        time.sleep(4)
        import os
        os.system('udevadm monitor')
        import time
        time.sleep(2)
        print("------------------------------------------------------")
        print("DEBUGGING TEST HAS FINISHED")
        import time
        time.sleep(2)
        import os
        os.system('clear')
        print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

    
    button4 = Button(root, text="DEBUG USB PLUG AND PLAY DEVICES", fg="orange", bg="black", width=50, command=plugandplay)
    button4.pack()

    #Mode 4 - UPDATE YOUR LINUX SYSTEM

    def updatelinux():
        import os
        os.system('sudo apt-get update')
        import time
        time.sleep(2)
        os.system('clear')
        print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")
    
    button5 = Button(root, text="UPDATE YOUR LINUX SYSTEM", fg="red", bg="black", width=50, command=updatelinux)
    button5.pack()

    #Network options
    def networkoptions():
    
        root = Tk()
        root.title('NETWORK CONTROL OPERATIONS')
        def bandwidthstart():
            import os
            os.system('sudo bash /home/check-speedometer-installed-or-not.sh')


        button1 = Button(root, text="START NETWORK BANDWIDH MEASUREMENT", width=50, fg="black", bg="green", command=bandwidthstart)
        button1.pack()    


        def stopbandwidth():
            print("BANDWIDTH MEASUREMENT STOPPED..")
            import time
            time.sleep(1)
            import os
            os.system('sudo pkill speedometer')
            os.system('exit')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")
        
        button2 = Button(root, text="STOP NETWORK BANDWIDH MEASUREMENT", width=50, fg="black", bg="red", command=stopbandwidth)
        button2.pack()

        #RELOADS ALL NETWORK INTERFACES AND LOGS INFO TO A FILE
        def networkreload():
            import os
            os.system('clear')
            print("ALL NETWORK INTERFACES WILL BE RELOADED..")
            import time
            time.sleep(2)  
            import os
            os.system('sudo bash /home/networkreload.sh')
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button3 = Button(root, text="RELOAD ALL NETWORK INTERFACES AND LOG INFO TO A FILE",width=50, fg="white", bg="black", command=networkreload)
        button3.pack(side="bottom")

        def networkreload2():
            import os
            os.system('clear')
            print("ALL NETWORK INTERFACES WILL BE RELOADED..")
            import time
            time.sleep(2)  
            import os
            os.system('sudo bash /home/networkreload-nolog.sh')
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button3 = Button(root, text="RELOAD ALL NETWORK INTERFACES",width=50, fg="orange", bg="black", command=networkreload2)
        button3.pack(side="bottom")

        #DISPLAYS IFCONFIG AND DNS INFORMATION
        def ipconfigurationanddns():
            print("----------------------------------------------------------------------------------")
            import os
            os.system('ifconfig -a')
            print("----------------------------------------------------------------------------------")
            import os
            os.system('nmcli dev show | grep DNS')
            print("----------------------------------------------------------------------------------")
            raw_input("HIT ENTER TO TERMINATE, OR PRESS ANY OTHER BUTTON...")

        button4 = Button(root, text="DISPLAYS CURRENT IP CONFIGURATION AND DNS SERVERS", width=50, fg="orange", bg="black", command=ipconfigurationanddns)
        button4.pack()
            
        #DISPLAYS CURRENT IP CONFIGURATION AND LOGS INFO TO A FILE
        def ipconfigurationlog():
            print("----------------------------------------------------------------------------------")
            import os
            os.system('sudo rm ipconfiguration.txt')
            os.system('clear')
            import os
            os.system('sudo touch ipconfiguration.txt')
            print("DISPLAYING CURRENT IP CONFIGURATION...")
            print("------------------------------------------------------")
            import time
            time.sleep(2)
            import os
            os.system('ifconfig -a')
            print("------------------------------------------------------")
            import os
            os.system('uptime | sudo tee -a /home/ipconfiguration.txt')
            os.system('echo "------------------------------------------" ')
            os.system('ifconfig | sudo tee -a /home/ipconfiguration.txt')
            os.system('echo "------------------------------------------" ')
            os.system('date | sudo tee -a /home/ipconfiguration.txt')
            os.system('echo "------------------------------------------" ')
            print("ipconfiguration.txt was created, you can see output of this command in this file at any time")
            print("-------------------------------------------------------------------------------------")
            import time
            time.sleep(3)
            print("located at /home directory")
            import time
            time.sleep(2)
            import os
            os.system('gedit /home/ipconfiguration.txt')
            print("-------------------------------------------------------------------------------------")
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button5 = Button(root, text="DISPLAYS CURRENT IP CONFIGURATION AND LOGS INFO TO A FILE", width=50, fg="white", bg="black", command=ipconfigurationlog)
        button5.pack()

        #SCANS YOUR LAN WITH IPSCAN TOOL
        def ipscantool():
            import time
            time.sleep(1)
            import os
            os.system('sudo bash /home/check-ipscan.sh')
            print("--------------------------------------------------------")
            import os
            os.system('clear')
            print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        button6 = Button(root, text="SCAN YOUR LAN WITH IPSCAN TOOL", height=0, width=50, fg="white", bg="black", command=ipscantool)
        button6.pack()

        def accessciscodevice():
            root = Tk()
            root.title('ACCESS A CISCO ROUTER/L3 DEVICE AND OBTAIN NETWORK STATUS')

            def access_ciscodevice_telnet():
                import time
                time.sleep(1)
                import os
                os.system('sudo bash /home/script-to-obtain-logs-from-devices.sh')
                print("--------------------------------------------------------")
                import os
                os.system('clear')
                print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

            button01 = Button(root, text="TELNET - OBTAIN CISCO ROUTER/L3 DEVICE NETWORK STATUS", height=0, width=50, fg="black", bg="white", command=access_ciscodevice_telnet)
            button01.pack()

            def access_ciscodevice_ssh():
                import time
                time.sleep(1)
                import os
                os.system('sudo bash /home/ssh-cisco-access.sh')
                print("--------------------------------------------------------")
                import os
                os.system('clear')
                print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

            button02 = Button(root, text="SSH - OBTAIN CISCO ROUTER/L3 DEVICE NETWORK STATUS", height=0, width=50, fg="black", bg="red", command=access_ciscodevice_ssh)
            button02.pack()
            
        button03 = Button(root, text="ACCESS A CISCO ROUTER/L3 DEVICE AND OBTAIN NETWORK STATUS", height=0, width=70, fg="black", bg="red", command=accessciscodevice)
        button03.pack()

    button3 = Button(root, text="NETWORK CONTROL OPTIONS", fg="black", bg="yellow", width=70, command=networkoptions)
    button3.pack()



button2 = Button(root, text="MODE 1 - MANAGE LINUX SYSTEM WITH THIS BUTTON CONSOLE", fg="orange", bg="black", width=75, command=managelinux)
button2.pack()

def shutdownorrsetart():

    root = Tk()
    root.title('SHUTDOWN OR RESTART LINUX SYSTEM')
    def shutdown():
        import os
        os.system('shutdown now')

    button1 = Button(root, text="SHUTDOWN LINUX SYSTEM NOW", fg="red", bg="black", width=37, command=shutdown)
    button1.pack(side="left")

    def restart():
        import os
        os.system('shutdown -r now')

    button2 = Button(root, text="RESTART LINUX SYSTEM NOW", fg="green", bg="black", width=37, command=restart)
    button2.pack(side="right")

button3 = Button(root, text="SHUTDOWN OR RESTART LINUX SYSTEM NOW", fg="red", bg="black", width=75, command=shutdownorrsetart)
button3.pack()



root.mainloop()
