from person import Person


class Member(Person):
    def __init__(self, name, id_number, age, phone, membership):
        super().__init__(name, id_number, age, phone)
        # composition: the Member creates and owns this Membership object
        self.membership = membership
        self.enrolled_classes = []

    def get_membership(self):
        return self.membership

    def print_info(self):
        plan_name = type(self.membership).__name__
        return "Member: " + self.name + " (ID " + self.id_number + "), age " + str(self.age) + ", plan: " + plan_name

    def get_monthly_fee(self):
        # polymorphism: calculate_fee() runs different code depending on
        # which Membership subclass this member actually has
        return self.membership.calculate_fee()

    def book_class(self, gym_class):
        gym_class.add_member(self)
        if gym_class not in self.enrolled_classes:
            self.enrolled_classes.append(gym_class)
