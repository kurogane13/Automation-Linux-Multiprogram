# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import Tkinter

print("PRESS A BUTTON FROM THE CONSOLE WINDOW, WAITING FOR INSTRUCTIONS...")


root = Tk()
root.title('MAIN LINUX BUTTON CONSOLE ADMINISTRATOR')

def regexp():
    import os
    os.system('clear')
    os.system('gnome-terminal --window --maximize -e "python /home/Multiprogram-Tkinter-new-1.py"')
    os.system('sudo bash /home/regular-expression-lookup-Tkinter.sh')

buttonregexp = Button(root, text="FIND A REGULAR EXPRESSION IN A FILE ", fg="green", bg="black", width=55, command=regexp)
buttonregexp.grid(row=6, column=0)

def copyprogram():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/copy-transfer-multiprogram-files-Tkinter.py"')

buttoncopy = Button(root, text="COPY THIS ENTIRE PROGRAM TO A LOCAL OR REMOTE LOCATION", fg="black", bg="blue", width=55, command=copyprogram)
buttoncopy.grid(row=0, column=0)

def copyprogramtomyexternalhd():
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash /home/copyalltomyhardrive.sh"')

buttoncopy = Button(root, text="COPY THE ENTIRE PROGRAM TO MY EXTERNAL DRIVE", fg="white", bg="black", width=55, command=copyprogramtomyexternalhd)
buttoncopy.grid(row=1, column=0)

def multiprogramcolored():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Multiprogram-new-1-server-colored.py"')

buttoncolored = Button(root, text="LAUNCH COLORED COMMAND LINE INTERFACE LINUX MULTIPROGRAM", fg="black", bg="orange", width=55, command=multiprogramcolored)
buttoncolored.grid(row=2, column=0)

def multiprogramblackhwhite():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Multiprogram-new-1-server.py"')

buttonblachwhite = Button(root, text="LAUNCH BLACK-WHITE COMMAND LINE INTERFACE LINUX MULTIPROGRAM", fg="black", bg="white", width=55, command=multiprogramblackhwhite)
buttonblachwhite.grid(row=3, column=0)

def runsgnometerm():
    import os
    os.system('gnome-terminal')
        
    
button2 = Button(root, text="RUN A GNOME TERMINAL", fg="white", bg="black", width=55, command=runsgnometerm)
button2.grid(row=4, column=0)


def filesandfolders():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/files-and-folders-operations.py"')
        
    
buttonfolders = Button(root, text="MANAGE FILES AND FOLDERS", fg="green", bg="black", width=55, command=filesandfolders)
buttonfolders.grid(row=5, column=0)

def scptransfer():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/scp-remote-tkinter.py"')
        
    
scptransfer = Button(root, text="TRANSFER FILES/FOLDERS VIA SCP PROTOCOL", fg="blue", bg="black", width=55, command=scptransfer)
scptransfer.grid(row=7, column=0)

def htmlreport():
    import time
    time.sleep(1)
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash htmlsysteminfofirefox.sh"')
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button3 = Button(root, text="LINUX SYSTEM HARDWARE REPORT IN HTML FORMAT ", fg="orange", bg="black", width=55, command=htmlreport)
button3.grid(row=8, column=0)
            
        
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
    

button4 = Button(root, text="LINUX SYSTEM HARDWARE REPORT IN TXT FORMAT", fg="white", bg="black", width=55, command=txtreport)
button4.grid(row=9, column=0)


def systemstatus():
    import time
    time.sleep(1)
    print("----------------------------------------------------------------------")
    import os
    os.system('sudo bash /home/systeminfo.sh')
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button5 = Button(root, text="LINUX SYSTEM ACTUAL STATUS CUSTOMIZED REPORT", fg="yellow", bg="black", width=55, command=systemstatus)
button5.grid(row=10, column=0)


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


button6 = Button(root, text="DEBUG USB PLUG AND PLAY DEVICES", fg="orange", bg="black", width=55, command=plugandplay)
button6.grid(row=11, column=0)

def htop():
    import time
    time.sleep(1)
    import os
    os.system('clear')
    os.system('sudo bash /home/htop.sh')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button7 = Button(root, text="RUN HTOP TO MONITOR LINUX PROCESSES", fg="blue", bg="black", width=55, command=htop)
