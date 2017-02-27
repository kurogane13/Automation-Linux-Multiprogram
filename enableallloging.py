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
              os.system('sudo gedit /home/loggingfromterminal.log')
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
          
    
    
    
