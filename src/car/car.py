class Car:

    make = None
    model = None
    year = None
    color = None

    # car constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Driving")

    def stop(self):
        print("Stopping")