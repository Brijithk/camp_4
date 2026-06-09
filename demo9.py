class Employee:
    def __init__(self,name,email,designation):
        self.name=name
        self.email=email
        self.designation=designation
    def display(self):
        print(f"name : {getattr(self,"name")} email : {getattr(self,"email")} designation : {getattr(self,"designation")}")
    def add_update(self,attr,value):
        setattr(self,attr,value)
        print("The updated object is :")
        print(f"name : {getattr(self,"name")} email : {getattr(self,"email")} designation : {getattr(self,"designation")}")
    def check(self,attr):
        if hasattr(self,attr):
            print("The entered attribute is present")
        else:
            print("The entered attribute is not present")
    def delete(self,attr):
        delattr(self,attr)
        print("The attribute is deleted")
emp1=Employee("brijith","bk@gmail.com","developer")
loop=True
while loop:
    print("1.Display Attribute")
    print("2.Add/Update Attribute")
    print("3.check Attribute")
    print("4.Delete Attribute")
    print("5.Exit")
    user_choice=int(input("Enter a number between 1 to 4 \n"))

    match (user_choice):
        case 1:
            print("displaying the entire object :")
            emp1.display()
        case 2:
            print("----------------")
            attr=input("enter a attribute \n")
            value=input("enter a value \n")
            emp1.add_update(attr,value)
        case 3:
            print("----------------")
            attr=input("enter a attribute \n")
            emp1.check(attr)   
        case 4:
            print("----------------")
            attr=input("Enter the attribute to be deleted")
            emp1.delete(attr)
        case 5:
            print("exiting...")
            loop=False



