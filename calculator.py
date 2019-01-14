choice2 = "yes"
choice1 = "yes"

while (choice2 == "yes") or (choice2 == "Yes"):

    choice1 = "yes"
    
    mode = str(input("please choose a mode: programmer or scientific "))

    while ((mode != "programmer") and (mode != "Programmer") and (mode != "scientific") and (mode != "Scientific")):
        print("that is not a valid mode")
        mode = str(input("please choose a mode: programmer or scientific "))
        
    #programmer mode        
    if ((mode == "programmer") or (mode == "Programmer")):

        while choice1 == "yes":
            
                
            dec = str(input("please enter any unsigned integer to be convert to binary: "))
            
            #check for floats
            while '.' in dec:
                print("please input a integer not a float")
                dec = str(input("please enter any unsigned integer to be convert to binary: "))

            #check for any characters in the input other than numbers
            i = 0
            j = 0
                    
            while j==0:
                if ((dec[i] >= chr(48)) and (dec[i] <= chr(57))):
                    i = i+1
                    if i == len(dec):
                        break
                else:
                    print("invalid input")
                    dec = list(input("please enter any unsigned integer to be convert to binary: "))
                    i = 0

            k = ""
            l = 0
            while l < len(dec):
                k = k + str(dec[l])
                l = l+1
            
            dec = int(k)
            
            #check if user input is negative and if it is reprompt user for input
            while (dec < 0) or (type(dec) == str):
                print("invalid input")
                dec = int(input("please enter any unsigned integer to be convert to binary: "))
        
            #find max exponent of base 2 for given decimal 
            if dec == 0.0:
                print(str(dec),"is equal to",str(int(dec)),"in binary")

            else:
                ex = 0
                test = 0
                switch = 0
                while switch == 0:
                    test = dec/((2)**(ex))
                    if test > 1:
                        ex = ex+1
                    else:
                        switch = 1
                dec = int(dec)
                inc = int(dec)
                ex = int(ex-1)    
                list = []*ex
     
                #convert integer input to to single binary string of numbers to print           
                bin = ""
                while inc > 0:
                    if (inc >= 2**(ex)):
                        bin = bin + "1"
                        inc = inc - (2**(ex))
                    else:
                        bin = bin + "0"
                    ex = ex-1
            
                print(str(dec),"is equal to",bin,"in binary")

            #user choice to either do another calculation in current mode  
            choice1 = str(input("would you like to run another conversion in programmer mode?: yes or no "))

            while ((choice1 != "yes") and (choice1 != "no")):
                print("that is not a valid input")
                choice1 = str(input("would you like to run another programmer calculation?: yes or no "))
                
            if (choice1 == "no"):
                choice2 = str(input("would you like to run a calculation in another mode?: yes or no "))
                
    #scientific mode   
    elif ((mode == "scientific") or (mode == "Scientific")):

        while choice1 == "yes":
        
            prob = str(input("please enter a calculation restricted to two numbers and one operator of the following ('/' '*' '+' '-' '**') seperated by spaces: "))

            while (('/' not in prob) and ('*' not in prob) and ('+' not in prob) and ('-' not in prob)):
                print("that is not a valid calculation")
                prob = str(input("please enter a calculation restricted to two numbers and one operator of the following ('/' '*' '+' '-' '**') all seperated by spaces: "))

            while (' ' not in prob):
                print("please include spaces between your operands and operator")
                prob = str(input("please enter a calculation restricted to two numbers and one operator of the following ('/' '*' '+' '-' '**') all seperated by spaces: "))

            calc = list(map(str,prob.split(" ")))
            op = calc[1]
        
            while ((op != '/') and (op != '*')  and (op != '+') and (op != '-') and (op != '**')):
                print("that is not a valid calculation")
                prob = str(input("please enter a calculation restricted to two numbers and one operator of the following ('/' '*' '+' '-' '**') seperated by spaces: "))

            calc = list(map(str,prob.split(" ")))
            a = (calc[0])
            b = (calc[2])

            i = 0
            while i == 0:
                if (a >= chr(48)) and (a <= chr(57)) and (b >= chr(48)) and (b <= chr(57)):
                    i = 1
                else:
                    print("that is not a valid calculation")
                    prob = str(input("please enter a calculation restricted to two numbers and one operator of the following ('/' '*' '+' '-' '**') all seperated by spaces: "))
                    calc = list(map(str,prob.split(" ")))
                    a = (calc[0])
                    b = (calc[2])

            

            calc = list(map(str,prob.split(" ")))
            a = float(calc[0])
            b = float(calc[2])
            op = calc[1]
            answer = 0.

            if op == "/":
                answer = (a/b)

            elif op == "*":
                answer = (a*b)

            elif op == "+":
                answer = (a+b)

            elif op == "-":
                answer = (a-b)

            elif op == "**":
                answer = (a**(b))

            print(prob," ",str(answer))

            choice1 = str(input("would you like to run another calculation in scientific mode?: yes or no "))

            while (((choice1 != "yes") and (choice1 != "Yes")) and ((choice1 != "no") and (choice1 != "No"))):
                print("that is not a valid input")
                choice1 = str(input("would you like to run another calculation in scientific mode?: yes or no "))
                
            if ((choice1 == "no") or (choice1 == "No")):
                choice2 = str(input("would you like to run a calculation in another mode?: yes or no "))


    
