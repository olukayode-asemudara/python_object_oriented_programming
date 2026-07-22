from person import Person
from bmi import BMI

person = Person("Alice", 65, 1.7)
person1 = Person("Kay", 68, 1.78)


bmi = BMI()

print(f"{person.name}'s BMI is {bmi.calculate(person):.2f}")
print(f"{person1.name}'s BMI is {bmi.calculate(person):.2f}")