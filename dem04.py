class Employee:
    name=""
    age=0
    def display_details(self):
        return f"{self.name}{self.age}"

objemp=Employee()
objemp.name="tom"
objemp.age=10

print(f'{objemp.name} is {objemp.age} years old')
print(f'employee details:{objemp.display_details()}')

