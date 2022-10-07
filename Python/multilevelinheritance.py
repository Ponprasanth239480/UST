class Person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print('name: {}'.format(self.name))
        print("age: {}".format(self.age))
        print("gender: {}".format(self.gender))

class employee(Person):
    def __init__ (self,name,age,gender,employeeid,salary):
        Person.__init__(self,name,age,gender)
        self.employeeid = employeeid
        self.salary = salary
    def employeeinfo(self):
        print("employeeid: {}".format(self.employeeid))
        print("salary: {}".format(self.salary))

class fulltime(Person):
    def __init__ (self,name,age,gender,employeeid,salary,experience):
        employee.__init__(self,name,age,gender,employeeid,salary)
        self.experience = experience
    def fulltimeinfo(self):
        print("experience: {}".format(self.experience))
class contractual(Person):
    def __init__ (self,name,age,gender,employeeid,salary,contractexpiry):
        employee.__init__(self,name,age,gender,employeeid,salary)
        self.contractexpiry = contractexpiry
    def contractualinfo(self):
        print("contractexpiry: {}".format(self.contractexpiry))

fulltime_obj = fulltime('sri',20,'m',12345,10000,'3 years')
print('fulltime employee details :')
print('--------')
fulltime_obj.personinfo()
#fulltime_obj.employeeinfo()
fulltime_obj.fulltimeinfo()
contractual_obj = contractual('prasanth',25,'m',98765,20000,'2 years')
print('contractual employee details :')
print('--------')
contractual_obj.personinfo()
#contractual_obj.employeeinfo()
contractual_obj.contractualinfo()


        
    
