def f(x):
    return x**2

def summation(lower,upper):
    result = 0
    for i in range(lower,(upper+1)):
	    result = result + f(i)
    return result

def square(lower,upper,n):
    sub = (upper-lower)/n
    result = 0.
    for i in range(n):
        result = result + f(lower+(sub*i))*sub
    return result

def trapezoid(lower,upper,n):
    sub = (upper-lower)/n
    result = 0.
    for i in range(n):
        result = result + (( f(lower+(sub*i)) + f( lower+(sub*(i+1)) ) )/2)*sub
    return result

def intCheck(num):

    check = False
 
    #checks if there is a negative sign and if there is, it's only the first character in the inputed string
    if '-' in num and num[0] == '-':
        i = 1
            #checks if num only contains number characters past the first character
        for i in range(1,len(num)):
            if not(ord(num[i]) >= 48 and ord(num[i]) <= 57):
                break
            else:
                check = True

    else:
        #checks if num only contains number characters
        for i in range(len(num)):
            if not(ord(num[i]) >= 48 and ord(num[i]) <= 57):
                break
            else:
                check = True

    return check

def main():

    switch = True

    while switch == True:
        print()
        method = input("choose method; ‘summation’ or ‘integration’ of f(x): ")

        #Check if the user's input of method is acceptable, if it is not reprompt the user for method
        while method != "summation" and method != "Summation" and method != "integration" and method != "Integration":
            print()
            print("Error, your input is not a valid option")
            method = input("choose method; ‘summation’ or ‘integration’ of f(x): ")

        #Prompt user for lower and upper bounds; (a,b) whole numbers
        print()
        a = input("enter the lower limit of the function: ")
        b = input("enter the upper limit of the function: ")

        #Check if the user's input of bounds is acceptable, if it is not reprompt the user for bounds
        checka = intCheck(a) 
        checkb = intCheck(b)

        while checka == False or checkb == False or int(a)>=int(b):
            print()
            print ("Error, invalid input")
            a = input("enter the lower limit of the function: ")
            b = input("enter the upper limit of the function: ")
            checka = intCheck(a) 
            checkb = intCheck(b)

        a = int(a)
        b = int(b)

        if method == "summation" or method == "Summation":
            print()
            print ("the area under f(x) from x=" + str(a) + " to x=" + str(b) + " using summation is " + str(summation(a,b)))

        if method == "integration" or method == "Integration":

            print()
            n = input("input the number of sub-intervals: ")

            #Check if the user's input of number of sub-intervals is acceptable, if it is not reprompt the user for the number of sub-intervals
            while intCheck(n) == False or int(n)<1:
                print()
                print ("Error, invalid input")
                n = input("input the number of sub-intervals: ")

            n = int(n)

            print()
            intMethod = input("input the method of integration; 'square' or 'trapezoid': ")

            #Check if the user's input of method acceptable, if it is not reprompt the user for method
            while intMethod != "square" and intMethod != "Square" and intMethod != "trapezoid" and intMethod != "Trapezoid":
                print()
                print("Error, your input is not a valid option")
                intMethod = input("input the method of integration; 'square' or 'trapezoid': ")

            if intMethod == "square" or intMethod == "Square":
                print()
                print ("the area under f(x) from x=" + str(a) + " to x=" + str(b) + " using integration with squares was " + str(square(a,b,n)))
                    
            if intMethod == "trapezoid" or intMethod == "Trapezoid":
                print()
                print ("the area under f(x) from x=" + str(a) + " to x=" + str(b) + " using integration with trapezoids was " + str(trapezoid(a,b,n)))
            

        #Prompt user if they want to make another calculation
        print()
        print("would you like to make another calculation?")
        choice = input("yes or no: ")

        #Check if the user's input of their choice to continue or not is acceptable, if it is not reprompt the user for choice
        while choice != "yes" and choice != "Yes" and choice != "no" and choice != "No":
            print()
            print("Error, your input is not a valid option")
            print("would you like to make another calculation?")
            choice = input("yes or no: ")

        if choice == "no" or choice == "No":
            break
 
main()

