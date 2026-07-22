class Map:
    def __init__(self):
        self.elements = {}

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def size(self):
        return len(self.elements)

    def put(self, key, value):
        self.elements[key] = value

    def contains(self, key):
        return key in self.elements