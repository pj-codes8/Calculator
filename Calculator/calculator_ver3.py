# Creating a calculator using Python 3
# Includes the basic arithmetic functions
# July 13, 2022

# Calculator Menu
print("----- Calculator Menu -----")
print("'a' for addition.")
print("'s' for subtraction.")
print("'m' for multiplication.")
print("'d' for division.")
print("'e' for exponentiation.")
print("'x' to exit the program.")
print("---------------------------")

# User Input for deciding what operation to perform
selection = input("What math operation: ")
selection = selection.lower()
print()

# Looping through the process until the user decides to exit the program
while selection != 'x':
    
    # User Input for Calculating two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print()
    
    # Outputs the addition of the two numbers
    if selection == 'a':
        total = num1 + num2
        print("Total: " + str(total))
        print()
        
    # Outputs the subtraction of the two numbers
    elif selection == 's':
        total = num1 - num2
        print("Total: " + str(total))
        print()
        
    # Outputs the multiplication of the two numbers
    elif selection == 'm':
        total = num1 * num2
        print("Total: " + str(total))
        print()
        
    # Outputs the division of the two numbers
    elif selection == 'd':
        total = num1 / num2
        print("Total: " + str(total))
        print()
        
    # Outputs the exponentiation of the first number as the base to the power 
    # of the second number
    elif selection == 'e':
        total = num1 ** num2
        print("Total: " + str(total))
        print()
        
    # Outputs an error for typing the wrong keyword
    else:
        print("Invalid Input. Please try again")
        print()
        
    # Get user input to run the program again  
    selection = input("What else would you like to do: ")
    selection = selection.lower()
    print()
     
    # Error Checking
    while selection not in ['a', 's', 'm', 'd', 'e', 'x']:
        selection = input("ERROR: Incorrect Input!! Please type 'a', 's', 'm', 'd', 'e', or 'x' to continue: ")
        selection = selection.lower()
        print()
 
# Exiting the program       
print("You chose to exit the program. Have a good day.")
    



