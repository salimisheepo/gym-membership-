
from member import Member

class GymClass:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.members = []
        self.trainer = None
        self.equipment = []

    def add_member(self, person):
        if not isinstance(person, Member):
            raise TypeError("Only members can join classes")
        if person not in self.members:
            self.members.append(person)

    def count_members(self):
        total = 0
        for m in self.members:
            total += 1
        return total
