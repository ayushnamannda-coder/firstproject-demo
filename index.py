#create student class that takes name & marks of 3 subject as arguments in constructor.
#then, create a method to print the average

class Student:

    def __init__(self,Name,Marks):
        self.name = Name
        self.marks = Marks

    def avg(self):
        sum = 0
        for i in self.marks:
            sum+=i
        print(self.name,"avarage marks is:",sum/3)

s1 = Student("Ayush",[88,98,78])

s1.avg()