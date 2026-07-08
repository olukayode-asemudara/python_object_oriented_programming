class Inventory:
    def __init__(self):
        self.__stock = {}

    def add_item(self, item):
        self.__stock[item.name] = item

    def get_item(self, name):
        return self.__stock.get(name)

    def check_availability(self, item):
        inventory_item = self.get_item(item.name)
        if inventory_item is None:
            return False
        return inventory_item.quantity >= item.quantity

    def remove_stock(self, item):
        if not self.check_availability(item):
            raise ValueError(f"Insufficient stock for {item.name}")
        self.__stock[item.name].quantity -= item.quantity