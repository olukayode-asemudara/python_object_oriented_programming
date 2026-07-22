class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def size(self):
        return len(self.elements)

    def enqueue(self, element):
        self.elements.append(element)
        return self.size() == len(self.elements)