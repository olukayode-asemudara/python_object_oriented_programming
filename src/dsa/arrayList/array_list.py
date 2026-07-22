class ArrayList:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def size(self):
        return len(self.elements)

    def get(self, index):
        return self.elements[index]

    def add(self, number):
        self.elements.append(number)

    def set(self, index, number):
        self.elements[index] = number

    def contains(self, number):
        return number in self.elements

    def get_first(self):
        if self.is_empty():
            raise ValueError("ArrayList is empty")
        return self.elements[0]

    def get_last(self):
        if self.is_empty():
            raise ValueError("ArrayList is empty")
        return self.elements[-1]

    def index_of(self, number):
        try:
            return self.elements.index(number)
        except ValueError:
            return -1