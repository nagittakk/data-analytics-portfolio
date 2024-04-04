'''
Finance Calculator

This program enables users to effortlessly compute home loan bond repayments or determine investment returns,
with options for simple or compound interest. This project highlights variable management and control structures, 
offering a practical tool for financial planning and analysis variables and control structures.

'''

# import math module to utilise respictive functions
import math

# request financial decision from user
finance = input( "investment - to calculate the amount of interest you'll earn on your investment \n"
		 "bond       - to calculate the amount you'll have to pay on a home loan \n\n"
		 "Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

print(" ") # blank space for output readability

# initial values for 'investment'/'bond' variables, requested from user inside respective if and elif blocks
deposit = 0 # investment 
rate = 0 # investment/bond 
time = 0  # years/months - investment/bond
interest = 0 # investment/bond
present = 0 # bond

# if block for investment financial calculation
if finance == "investment":
    deposit = float(input("Enter the amount of money you would like to invest. (Enter the value only): "))
    print(" ") 

    rate = float(input("At what interest rate would you like the investment to grow?: (Enter the value only): "))
    print(" ")

    time = int(input("For how many years would you like to invest your funds? (Enter the value only): "))
    print(" ")

    interest = input("Would you like your investment to be carried out with simple or compound interest? (Enter 'simple' or 'compound'): ").lower()
    print(" ")

    # nested if-statemnt for 'simple' or 'compund' interest within 'investment' if block
    # simple interest calculation
    if interest == 'simple':        
        print("The expeceted return on your investment of R" + str(round(deposit,2)) + " after " + str(time) + 
              " years at an interest rate of " + str(round(rate,2)) + "% is R" + str(round(deposit * (1 + rate/100 * time),2) )) 

    # compound interest calculation
    else:
        print("The expected return on your investment of R" + str(round(deposit,2)) + " after " + str(int(time)) + 
              " years at an interest rate of " + str(round(rate,2)) + "%, compounded annually, is R" + 
              str(round(deposit * math.pow((1 + rate/100),time),2))) # compound interest calc


# elif block for bond financial calculation			
elif finance == "bond":
    present = float(input("Enter the bond amount for the property. (Enter the value only): "))
    print(" ")

    rate = float(input("At what interest rate do you plan to pay off the bond?: (Enter the value only): "))
    print("")

    time = float(input("Over how many months will you pay off the bond? (Enter the value only): "))
    print(" ")

    # bond repayment formula
    print("The monthly repayment amount for a bond of R" + str(round(present,2)) + " paid over a period of " + str(int(time)) + 
          " months is: R" + str(round(((rate/100)/12 * present ) / (1 - (1 + (rate/100)/12)**(-time)),2))) 
    
else: # neither if or elif block conditions met
    # error message for invalid entry
    print("ERROR: You have made an invalid entry. Please enter either 'investment' or 'bond' to proceed.") 
