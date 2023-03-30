# Program a calculator that performs arithmetic or mathematical calculations

import math # Needed for the mathematical functions (Square Root, Trigonometric Functions, etc.)

# Function aritmetic_calc: Arithmetic calculation +, -, *, /
def arithmetic_calc(c):
  n1 = float(input("Enter a value: "))
  n2 = float(input("Enter another value: "))
  op = input("What operator (Please enter '+', '-', '*', '/'): ")
  print()
  
  # Error Checking on the wrong operation
  while op not in ["+", "-", "*", "/"]:
    op = input("ERROR: Invalid Operator!! Please enter the following operation signs above: ")
    print()

  # Returns the sum
  if op == "+":
    print("Result:", str(n1 + n2))
    
  # Returns the difference
  elif op == "-":
    print("Result:", str(n1 - n2))
    
  # Returns the product
  elif op == "*":
    print("Result:", str(n1 * n2)) 
    
  # Returns the quotient
  elif op == "/":
    print("Result:", str(n1 / n2))


# Function functional_calc: Using math function (Exponents, Square Roots, etc.)
def functional_calc(c):
  n = float(input("Enter a number: "))
  x = int(input("Enter a component (For Exponent Only -> Must be an integer value): "))
  f = input("Enter a math function ('Square Root', 'Exponent', 'Absolute Value', 'Sine', Cosine', 'Tangent', 'Logarithm'): ")
  print()

  # Error Checking on the wrong math function
  while f not in ["Square Root", "Exponent", "Absolute Value", "Sine", "Cosine", "Tangent", "Logarithm"]:
    f = input("ERROR: Not a function!! Please type the following function options above: ")
    print()
    
  # Returns the Square Root 
  if f == "Square Root":
    print("Result:", math.sqrt(n))
    
  # Returns the Exponential Value
  elif f == "Exponent":
    print("Result:", math.pow(n,x))
    
  # Returns the Absolute Value
  elif f == "Absolute Value":
    print("Result:", math.fabs(n))
    
  #Returns the Sine
  elif f == "Sine":
    print("Result:", math.sine(n))
    
  # Returns the Cosine
  elif f == "Cosine":
    print("Result:", math.cosine(n))
    
  # Returns the Tangent
  elif f == "Tangent":
    print("Result:", math.tan(n))
    
  # Returns the Logarithm
  elif f == "Logarithm":
    print("Result:", math.log(n))
    
# Exit Function
def exit(c):
  print("Thank you! Take care.")
 
# Main function   
def main():
  print("Welcome to Calculator!!") 
  choice = input("Please type 'Arithmetic', 'Functional', or 'Exit': ") # Get User Input
  print()
  
  # Error Checking
  while choice not in ['Arithmetic','Functional','Exit']:
    choice = input("ERROR: Incorrect Input!! Please type either 'Arithmetic' or 'Functional': ")
    print()
  
  else:
    while choice != "Exit":
      if choice == "Arithmetic":
        arithmetic_calc(choice)
        print()
        
      elif choice == "Functional":
        functional_calc(choice)
        print()
    
      # User entering another option
      choice = input("What other operation would you like to perform ('Please type 'Arithmetic', 'Functional', or 'Exit'): ")
      print()
      
      # Error Checking
      while choice not in ['Arithmetic','Functional','Exit']:
        choice = input("ERROR: Incorrect Input!! Please type either 'Arithmetic' or 'Functional': ")
        print()
    
  # Exiting the program    
  exit(choice)
  
  
# Main Program
main() 


    
  
    
    
    



  