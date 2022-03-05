import csv

class Item:
    
    pay_rate = 0.8 # the pay rate after 20% discount
    all = []
    
    def __init__(self,name:str,price:float,quantity=0):
        
        ##Run validations to received arguments
        assert price >=0, f"Price {price} is not greater than equal to zero."
        assert quantity >=0, f"Quantity {quantity} is not greater than equal to zero."
        
        ## Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        ## Append instance to list
        Item.all.append(self)

    def calculate_total_price(self):
        return(self.price*self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        
        with open('data/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            #print(item)
            Item(name=item.get('name'),price=float(item.get('price')),quantity=float(item.get('quantity')))
    
    @staticmethod
    def is_integer(num):
        # We will count the floats that have .0 as integer.
        # eg. 5.0 is integer
        if isinstance(num,float):
            # COunt out the number of floats that are .0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"

