
from person import Person
from membership import BasicMembership, PremiumMembership, VIPMembership

class Member(Person):
    def __init__(self, name, pid, age, phone, membership_type, vip_months=0):
        super().__init__(name, pid, age, phone)
        self.membership = self._create_membership(membership_type, vip_months)
        self.classes = []

    def _create_membership(self, membership_type, vip_months):
        membership_type = membership_type.lower()
        if membership_type == "basic":
            return BasicMembership()
        elif membership_type == "premium":
            return PremiumMembership()
        elif membership_type == "vip":
            return VIPMembership(vip_months)
        else:
            raise ValueError(f"Unknown membership type: {membership_type}")

    def get_fee(self):
        return self.membership.calculate_fee()

    def can_join_class(self):
        return len(self.classes) < self.membership.max_classes()

    def details(self):
        return f"Member: {self.name}"
