#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
      self.total+= price*quantity 
      self.items.extend([title] * quantity)
      return self.items
    

    def apply_discount(self):
        if self.discount:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.2f}.\n")
        else:
            print("There is no discount to apply.")
    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item['price']
        else:
            print("No transactions to void.")

        if not self.items:
            self.total = 0.0        
    