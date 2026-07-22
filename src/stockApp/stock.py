class Stock:
    def __init__(self, symbol: str, name: str, previous_closing_price: float, current_price: float):
        self.__symbol = "Nothing"
        self.set_symbol(symbol)
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.__current_price = current_price


    def get_symbol(self):
       return self.__symbol

    def set_symbol(self, symbol: str):
        self.__symbol = symbol.upper()

    def get_name(self):
        return self.__name

    def get_previous_closing_price(self):
        return self.__previous_closing_price

    def set_previous_closing_price(self, previous_closing_price: float):
        self.__previous_closing_price = previous_closing_price

    def get_current_price(self):
        return self.__current_price

    def set_current_price(self, current_price: float):
        self.__current_price = current_price