from database import customers # importing customers dictionary from database.py to be used in this file

def account_validation(account_number):
        if account_number in customers.keys():
            return "account already exist"
        return False