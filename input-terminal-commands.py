
loop = 120
while (loop==120):
    print("###################################################################################################")
    print("LINUX TERMINAL MODE ACCESSED -")
    print("-----------------------------------------------------------------------------------------------------")
    print("'history' - TO ENABLE LOGGING ALL ENTERED INPUT FOR THIS SESSION - ")
    print("NOTE: THE SECOND TIME YOU ENTER IT, YOU WILL SEE YOUR FIRST SAVED COMMAND - ")
    loop = 121
    while (loop==121):
        
        print("-----------------------------------------------------------------------------------------------------")
        print("'0' - TO GET BACK TO MAIN MENU - ")
        print("-----------------------------------------------------------------------------------------------------")
        inputterminalcommands=raw_input("ENTER LINUX TERMINAL COMMAND HERE: ")
        backtomainmenufrominputcommand=("0")
        enteredcommand=inputterminalcommands
        enteredcommandpipe=("|")
        commandafterpipe=inputterminalcommands
        historylog=("history")
        space=(" ")
        
        if inputterminalcommands==backtomainmenufrominputcommand:
            break

        elif inputterminalcommands==enteredcommandpipe:
            
            import os
            os.system(' ' + enteredcommand + space + enteredcommandpipe + space + commandafterpipe )
            loop = 121

        elif inputterminalcommands==historylog:
            print("-----------------------------------------------------------------------------------------------------")
            print("SHOWING HISTORY FILE FOR THIS SESSION: ")
            print("-----------------------------------------------------------------------------------------------------")
            import readline
            for i in range(readline.get_current_history_length()):
                print readline.get_history_item((i + 1))
                loop = 121

        else:
            
            import os
            os.system(' ' + enteredcommand )
            
            loop = 121
        
