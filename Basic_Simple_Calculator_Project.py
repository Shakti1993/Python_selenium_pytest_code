##############Simple Calculator#######################

while True:
    print("\n=====================================\n") ##this will add new line after each loop

    input1 = input('Enter a number or type Stop to close the Calc: ') 

    if input1 == "stop": 
        break     ## this will stop the calculator once stop is printed
    elif not input1.isdigit(): ## if digit not printed 
        print("This is not a valid number")  
        continue     ##back to loop
    else:
        number1 = int(input1) ## 1st input
    
    Cal_Op = input('Enter the operation(+, -, /, *, %):-> ') ##Maths Equation

    input2 = input("Enter the second number: ")  
    if not input2.isdigit(): 
        print("This is not a valid number.")
        continue     ##Back to loop
    else:
        number2 = int(input2)  ##2nd Input
    
    if Cal_Op =='+':
        ans = number1 + number2
    elif Cal_Op == '-':
        ans= number1 - number2
    elif Cal_Op =='/':
        ans = number1 / number2
    elif Cal_Op =='*':
        ans = number1 * number2
    elif Cal_Op =='%':
        ans = number1 % number2
    else:
        print('This is not a valid Operation')
        continue
    print(number1,Cal_Op,number2,'=',ans)
    
