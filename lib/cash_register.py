#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []  # This will store titles as strings
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)  # Add just the title to items
        # Save the last transaction for voiding
        self.last_transaction = {"title": title, "price": price, "quantity": quantity}

    def apply_discount(self):
      if self.discount > 0:
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Ensure the message uses whole dollar amounts when appropriate
        total_display = f"${int(self.total)}" if self.total.is_integer() else f"${self.total:.2f}"
        print(f"After the discount, the total comes to {total_display}.")
      else:
        print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            title = self.last_transaction["title"]
            price = self.last_transaction["price"]
            quantity = self.last_transaction["quantity"]

            # Remove the last transaction's effect on total
            self.total -= price * quantity

            # Remove the last transaction's items
            for _ in range(quantity):
                if title in self.items:
                    self.items.remove(title)

            # Reset total to 0 if items list is empty
            if not self.items:
                self.total = 0.0
