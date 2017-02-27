loop = 60
while (loop==60):
    import os
    os.system('clear')
    print("##################################################################################################################")
    print("SCP TRANSFER MODE ACCESSED")
    print("##################################################################################################################")
    print("THIS PROGRAM TRANSFERS FILES AND/OR FOLDERS TO A REMOTE HOST VIA SCP PROTOCOL")
    print("------------------------------------------------------------------------------------------------------------------")
    raw_input("HIT ENTER TO START PROGRAM...")
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
    print("STEP 1 - ENTER NOW LOCAL PATH OF FILE/FOLDER TO TRANSFER - ")
    localpath=raw_input("( FORMAT EXAMPLE: local/path/of/file_or_folder ): ")
    print("------------------------------------------------------------------------------------------------------------------")
    print("STEP 2 - ENTER USERNAME@REMOTE_IP_ADDRESS OR USERNAME@REMOTE_HOSTNAME ")
    remotehostuserip=raw_input("FORMAT EXAMPLE: ( USERNAME@REMOTE_IP_ADDRESS ) OR ( USERNAME@REMOTE_HOSTNAME ): ")
    print("------------------------------------------------------------------------------------------------------------------")
    print("STEP 3 - ENTER REMOTE HOST PATH TO PLACE DIRECTORY ")
    remotepath=raw_input("FORMAT EXAMPLE: remote/path/of/file_or_folder): ")
    print("------------------------------------------------------------------------------------------------------------------")
    print("ATTEMPTING TO TRANSFER FILES NOW...")
    print("------------------------------------------------------------------------------------------------------------------")
    space=(" ")
    colon=(":")
    os.system('sudo scp -r' + space + localpath + space + remotehostuserip + colon + remotepath )
    print("------------------------------------------------------------------------------------------------------------------")
    raw_input("SCRIPT EXECUTED, HIT ENTER TO CONTINUE...")
    os.system('clear')
    print("PROGRAM TERMINATED, IF THERE WAS AN ERROR CONNECTING/TRANSFERING THE DATA, PLEASE RECHECK AND CONFIRM REACHABILITY,")
    print("CORRECT CREDENTIALS WERE ENTERED, AND CORRECT SSH ACCESS TO HOST IS CONFIRMED, YOU CAN RE-LAUNCH THIS PROGRAM AGAIN. ")
    print("##################################################################################################################")
    relaunchprogram=raw_input("ENTER '1' TO RELAUNCH THIS PROGRAM OR ENTER '0' TO GET BACK TO MAIN MENU: ")
    relaunch=("1")
    toreturntomainmenu=("0")
    if relaunchprogram==relaunch:
        import os
        os.system('clear')
        print("RELAUNCHING PROGRAM...")
        import time
        time.sleep(1)
        

    elif toreturntomainmenu:
        import os
        os.system('clear')
        print("RETURNING TO MAIN MENU...")
        import time
        time.sleep(1)
        import os
        os.system('clear')
        loop = 0

    else:
        import os
        os.system('clear')
        print("------------------------------------------------------------------------------------------------------------------")
        print("PLEASE ENTER EITHER '1' TO RELAUNCH PROGRAM, OR '0' TO RETURN TO MAIN MENU...")
        import time
        time.sleep(2)
        import os
        os.system('clear')
        loop = 60
        
        
    
    
    
    
    
    
    
    
    
          
    


