class Student:
        def __init__(self,name,age):
            self.Name=name
            self.Age=age
        def display(self):
            return f"{self.Name} has age {self.Age}"
        def updateAge(self,new_age):
             self.age=new_age

s1 = Student("Brijith", 22)
s2 = Student("Rahul", 21)
s3 = Student("Anu", 20)

print(s1.display())
print(s2.display())
s2.updateAge(99)
print(s2.display())                                                                                                                                                                                                                                                                                                                                                                                                                                     
print(s3.display())

