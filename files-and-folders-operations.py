loop = 40
while (loop==40):
    import os
    os.system('clear')
    print("***************************************************************************")
    print("FILES AND FOLDERS MENU ACCESSED..")
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

        
            
