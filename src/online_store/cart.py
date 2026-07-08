class Cart:
    def __init__(self, items, id: str):
        self.__items = items
        self.__id = id

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        self.__items.remove(item)

    def checkout(self, inventory):
        total = 0

        for item in self.__items:
            inventory.remove_stock(item)
            total += item.subtotal()

        return {
            "cart_id": self.__id,
            "items": self.__items,
            "total": total
        }