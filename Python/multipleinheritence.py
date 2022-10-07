class CurrentDate:
    def __init__ (self,date):
        self.date = date

class CurrentTime:
    def __init__ (self,time):
        self.time = time

class timestamp(CurrentDate,CurrentTime):
    def __init__ (self,date,time):
        CurrentDate.__init__ (self,date)
        CurrentTime.__init__ (self,time)
        DateTime = self.date + ' ' + self.time
        print(DateTime)

datetime1 = timestamp('2022/10/07','10:48:25')
    
