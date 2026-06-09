class Employee:
    def login(self):
        print("logged in")
    def logout(self):
        print("logged out") 

class Manager(Employee):
    def work(self):
        print("manager is managing team") 

objManager=Manager()
objManager.login()  
objManager.logout()
objManager.work()