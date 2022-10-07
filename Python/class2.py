import datetime
class Person:
    def __init__ (self,name,surname,birthdate,address,phone,email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
        self.email = email
    def age (self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year

        if today < datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            age -= 1
            return age

person = Person('sri','p',datetime.date(2001,11,13),'coimbatore','498484','sri@example.com')
print(person.name)
print(person.surname)
print(person.address)
print(person.phone)
print(person.email)
print(person.age())

    
