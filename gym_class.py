from member import Member


class GymClass:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.trainer = None       # aggregation: set by Trainer.lead_class()
        self.members = []         # aggregation: filled by add_member()
        self.equipment = []       # aggregation: filled by add_equipment()

    def get_name(self):
        return self.name

    def get_schedule(self):
        return self.schedule

    def add_member(self, person):
        # this is the method that checks for a specific object type:
        # only a Member is allowed in, anything else raises an error
        if not isinstance(person, Member):
            raise TypeError("Only a Member object can be enrolled in a class")
        if person not in self.members:
            self.members.append(person)

    def add_equipment(self, item):
        self.equipment.append(item)

    def count_members(self):
        # basic algorithm: counting
        count = 0
        for member in self.members:
            count = count + 1
        return count
