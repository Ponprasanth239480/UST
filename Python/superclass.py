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
        super().__init__(name,age,gender)
        self.studentid = studentid
        self.fees = fees
    def StudentInfo(self):
        super().personinfo()
        print("studentid: {}".format(self.studentid))
        print("fees: {}".format(self.fees))

stu_obj = student('sri',20,'m',12345,10000)
print('student details :')
print('--------')
stu_obj.StudentInfo()
