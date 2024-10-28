"""
Finance Calculator

This program allows users to calculate either home loan bond repayments or investment returns.
Users can choose between simple and compound interest for investment calculations. This project
demonstrates effective variable management and control structures, providing a practical tool 
for financial planning and analysis.
"""

# Import the math module for mathematical functions
import math

# Request the type of financial decision from the user
finance = input(
    "Type 'investment' to calculate the interest earned on your investment.\n"
    "Type 'bond' to calculate the monthly repayment on a home loan.\n\n"
    "Enter either 'investment' or 'bond' to proceed: "
).lower()

print()  # Print a blank line for output readability

# Initialize variables for investment/bond calculations
deposit = 0  # Investment amount
rate = 0     # Interest rate
time = 0     # Investment duration in years or loan duration in months
interest_type = ''  # Type of interest for investment calculations
present_value = 0   # Bond amount

# If block for investment financial calculation
if finance == "investment":
    deposit = float(input("Enter the amount of money you would like to invest: "))
    print()

    rate = float(input("At what interest rate would you like the investment to grow? "))
    print()

    time = int(input("For how many years would you like to invest your funds? "))
    print()

    # Request interest type for investment
    interest_type = input("Would you like your investment to be calculated with simple or compound interest? (Enter 'simple' or 'compound'): ").lower()
    print()

    # Calculate and display simple interest
    if interest_type == 'simple':
        final_amount = round(deposit * (1 + rate / 100 * time), 2)
        print(f"The expected return on your investment of R{deposit:.2f} after {time} years at an interest rate of {rate:.2f}% is R{final_amount:.2f}.")

    # Calculate and display compound interest
    elif interest_type == 'compound':
        final_amount = round(deposit * math.pow((1 + rate / 100), time), 2)
        print(f"The expected return on your investment of R{deposit:.2f} after {time} years at an interest rate of {rate:.2f}%, compounded annually, is R{final_amount:.2f}.")
    else:
        print("ERROR: Invalid interest type entered. Please enter 'simple' or 'compound'.")

# Elif block for bond financial calculation
elif finance == "bond":
    present_value = float(input("Enter the bond amount for the property: "))
    print()

    rate = float(input("At what interest rate do you plan to pay off the bond? "))
    print()

    time = float(input("Over how many months will you pay off the bond? "))
    print()

    # Bond repayment calculation
    monthly_payment = round(((rate / 100) / 12 * present_value) / (1 - (1 + (rate / 100) / 12) ** (-time)), 2)
    print(f"The monthly repayment amount for a bond of R{present_value:.2f} paid over a period of {int(time)} months is: R{monthly_payment:.2f}.")

else:
    # Error message for invalid entry
    print("ERROR: You have made an invalid entry. Please enter either 'investment' or 'bond' to proceed.")
