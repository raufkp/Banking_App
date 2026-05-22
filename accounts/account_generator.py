from database import customers 

def account_generator():
    if len(customers) == 0:
        return 1001
    return max(customers.keys())+1