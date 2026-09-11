
class Gym:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.trainers = []
        self.classes = []
        self.equipment = []

    def avg_age(self):
        if len(self.members) == 0:
            return 0
        total = 0
        for m in self.members:
            total += m.age
        return total / len(self.members)

    def find_person(self, name):
        found = []
        for p in self.members + self.trainers:
            if name.lower() in p.name.lower():
                found.append(p)
        return found
