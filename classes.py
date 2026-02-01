# class student:
#     name = "yasin"
#     id = "1"
#     std1 = student()
    
#     print(std1.name)
#     print(std1.id)
    
# class student:
#     name = "yasin"
#     id = "1"
    
#     def student1(abc):
        
#         std1 = student()
#         std2 = student()
    
# class car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
        
        
    
#     def __str__(self):
#         return f"model: {self.model}, Color: {self.color}"    

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#         def area (self):
#             return self.length * self.width   
        
# rectangle = Rectangle(5, 3) 
# print ("Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

# class Student: 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def check_pass(self):
#         if self.mark >= 50:
#             return f"{self.name} is passed."
#         else:
#             return f"{self.namre} is failed."
        
#     student1 = Student("Jhon Doe", 75)
#     print(student1 .check_pass())   
# class Account:
#     def __init__(self, credit, balance):
#         self.credit = credit
#         self.balance = balance
        
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print (f"debited {amount}. Remainin balance: {self.balane}")
#         else:
#             print("Insufficient balance. ")   
            
#     def print_balance(self):
#         print(f"Currenrt balance: {self.balance}")
        
# account = Account(5000, 10000)
# account.debit(2000)
# account.print_balance()   

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def calculate_annual_salary(self):
        return self.salary * 12
    
    def disply_annual_salary(self):
        print(f"Annual salary for {self.name}: {self.calculate_annual_salary()}")   
        
employee = Employee ("Jane Doe", 50000)         
employee.display_annual_salray            