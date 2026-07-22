class Fuel:
    def __init__(self, name, price_per_liter):
        self.name = name
        self.price_per_liter = price_per_liter

class Transaction:
    def __init__(self, product_name, amount_paid, liters_bought):
        self.product_name = product_name
        self.amount_paid = amount_paid
        self.liters_bought = liters_bought

    def display_receipt(self):
        print("==================================")
        print(f"= Product : {self.product_name:<20} =")
        print(f"= Amount paid : #{self.amount_paid:<19.2f} =")
        print(f"= Liters: {self.liters_bought:<19.2f}L =")
        print("= Thank you for your Patronage =")
        print("==================================")