"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

class PayType(Enum):
    Hourly = "contract"
    Salary = "monthly salary"
    
class CommissionType(Enum):
    Bonus = "bonus commission"
    Contract = "commission"
    
class Pay:
    def __init__(self, typeofpay, pay, hours = None):
        self.typeofpay = typeofpay
        self.pay = pay
        self.hours = hours
        
    def get_contract_pay(self):
        if(self.typeofpay == PayType.Hourly):
            return self.pay * self.hours
        else:
            return self.pay
    
    def __str__(self):
        if(self.typeofpay == PayType.Hourly):
            return "contract of "+ str(self.hours) + " hours at " + str(self.pay) + "/hour"
        else:
            return "monthly salary of " + str(self.pay) 
            
class Commission:
    def __init__(self, typeofcommission, pay, contracts = None):
        self.typeofcommision = typeofcommission
        self.pay = pay
        self.contracts = contracts
        
    def get_commission_pay(self):
        if(self.typeofcommision == CommissionType.Bonus):
            return self.pay
        else:
            return self.pay*self.contracts
        
    def __str__(self):
        if(self.typeofcommision == CommissionType.Bonus):
            return "bonus commission of " + str(self.pay) 
        else:
            return "commission for " + str(self.contracts) + " contract(s) at " + str(self.pay) + "/contract"
            
    
class Employee:
    def __init__(self, name, pay, commission):
        self.name = name
        self.pay = pay
        self.commission = commission

    def get_pay(self):
        pay = 0
        if(self.commission is not None):
            pay += self.commission.get_commission_pay()
        pay += self.pay.get_contract_pay()
        return pay

    def __str__(self):
        description = "" + self.name
        description += " works on a "
        description += str(self.pay)
        if(self.commission is not None):
            description += " and receives a " + str(self.commission)
        description += ".  Their total pay is " + str(self.get_pay()) + "."
        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
contract = Pay(PayType.Salary, 4000)
billie = Employee('Billie', contract, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
contract = Pay(PayType.Hourly, 25, 100)
charlie = Employee('Charlie', contract, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
contract = Pay(PayType.Salary, 3000)
commission = Commission(CommissionType.Contract, 200, 4)
renee = Employee('Renee', contract, commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
contract = Pay(PayType.Hourly, 25, 150)
commission = Commission(CommissionType.Contract, 220, 3)
jan = Employee('Jan', contract, commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
contract = Pay(PayType.Salary, 2000)
commission = Commission(CommissionType.Bonus, 1500)
robbie = Employee('Robbie', contract, commission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
contract = Pay(PayType.Hourly, 30, 120)
commission = Commission(CommissionType.Bonus, 600)
ariel = Employee('Ariel', contract, commission)