button7.grid(row=12, column=0)

#Mode 4 - UPDATE YOUR LINUX SYSTEM

def updatelinux():
    import os
    os.system('sudo apt-get update')
    import time
    time.sleep(2)
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button8 = Button(root, text="UPDATE YOUR LINUX SYSTEM", fg="red", bg="black", width=55, command=updatelinux)
button8.grid(row=15, column=0)



def bandwidthstart():
    import os
    os.system('sudo bash /home/nload-network-monitor.sh')


button9 = Button(root, text="START NETWORK BANDWIDH MEASUREMENT", width=55, fg="black", bg="green", command=bandwidthstart)
button9.grid(row=4, column=1)
    


def stopbandwidth():
    print("BANDWIDTH MEASUREMENT STOPPED..")
    import time
    time.sleep(1)
    import os
    os.system('sudo pkill nload')
    os.system('exit')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button10 = Button(root, text="STOP NETWORK BANDWIDH MEASUREMENT", width=55, fg="black", bg="red", command=stopbandwidth)
button10.grid(row=5, column=1)


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

button11 = Button(root, text="RELOAD ALL NETWORK INTERFACES AND LOG INFO TO A FILE", width=55, fg="black", bg="red", command=networkreload)
button11.grid(row=3, column=1)


#ACCESSES CISCO DEVICES

def ciscosshrunning():
    import os
    os.system('cd /home/')
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash /home/create-ssh-script-to-get-running-config.sh"')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button_ciscosshrunning = Button(root, text="SSH - CREATE SCRIPT FILE TO OBTAIN RUNNING CONFIG", width=55, fg="orange", bg="black", command=ciscosshrunning)
button_ciscosshrunning.grid(row=10, column=1)

def ciscosshcheckrouternetwork():
    import os
    os.system('cd /home/')
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash /home/create-ssh-script-to-check-router-network-status.sh"')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button_ciscocheckrouternetwork = Button(root, text="SSH - CREATE SCRIPT FILE TO CHECK ROUTER AND NETWORK STATUS", width=55, fg="orange", bg="black", command=ciscosshcheckrouternetwork)
button_ciscocheckrouternetwork.grid(row=9, column=1)

def ciscotelnetrunningconfig():
    import os
    os.system('cd /home/')
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash /home/create-telnet-script-to-get-running-config.sh"')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button_ciscocheckrouternetwork = Button(root, text="TELNET - CREATE SCRIPT FILE TO OBTAIN RUNNING CONFIG", width=55, fg="black", bg="yellow", command=ciscotelnetrunningconfig)
button_ciscocheckrouternetwork.grid(row=7, column=1)

def ciscotelnetcheckrouternetwork():
    import os
    os.system('cd /home/')
    import os
    os.system('gnome-terminal --window --maximize -e "sudo bash /home/create-telnet-script-to-check-router-network-status.sh"')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button_ciscocheckrouternetwork = Button(root, text="TELNET - CREATE SCRIPT FILE TO CHECK ROUTER AND NETWORK STATUS", width=55, fg="black", bg="yellow", command=ciscotelnetcheckrouternetwork)
button_ciscocheckrouternetwork.grid(row=8, column=1)


