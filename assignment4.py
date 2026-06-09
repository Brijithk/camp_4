class  BillingSystem:
    def __init__(self,country_name,language,customer_id,billing_date,amount_outstanding):
        self.country_name=country_name
        self.language=language
        self.customer_id=customer_id
        self.billing_date=billing_date
        self.amount_outstanding=amount_outstanding
    def display_details(self):
        print(f"Customer from {self.country_name} of language {self.language} having id {self.customer_id} of date {self.billing_date} having amount {self.amount_outstanding} ")


obj_1=BillingSystem("us","english","101","01/01/2011",9900.018)
obj_2=BillingSystem("japan","japanese","001","01/01/2001",300.01)

obj_1.display_details()
obj_2.display_details()