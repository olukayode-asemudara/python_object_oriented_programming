class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Empty collection")
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Empty collection")
        return self.elements[-1]