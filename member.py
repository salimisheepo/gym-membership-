
from person import Person

class Member(Person):
    def __init__(self, name, pid, age, phone, membership):
        super().__init__(name, pid, age, phone)
        self.membership = membership
        self.classes = []

    def get_fee(self):
        return self.membership.calculate_fee()

    def details(self):
        return f"Member: {self.name}"
