class person:
    def __init__(self,  name , age) :
        self.name =name 
        self.age=age

    def __str__(self) :
        return f"The person name is {self.name} , and he is {self.age} years old "
    
p_1=person("Tobenna" ,30)    
print (p_1)




class Calculator:
    def add(self,a, b):
        return a + b

    def sub( self, a , b):  
        return a - b

    def mul (self, a, b)  :
        return a  * b  
    
    def div (self , a, b):
        if b ==0:
            raise ZeroDivisionError("divisor cant be zero")
        return  a /b
    


#Bank account
class BankAccount:      
    def __init__(self , owner , initial_balance =0 ) :
        self.owner = owner
        self.balance =initial_balance

    def deposit(self , amount ):
        self.balance += amount
        return self.balance
    def withdrawal(self , amount ):
        if amount >self.balance :
            print("insufficient funds")
        self.balance -= amount
        return self.balance
    def display_balance(self) :
        print("Balance:", self.balance)


if __name__ =="__main__" :
    print(Calculator().add(5,6)) 
    print(Calculator().sub(9,2))
    print(Calculator().mul(7,8))
    print(Calculator( ).div(10,4))
    try:
        print(Calculator().div(10,0))
    except Exception as e:
        print(e)
    acc= BankAccount("John Doe" , 1000)
    print(acc.withdrawal(300))
    acc.display_balance()
        

