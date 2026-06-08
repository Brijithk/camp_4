#creating a class
#syntax : class:className
class Student:
    #declaring attributes
    name=""
    age=0

#creating objectss
#syntax: objectNmae=classNmae()
objStudent=Student()
objStudent1=Student()
objStudent2=Student()

#assigning values
#syntax:objectNmae.attribute=value
objStudent.name="Tom"
objStudent.age=12
objStudent1.name="jerry"
objStudent1.age=22
objStudent2.name="oggy"
objStudent2.age=22

#printing the values
print("---------1-----------")
print("Name:",objStudent.name)
print("Age:",objStudent.age)
print("---------2-----------")
print("Name:",objStudent1.name)
print("Age:",objStudent1.age)
print("---------3-----------")
print("Name:",objStudent2.name)
print("Age:",objStudent2.age)