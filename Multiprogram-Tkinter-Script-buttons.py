from Tkinter import *
import tkMessageBox
import Tkinter

print("PRESS A BUTTON FROM THE CONSOLE WINDOW, WAITING FOR INSTRUCTIONS...")


root = Tk()
root.title('CREATED SCRIPTS BUTTON CONSOLE')

#button for telnet

def definetelnet():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Telnet-button-scripts.py"')

buttontelnet = Button(root, text="BUTTON TO RUN TELNET SCRIPTS", fg="white", bg="black", width=55, command=definetelnet)
buttontelnet.grid(row=0, column=0)


#button for ssh

def definessh():
    import os
    os.system('gnome-terminal --window --maximize -e "python /home/Ssh-button-scripts.py"')

buttonssh = Button(root, text="BUTTON TO RUN SSH SCIPTS", fg="yellow", bg="black", width=55, command=definessh)
buttonssh.grid(row=1, column=0)

root.mainloop()
