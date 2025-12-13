#Some Exercises for inheritance in OOPs...

#Exercise-1 : Basic Single Inheritance
""" 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print(f"{self.name} has salary of {self.salary}$")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def show_details(self):
        print(f"{self.name} is manager with salary {self.salary} in {self.department} department.")

Employee1=Employee("Anjali",500000)   
Employee1.show_details() 
Manager1=Manager("Pushpa",200000000,"Surgical")    
Manager1.show_details()
"""

#Exercise-2 : Multiple Inheritance (Real Test)
"""
class Device:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def device_info(self):
        print(f"Device's brand is {self.brand} and it costs {self.price}$ ") 

class Network:
    def __init__(self,network_type):
        self.network_type=network_type
    def network_info(self):
        print(f"Network's type : {self.network_type}")

class SmartDevice(Device,Network):
    def __init__(self,brand,price,network_type,model):
        Device.__init__(self,brand,price)
        Network.__init__(self,network_type)
        self.model=model
    def full_info(self):
        print(f"Device Brand : {self.brand}\nPrice : {self.price}")  
        print(f"Network's type : {self.network_type}")
        print(f"SmartDevice's Model : {self.model}")

SmartDevice1=SmartDevice("Samsung",50000,"5G","S22")       
SmartDevice1.full_info()
"""

#Exercise-3 : Method Overriding + Polymorphism (REAL TEST)
#Adding logs to clarify the concept of the objects we made below with another way.
"""
from helper import log_setup
log_setup()
from math import pi
import logging
class Shape:
    def __init__(self):
        logging.info("Shape object created...")
        pass
    logging.info("Defined Shape Object...")    
    def area(self):
        logging.info("Printing area of shape...")
        print("Area not defined...")

class Rectangle(Shape):
    logging.info("Defined Rectangle Object...")
    def __init__(self,length,breadth):
        logging.info("Rectangle object created...")
        self.length=length
        self.breadth=breadth
    def area(self):
        logging.info("Printing area of Rectangle...")
        print(f"Area : {self.length*self.breadth}")

class Circle(Shape):
    logging.info("Defined Circle Object...")
    def __init__(self,radius):
        logging.info("Created Circle Object...")
        self.radius=radius
    def area(self):
        logging.info("Printing area of Circle...")
        print(f"Area of Circle : {pi*self.radius**2:.2f}")

objects=[Rectangle(10,20),Circle(7)]
for obj in objects:
    obj.area()
"""

#FINAL EXERCISE — Exercise 4 (This seals inheritance forever)
"""
class Account:
    def __init__(self):
        pass

    def calculate_interest(self):
        raise NotImplementedError("Subclasses must run calculate_interest()") 

class SavingAccount(Account):
    def __init__(self,balance,time,rate=5):
        self.balance=balance
        self.time=time
        self.rate=rate
    def calculate_interest(self):
        print(f"SavingAccount Interest : {(self.balance*self.time*self.rate)/100:.2f}")    

class FixedAccount(Account):
    def __init__(self,balance,time,rate=8):
        self.balance=balance
        self.time=time
        self.rate=rate
    def calculate_interest(self):
        print(f"FixedAccount Interest : {(self.balance*self.time*self.rate)/100:.2f}")

objects=[SavingAccount(1000,2),FixedAccount(1000,2)]
for obj in objects:
    obj.calculate_interest()
"""    












