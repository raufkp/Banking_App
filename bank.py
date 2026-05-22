from accounts.signup import customer_signup
import sys
from database import customers # importing customers dictionary from database.py to be used in this file
print(globals()) # This line prints a dictionary representing the current global symbol table. It contains all the global variables, functions, and other objects that are defined in the global scope. This can be useful for inspecting what is available globally in the program.
print(sys.path) # This line prints the list of directories that Python searches for modules when importing. It helps to understand where Python looks for modules and can be useful for debugging import issues.
print(customer_signup("Abdulaziz", 25))
print(customer_signup("Abdulaziz", 25))
print(customers)
