#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.price_map = {}

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.price_map[item] = price
    self.price_map[f"{item}_quant"] = quantity
    for i in range(quantity):
      self.items.append(item)

  def apply_discount(self):
    if self.discount:
      self.total = self.total - self.total * self.discount / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    quantity = self.price_map[f"{self.items[-1]}_quant"]
    self.total -= self.price_map[self.items[-1]] * quantity
    del(self.items[-1 * quantity: -1])
