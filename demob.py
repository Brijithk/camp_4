class Author:
    def __init__(self,author_name,country):
        self.author_name=author_name
        self.country=country
    def display_author(self):
        print("Authore name :",self.author_name)
        print("Country :",self.country)

class Book(Author):
    def __init__(self, author_name, country,title,price):
        super().__init__(author_name, country)
        self.titl=title
        self.price=price
    
def display_books(self):
    self.display_author()
    print("Book title :",self.title)
    print("Book Price",self.price)