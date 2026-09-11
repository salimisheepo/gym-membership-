
from person import Person

class Trainer(Person):
    def __init__(self, name, pid, age, phone, speciality):
        super().__init__(name, pid, age, phone)
        self.speciality = speciality

    def details(self):
        return f"Trainer: {self.name}"
