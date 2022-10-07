class Employee:
    def __init__ (self,name,empid):
        self.name = name
        self.empid = empid
    def greet(self):
        print('thanks for joining XYZ company {} !!'.format(self.name))

emp1 = Employee("sri",5847)
print('name :',emp1.name)
print('employee id :',emp1.empid)
emp1.greet()
emp2 = Employee("prasanth",4444)
print('name :',emp2.name)
print('employee id :',emp2.empid)
emp2.greet()

emp2.country = 'india'
print(emp2.country)

emp1.name = "surya"
print('name :',emp1.name)
#attribute error
del (emp1.empid)
#attribute error
#emp1.empid

del emp1
#name error
emp1
