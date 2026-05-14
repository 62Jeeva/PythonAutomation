# 1. Bank Account

class bankaccount():
   
   def attribute(self,account_numb,balance):
       self.account_numb =account_numb
       self.__balance = balance
   

   def deposit(self,amount):
       self.__balance = self.__balance +  amount
       print("Amount deposited successfully")
    
   def withdraw(self,amount):
       if amount <= self.__balance:
          self.__balance = self.__balance - amount
          print("Withdrawal of an amount successfully")
        
       else:
           print("Insufficient balance:", self.__balance)
        
   def get_balance(self):
         return self.__balance
              
class savings_account(bankaccount):
    def __init__(self,interest_rate):
        self.interest_rate=interest_rate
        #print("Amount has been deposited successfully")

    def calculate_interest(self):

        interest = self.get_balance() * self.interest_rate/100
        print("Interest has been calculated", interest)

    

class current_account(bankaccount):

    def __init__(self,minimum_balance):
        self.minimum_balance = minimum_balance

    def withdraw_minimum_bank_balance(self,amount):
        if self.get_balance() - amount >= self.minimum_balance:
            current_balance = self. get_balance()
            new_balance = current_balance - amount 

            self._bankaccount__balance = new_balance
            print("withdrawal of an amount is successfull")
        else:
          print("Minimum balance should be maintained")


sav_acc=savings_account(2)
sav_acc.attribute(121,1000)
sav_acc.deposit(5000)
sav_acc.withdraw(7000)
sav_acc.calculate_interest()

cur_acc =current_account(287)
cur_acc.attribute(210,5442)
cur_acc.deposit(4000)
cur_acc.withdraw_minimum_bank_balance(5000)


# 2. Employee Management

class Employee():
    def attribute(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass

class RegularEmployee(Employee):
    def calculate_salary(self,bonus , empid):
        self.empid = empid
        self.bonus = bonus
        total_amount = self.salary + self.bonus
        print("Salary for the Regular employee having emp id -",self.empid,"-", self.name ,"is , Rs.", total_amount , "has been calculated")
  

class ContractEmployee(Employee):
    def calculate_salary(self,working_hours , hourly_salary):
        self.working_hours = working_hours
        self.hourly_salary = hourly_salary

        calculating_wages = self.working_hours * self.hourly_salary
        total_amount = self.salary + calculating_wages
        print("Salary for the contract employee", self.name , 
              "is" ,total_amount , "has been calculated")
    
class Manager(Employee):
    def calculate_salary(self , overtime ,hourly_salary):
        self.hourly_salary = hourly_salary
        self.overtime = overtime
        Ot_wage = self.overtime * self.hourly_salary
        total_amount = self.salary + Ot_wage
        print("Salary for the Manager",self.name," has been calculated", total_amount)
    
Reg_emp = RegularEmployee()
Reg_emp.attribute("Pavithra" , 20000)
Reg_emp.calculate_salary(1500 , 142423)

Cont_emp = ContractEmployee()
Cont_emp.attribute("Ben", 15000)
Cont_emp.calculate_salary(8, 500)


Manager_m1 = Manager()
Manager_m1.attribute("Jack" , 45000)
Manager_m1.calculate_salary(3 , 550)



# 3. Vehicle Rental

class Vehicle():
 def attribute(self,model,rental_rate):
  self.model=model
  self.rental_rate = rental_rate

 def calculate_rental(self):
  pass
  
class car(Vehicle):
 def calculate_rental(self,seater,day):
  self.seater = seater
  self.day=day
  rent = self.rental_rate * day
  print("Rental car has been booked and its charge = " , rent)
 
class Bike(Vehicle):
 def calculate_rental(self,hours):
  self.hours = hours
  bike_rent= self.rental_rate * hours
  print("Bike ride charge for ", hours, "hours is = ", bike_rent)

class truck(Vehicle):
 def calculate_rental(self,days):
  self.days = days
  truck_rent= self.rental_rate * days
  print("Rental charge for truck is  ", truck_rent)

car_c1= car()
car_c1.attribute("Xuv",750)
car_c1.calculate_rental("7-seater",2)

Bike_B1= Bike()
Bike_B1.attribute("Pulsar",200)
Bike_B1. calculate_rental(3)

Truck_T1 = truck()
Truck_T1.attribute("AshokLeyland", 10000)
Truck_T1.calculate_rental(5)
