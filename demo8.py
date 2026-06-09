class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
    def display_price(self):
        print(getattr(self,"price"))
    def increase_price(self):
        setattr(self,"price",self.price+self.price*(10/100))
        print(getattr(self,"price"))

p1=Product(1,"phone",15000)

p1.display_price()
p1.increase_price()


