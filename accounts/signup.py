from .account_generator import account_generator
from .validator import account_validation
from database import customers # importing customers dictionary from database.py to be used in this file

def customer_signup(name, age):
    account_number = account_generator()
    account_check = account_validation(account_number)
    print(account_check)
    if account_check:
        return account_check
    customers[account_number] = ({"name":name, "age":age, })
    return f"account created successfully with account number {account_number}"
    #print(account_number)