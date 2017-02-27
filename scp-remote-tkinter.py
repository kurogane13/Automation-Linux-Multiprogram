loop = 60
while (loop==60):

    import os
    os.system('clear')
    print("##################################################################################################################")
    print("SCP TRANSFER MODE ACCESSED")
    print("##################################################################################################################")
    print("THIS PROGRAM TRANSFERS FILES AND/OR FOLDERS TO A REMOTE HOST VIA SCP PROTOCOL")
    print("------------------------------------------------------------------------------------------------------------------")
    userentry=raw_input("ENTER '1' TO START PROGRAM...")
    startprogram=("1")

        
    if userentry==startprogram:

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
                loop = 60
            
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
                    if remotehostuserip==returntomain:
                    
                        import os
                        os.system('clear')
                        print("RETURNING TO MAIN MENU...")
                        import time
                        time.sleep(1)
                        loop = 60

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
                            returntomainmenu1=("0")
                            if remotepath==returntomainmenu1:
                                
                                import os
                                os.system('clear')
                                print("RETURNING TO MAIN MENU...")
                                import time
                                time.sleep(1)

                                loop = 60

                            elif remotepath==backtostep2:

                                loop = 64

                            else:
                                print("-------------------------------------------------------------------------------------------------------------------")
                                step3proccedornot=raw_input("IF YOU NEED TO CORRECT STEP 3, ENTER '3' TO DO SO NOW, IF NO CORRECTIONS ARE NEEDED, HIT ENTER TO RUN SCRIPT NOW: ")
                                backtostep3=("3")
                                returntomainmenu2=("0")
                                if step3proccedornot==returntomainmenu2:

                                    import os
                                    os.system('clear')
                                    print("RETURNING TO MAIN MENU...")
                                    import time
                                    time.sleep(1)

                                    loop = 60
                                    
                                elif step3proccedornot==backtostep3:

                                    loop = 65

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
                                    loop = 60

    else:
        
        import os
        os.system('clear')
        print("------------------------------------------------------------------------------------------------------------------")
        print("PLEASE ONLY ENTER '1' TO START THE PROGRAM...")
        import time
        time.sleep(2)
        import os
        os.system('clear')
        loop = 60
