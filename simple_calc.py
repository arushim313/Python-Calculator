## Making a simple calc as a part of execise

''' Let us take the input from the user first
We will take three inputs from the user. 
The first is num one which is the first number 
The second input is num two which is the second number
The third we will ask them to enter a character for the arithmetic
calculation they want to conduct. 
'''


''' Now that we have taken the input we will write the code for the calculations.'''

run_again = "Y" ## The checker to keep running the calculator until user enters something else. 
while run_again == "Y": ## The while loop to keep running the calc
    ## Then we take the input from the user for the two numbers
    num1 =int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    ## Then take the operation that wants ti be conducted on the two numbers
    calc_op = input("Enter of the the following symbols for the calculation: +, -, x, /: ")

    ## Now based on the symbol selected do the calculation

    if calc_op == "+":
        print(f"The sum is {num1+num2}")
    elif calc_op == "-":
        print(f"The difference is {num1-num2}")
    elif calc_op == "x":
        print(f"The product is {num1*num2}")
    else:
        if num2 == 0:
            print("Since the second number is 0, the result will be invalid")
        else:
            print(f"The fraction is {num1//num2}")
    ## Now confirm from the user if they want to use the calculator again
    run_again = input("Do you want to use the calculator again? Y/N: ")      
  
print("I hope you are happy with the results!")