def accessciscotelnet():
    
    import os
    os.system('sudo bash /home/telnet-Tkinter-check-router-network-status.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button12 = Button(root, text="TELNET - TKINTER CISCO ROUTER TO OBTAIN NETWORK STATUS", width=55, fg="black", bg="orange", command=accessciscotelnet)
button12.grid(row=11, column=1)

def accessciscossh():
    
    import os
    os.system('sudo bash /home/ssh-Tkinter-check-router-network-status.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button13 = Button(root, text="SSH - TKINTER CISCO ROUTER TO OBTAIN NETWORK STATUS", width=55, fg="yellow", bg="black", command=accessciscossh)
button13.grid(row=12, column=1)


def telnetrunningconfig():
    
    import os
    os.system('sudo bash /home/telnet-Tkinter-retrieve-running-config.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button14 = Button(root, text="TELNET - TKINTER CISCO ROUTER AND OBTAIN RUNNING CONFIG", width=55, fg="black", bg="orange", command=telnetrunningconfig)
button14.grid(row=13, column=1)

def sshrunningconfig():
    import time
    time.sleep(1)
    import os
    os.system('sudo bash /home/ssh-Tkinter-retrieve-running-config.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button15 = Button(root, text="SSH - TKINTER CISCO ROUTER AND OBTAIN RUNNING CONFIG", width=55, fg="yellow", bg="black", command=sshrunningconfig)
button15.grid(row=14, column=1)

def createbridgeinterfaceswireless():
    
    import os
    os.system('sudo bash /home/create-bridge-interfaces-wireless.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button16 = Button(root, text="CREATE BRIDGE INTERFACES FOR WLAN0", width=55, fg="green", bg="white", command=createbridgeinterfaceswireless)
button16.grid(row=17, column=1)


def deletebridgeinterfaceswireless():
    import time
    time.sleep(1)
    import os
    os.system('sudo bash /home/delete-bridge-interfaces-wireless.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button17 = Button(root, text="DELETE BRIDGE INTERFACES FOR WLAN0", width=55, fg="red", bg="white", command=deletebridgeinterfaceswireless)
button17.grid(row=18, column=1)


def createbridgeinterfaces():
    
    import os
    os.system('sudo bash /home/create-bridge-interfaces.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button16 = Button(root, text="CREATE BRIDGE INTERFACES FOR ETH0", width=55, fg="black", bg="green", command=createbridgeinterfaces)
button16.grid(row=15, column=1)


def deletebridgeinterfaces():
    import time
    time.sleep(1)
    import os
    os.system('sudo bash /home/delete-bridge-interfaces.sh')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button17 = Button(root, text="DELETE BRIDGE INTERFACES FOR ETH0", width=55, fg="black", bg="red", command=deletebridgeinterfaces)
button17.grid(row=16, column=1)




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

button18 = Button(root, text="RELOAD ALL NETWORK INTERFACES", width=55, fg="black", bg="red", command=networkreload2)
button18.grid(row=2, column=1)


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

button19 = Button(root, text="DISPLAYS CURRENT IP CONFIGURATION AND DNS SERVERS", width=55, fg="orange", bg="black", command=ipconfigurationanddns)
button19.grid(row=0, column=1)

    
#DISPLAYS CURRENT IP CONFIGURATION AND LOGS INFO TO A FILE
def ipconfigurationlog():
    print("----------------------------------------------------------------------------------")
    import os
    os.system('sudo rm -r /home/ipconfiguration.txt')
    os.system('clear')
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
    os.system('date | sudo tee -a /home/ipconfiguration.txt')
    os.system('echo "----------------------------------------------------------------" sudo tee -a /home/ipconfiguration.txt ')
    os.system('ifconfig -a | sudo tee -a /home/ipconfiguration.txt')
    os.system('echo "----------------------------------------------------------------" sudo tee -a /home/ipconfiguration.txt ')
    os.system('nmcli dev show | sudo tee -a /home/ipconfiguration.txt')    
    os.system('echo "----------------------------------------------------------------" sudo tee -a /home/ipconfiguration.txt')
    print("ipconfiguration.txt was created, you can see output of this command in this file at any time")
    print("--------------------------------------------------------------------------------------------")
    import time
    time.sleep(3)
    print("located at /home/ directory")
    print("--------------------------------------------------------------------------------------------")
    import time
    time.sleep(1)
    os.system('ls -a -l -t -h /home/ipconfiguration.txt')
    import os
    os.system('gedit /home/ipconfiguration.txt')
    print("-------------------------------------------------------------------------------------")
    raw_input("HIT ENTER TO RETURN TO MAIN MENU..")
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button20 = Button(root, text="DISPLAYS CURRENT IP CONFIGURATION AND LOGS INFO TO A FILE", width=55, fg="white", bg="black", command=ipconfigurationlog)
button20.grid(row=1, column=1)


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

button21 = Button(root, text="SCAN YOUR LAN WITH IPSCAN TOOL", height=0, width=55, fg="silver", bg="black", command=ipscantool)
button21.grid(row=6, column=1)


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

button22 = Button(root, text="SHUTDOWN OR RESTART LINUX SYSTEM NOW", fg="black", bg="red", width=55, command=shutdownorrsetart)
button22.grid(row=19, column=0)


def viewservices():
    import time
    time.sleep(1)
    import os
    os.system('gnome-terminal -e "sudo bash /home/viewservices.sh"')
    print("--------------------------------------------------------")
    import os
    os.system('clear')
    print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

button23 = Button(root, text="VIEW SERVICES STATUS", height=0, width=55, fg="black", bg="yellow", command=viewservices)
button23.grid(row=13, column=0)


def linuxlogs():
    loop = 0
    while (loop==0):
        
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
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")
              

        elif selectlog==auth:

              import os
              os.system('clear')
              os.system('cat /var/log/auth.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")


        elif selectlog==boot:

              import os
              os.system('clear')
              os.system('cat /var/log/boot.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==bootstrap:

              import os
              os.system('clear')
              os.system('cat /var/log/bootstrap.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")
              

        elif selectlog==btmp:

              import os
              os.system('clear')
              os.system('sudo last -f /var/log/btmp')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==dmesg:

              import os
              os.system('clear')
              os.system('dmesg')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")
              

        elif selectlog==dpkg:

              import os
              os.system('clear')
              os.system('cat /var/log/dpkg.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")


        elif selectlog==faillog:

              import os
              os.system('clear')
              os.system('faillog -a')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==kernlog:

              import os
              os.system('clear')
              os.system('cat /var/log/kern.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==last:

              import os
              os.system('clear')
              os.system('last')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==preload:

              import os
              os.system('clear')
              os.system('sudo cat /var/log/preload.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==syslog:

              import os
              os.system('clear')
              os.system('cat /var/log/alternatives.log')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        elif selectlog==wtmp:

              import os
              os.system('clear')
              os.system('last -f /var/log/wtmp')
              print("-----------------------------------------------------------------------------------")
              raw_input("HIT ENTER TO RETURN TO LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE...")
              os.system('clear')
              print("INSTRUCTION EXECUTED, WAITING FOR NEW INSTRUCTION...")

        else:
            import os
            os.system('clear')
            print("------------------------------------------------------------------------------------------------------------------")
            print("PLEASE ENTER ONLY OPTIONS HIGHLITED IN THE MENU, YOU CAN ALSO PRESS ANY OTHER BUTTON FROM THE CONSOLE WINDOW.")
            print("------------------------------------------------------------------------------------------------------------------")
            raw_input("HIT ENTER TO GET BACK TO THE LOGS MENU, OR PRESS ANY OTHER BUTTON FROM THE CONSOLE WINDOW FOR ANOTHER TASK...")
            print("-------------------------------------------------------------------------")
            print("RETURNING TO MENU IN 2 SECONDS...")
            import time
            time.sleep(2)

            loop = 0
          

button24 = Button(root, text="VIEW LINUX LOGS", height=0, width=55, fg="black", bg="green", command=linuxlogs)
button24.grid(row=14, column=0)

def gns3():
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

button25 = Button(root, text="INSTALL GNS3 NETWORK EMULATOR", height=0, width=55, fg="blue", bg="white", command=gns3)
button25.grid(row=19, column=1)



def definetelnet():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Telnet-button-scripts.py"')

buttontelnet = Button(root, text="BUTTON TO RUN TELNET SCRIPTS", fg="white", bg="black", width=55, command=definetelnet)
buttontelnet.grid(row=16, column=0)

def definessh():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Ssh-button-scripts.py"')

buttonssh = Button(root, text="BUTTON TO RUN SSH SCIPTS", fg="yellow", bg="black", width=55, command=definessh)
buttonssh.grid(row=17, column=0)

def anotherinstance():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Multiprogram-Tkinter-new-1.py"')

buttonanotherinstance = Button(root, text="LAUNCH ANOTHER INSTANCE OF THIS CONSOLE", fg="red", bg="black", width=55, command=anotherinstance)
buttonanotherinstance.grid(row=18, column=0)


root.mainloop()





