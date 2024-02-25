class Person:
    def __init__(self, first_name, last_name, b_year):
        self.first_name = first_name
        self.last_name = last_name
        self.b_year = b_year

    @property
    def full_name(self):
        return f"{self.first_name} + {self.last_name}"

    @property
    def age(self):
        return 2024 - self.b_year
p1 = Person("Azizbek", "Boltaev", 2004)