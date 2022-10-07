class Person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print("hello person")

class student(Person):
    def __init__ (self,name,age,gender,studentid,fees):
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees
    def greet(self):
        print("hello student")

stu_obj = student('sri',20,'m',12345,10000)
stu_obj.greet()
person_obj = Person('sri',20,'m')
person_obj.greet()
    
