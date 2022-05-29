# the following is importing functions from the files in the helpers folder 
# addition.py import
import helpers.addition as calc 
from helpers.addition import add

# subtraction.py import
import helpers.subtraction as calc 
from helpers.subtraction import sub

# multiplication.py import
import helpers.multiplication as calc 
from helpers.multiplication import mult

# division.py import
import helpers.division as calc 
from helpers.division import div


# This becomes a "greeting screen" for a user, so when the user runs the file name, the next 5 lines will appear in the terminal. 
print('Welcome to Tyler\'s simple calculator, choose from the following operations:')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')


# this section is a conditional within a conditional, it allows for the user to interact with the "greeting screen" by using the input code to select the operation function (1,2,3,4). 
# The float value is also neccessary so the system doesn't push the numbers together (for example, 4+4=44 or 5*9=59).
# The outer conditional will handle the error if someone enters something that is not 1,2,3,4.
math_type = input('Select your operation: ')
if math_type in ('1','2','3','4'):
  num1 = float(input("enter the first number: "))
  num2 = float(input("enter the second number: "))
  
  # the below conditionals are used to tell the system which function to run based on the user's input
  # math_type is the user input, so it could read "if user input = 1, print the add function" and then would prompt for num1 and num2 values to be filled
  if math_type == '1':
    print('the answer is ', add(num1, num2))
  elif math_type == '2':
    print('the answer is ', sub(num1, num2))
  elif math_type == '3':
    print('the answer is ', mult(num1, num2))
  elif math_type == '4':
    print('the answer is ', div(num1, num2))
  else:
    print('error')
else:
  print('that is not an operation')
  
