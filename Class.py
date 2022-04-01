class fruit:
    minAge = 1
    maxAge = 120

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


    def __str__(self):
        return f"fruit ({self.name}, {self.age}, {self.country})"

    def __eq__(self, other):
        if isinstance(other, fruit):
            retutn (self.country == other.country)

fruit1 = fruit("Яблоко", 5, "USA")
fruit2 = fruit("Апельсин", 12, "USA")

print(fruit1)
print(fruit2)
print(fruit1.country==fruit2.country)
print(fruit1)