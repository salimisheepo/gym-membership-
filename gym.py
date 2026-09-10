class Gym:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.trainers = []
        self.classes = []
        self.equipment = []

    def add_member(self, member):
        self.members.append(member)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def add_class(self, gym_class):
        self.classes.append(gym_class)

    def add_equipment(self, item):
        self.equipment.append(item)

    def enroll_member(self, member, gym_class):
        gym_class.add_member(member)

    def average_member_age(self):
        # basic algorithm: average
        if len(self.members) == 0:
            return 0
        total_age = 0
        for member in self.members:
            total_age = total_age + member.get_age()
        return total_age / len(self.members)

    def search_by_name(self, name):
        # basic algorithm: searching
        results = []
        everyone = self.members + self.trainers
        for person in everyone:
            if name.lower() in person.get_name().lower():
                results.append(person)
        return results

    def members_in_class(self, class_name):
        for gym_class in self.classes:
            if gym_class.get_name() == class_name:
                return gym_class.count_members()
        return 0

    def total_monthly_revenue(self):
        # polymorphism: get_monthly_fee() calls calculate_fee(), which runs
        # different code depending on each member's Membership subclass
        total = 0
        for member in self.members:
            total = total + member.get_monthly_fee()
        return total

    def members_by_membership_type(self, membership_class_name):
        matches = []
        for member in self.members:
            plan_name = type(member.get_membership()).__name__
            if plan_name == membership_class_name:
                matches.append(member)
        return matches
