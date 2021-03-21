
'''
Banking Project 
@author: Sandeep Kumar Jakkaraju

Create Bank, Account and Savings Account Classes
Do deposit and withdraw operations on the account objects.


'''


print("Start !!")

class Bank(object):
    
    def __init__(self,ifsc_code, bank_name, branch_name, loc):
        self.ifsc_code = ifsc_code
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.loc = loc

    def to_String(self):
        print("ifsc="+self.ifsc_code+",name ="+self.bank_name+",branch="+self.branch_name+",loc"+self.loc)    

    

class Customer(object):

    def __init__(self,cust_id, cust_name, address, contact_details):
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.address = address
        self.contact_deatils = contact_details

    def to_String(self):
        print("custid="+self.cust_id+",custname="+self.cust_name+",address="+self.address+",contact="+self.contact_deatils)
        return "custid="+self.cust_id+",custname="+self.cust_name+",address="+self.address+",contact="+self.contact_deatils

class Account(Bank):
    
    def __init__(self,ifsc_code, bank_name, branch_name, loc, customer, balance):
        super().__init__(ifsc_code,bank_name,branch_name,loc)
        self.customer = customer
        self.balance = balance
        
    def to_String(self):
        print("ifsc="+self.ifsc_code+",name ="+self.bank_name+",branch="+self.branch_name+",loc"+self.loc+",customer=["+self.customer.to_String()+"],balance="+str(self.balance))    
        
         
    def get_Account_Info(self):
        print("ifsc="+self.ifsc_code+",name ="+self.bank_name+",branch="+self.branch_name+",loc"+self.loc+",customer=["+self.customer.to_String()+"],balance="+str(self.balance))        
        
    def getBalance(self):
        print("balance="+str(self.balance))
        
        
    def deposit(self,amount):
        self.balance = self.balance+amount
        
    def withdraw(self,amount):
        self.balance = self.balance - amount
        
                
class SavingsAccount(Account):
    def __init__(self,ifsc_code, bank_name, branch_name, loc, customer, balance, smin_balance):
        super().__init__(ifsc_code,bank_name,branch_name,loc,customer,balance)
        self.smin_balance = smin_balance
        
        
    def to_String(self):
        print("ifsc="+self.ifsc_code+",name ="+self.bank_name+",branch="+self.branch_name+",loc"+self.loc+",customer=["+self.customer.to_String()+"],balance="+str(self.balance)+",smin_balance="+str(self.smin_balance))    
            
    def get_Account_Info(self):
        print("ifsc="+self.ifsc_code+",name ="+self.bank_name+",branch="+self.branch_name+",loc"+self.loc+",customer=["+self.customer.to_String()+"],balance="+str(self.balance)+",smin_balance="+str(self.smin_balance))        
    
    def withdraw(self,amount):
        if((self.balance - amount)> self.smin_balance):
            self.balance = self.balance - amount
        else:
            print("Not sufficient balance !!")
    
    
    
account_info = Account("ifsc","hdfc","cyberabad","cyberabad",Customer("cust_id","Sandeep","KPHB","9581570507"),5000)

account_info.get_Account_Info()
account_info.deposit(2000)
account_info.getBalance()
account_info.withdraw(500)
account_info.getBalance()

saving_account_info = SavingsAccount("ifsc","hdfc","cyberabad","cyberabad",Customer("cust_id","Sandeep","KPHB","9581570507"),5000,1000)

saving_account_info.get_Account_Info()
saving_account_info.deposit(2000)
saving_account_info.getBalance()
saving_account_info.withdraw(500)
saving_account_info.getBalance()

