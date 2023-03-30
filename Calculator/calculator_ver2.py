# Program a Simple/Complex Graphing Calculator

# Math Module to add Trigonometric, Absolute Value, Square Root, and Logarithmic Functions
import math

# Calculator using numbers and operators

# Welcome menu
def welcome():
  print("------- Python Calculator ----------")
  print("Press 'b' to perform the basic 4 operational calculation.")
  print("Press 'f' to perform the a functional calculation.")
  print("Press 'h' to show this menu again.")
  print("Press 'x' to exit the program.")
  print()

# Four operator calculator function
def basic_calculation(s):
  
  # User Input for the first and second numbers
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  
  # Selecting what type of operator
  op = input("What operator ('+','-','*','/'): ")
  print()

  # Addition
  if op == "+":
    print(num1 + num2)
    
  # Subtraction
  elif op == "-":
    print(num1 - num2)
  
  # Multiplication
  elif op == "*":
    print(num1 * num2)
    
  # Division
  elif op == "/":
    print(num1 / num2)
     
  # Invalid Operator
  else:
    print("Not an operatable calculation.") 
    

# Using mathematical function (Exponents, Square Roots, etc.)
def functional_calculation(s):

  # User Input
  number = int(input("Enter a number: "))
  print()
  
  # Menu Display
  print("--- Math Function Menu ---")
  print("Please type the following: ")
  print("'Square Root'")
  print("'Absolute Value")
  print("'Trig Sine'")
  print("'Trig Cosine'")
  print("'Trig Tangent'")
  print("'Log Base 2'")
  print()
  
  # User Input for function type
  function_type = input("Enter a math function: ")
  print()
  
  # Square root
  if function_type == "Square Root":
    print(math.sqrt(number))
    print()
    
  # Absolute Value
  elif function_type == "Absolute Value":
    print(math.fabs(number))
    print()
    
  # Sine Value (Exact) 
  elif function_type == "Trig Sine":
    print(math.sin(number))
    print()
    
  # Cosine Value (Exact)
  elif function_type == "Trig Cosine":
    print(math.cos(number))
    print()
    
  # Tangent Value
  elif function_type == "Trig Tangent":
    print(math.tan(number))
    print()
    
  # Logarithmic Value with Base 2
  elif function_type == "Log Base 2":
    print(math.log2(number))
    print()
    
  # Invalid Input
  else:
    print("Not an operatable calculation.")
    print()
      
      
# Show the menu again
def help(s):
  welcome()
  print()
  
# Exiting the program
def exit(s):
  print("You chose to exit this program. Have a good day.")
  
      
# ------- MAIN --------

# Display welcome menu
welcome()

# User Input from welcome menu
selection = input("Type the following keys: ")
print()

# Error Check if user did not enter the following keys
while selection not in ['b', 'f', 'h', 'x']:
  selection = input("ERROR: Incorrect input!!! Please enter 'b','f', 'h', or 'x' to continue: ")
  print()
  
# Calls the functions if the user 
else: 
  while selection != "x":
    
    # Performing the 4 operational calculation
    if selection == "b":
      basic_calculation(selection)
      print()
      
    # Performing the functional calculation (Square Root, Sin(x), etc.)
    elif selection == "f":
      functional_calculation(selection)
      print()
      
    # Display the welcome menu again
    elif selection == "h":
      help(selection)
      
    # User Input to either enter another calculation or exit
    selection = input("What else would you like to do: ")
    print()
    
    # Error Checking
    while selection not in ['b', 'f', 'h', 'x']:
      selection = input("ERROR: Incorrect input!!! Please eneter 'b','f', 'h', or 'x' to continue: ")
      print()
    
# Exiting the program  
exit(selection)

