loop = 1
while (loop==1):
    import os
    os.system('clear')
    
    print("----------------------------------------------------------------------")

    binary=raw_input("Enter Binary number ( only 0 or 1 ) to convert in Decimal: ")
    int(binary,2)
    print("---------------------------------------------------------------------")
    print("BINARY NUMBER ENTERED IS " + binary)
    print("---------------------------------------------------------------------")
    print"The Decimal Representation of ", binary, " is " , int(binary, 2)
    print"-----------------------------------------------------------------------"
    loop = 2
    while (loop==2):
        import os
        os.system('clear')
        quitornot=raw_input("Convert another number?, if yes enter (y), to exit enter (q): ")
        yes=("y")
        exitprogram=("q")
        if quitornot==yes:
            loop = 1
        elif quitornot==exitprogram:
            break
        else:
            import os
            os.system('clear')
            raw_input("Only enter either letter (y) to continue or (q) to quit program: ")
            loop = 2





    
        

