from dataclasses import dataclass
from typing import Iterable

@dataclass
class LineItem:
    
    price:int
    quantity:int

    def total_price(self):
        return self.price*self.quantity

def print_totals(items:Iterable[LineItem])->None:
    for item in items:
        print(item.total_price())

def main():
    # Here the iterable is a list.
    items = [LineItem(1,2),LineItem(3,4),LineItem(5,6),]
    print_totals(items)

    # The function expects an Iterable object
    # But the iterable object could be a tuple instead of a list.
    # Therefore the class Iterable acts as an abstraction for any object that is Iterable.

    items = (LineItem(1,2),LineItem(3,4),LineItem(5,6))
    print_totals(items)

if __name__=='__main__':
    main()
