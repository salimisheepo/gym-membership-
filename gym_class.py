
from member import Member
from trainer import Trainer
from equipment import Equipment

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

    def set_trainer(self, trainer):
        if not isinstance(trainer, Trainer):
            raise TypeError("Only a Trainer can be assigned to a class")
        self.trainer = trainer

    def add_equipment(self, item):
        if not isinstance(item, Equipment):
            raise TypeError("Only Equipment objects can be added")
        if item not in self.equipment:
            self.equipment.append(item)

    def count_members(self):
        total = 0
        for m in self.members:
            total += 1
        return total
