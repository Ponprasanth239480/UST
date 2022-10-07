class Person:
    def __init__ (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):
        print('name: {}'.format(self.name))
        print("age: {}".format(self.age))
        print("gender: {}".format(self.gender))

class student(Person):
    def __init__ (self,name,age,gender,studentid,fees):
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees
    def StudentInfo(self):
        print("studentid: {}".format(self.studentid))
        print("fees: {}".format(self.fees))

class teacher(Person):
    def __init__ (self,name,age,gender,employeeid,salary):
        Person.__init__(self,name,age,gender)
        self.employeeid = employeeid
        self.salary = salary
    def TeacherInfo(self):
        print("employeeid: {}".format(self.employeeid))
        print("salary: {}".format(self.salary))

stu_obj = student('sri',20,'m',12345,10000)
teacher_obj = teacher('prasanth',25,'m',98765,20000)
print('student details :')
print('--------')
stu_obj.personinfo()
stu_obj.StudentInfo()
print('Teacher details :')
print('--------')
teacher_obj.personinfo()
teacher_obj.TeacherInfo()



        
    
