from person import Person
from membership import BasicMembership, PremiumMembership, VIPMembership


class Member(Person):


    def __init__(self, name, pid, age, phone, membership_type, vip_months=0):
        super().__init__(name, pid, age, phone)
        self.membership = self._create_membership(membership_type, vip_months)
        self.classes = []


    def _create_membership(self, membership_type, vip_months):
        if not isinstance(membership_type, str):
            raise ValueError("Membership type must be text, e.g. 'basic'")
        membership_type = membership_type.strip().lower()
        if membership_type == 'basic':
            return BasicMembership()
        elif membership_type == 'premium':
            return PremiumMembership()
        elif membership_type == 'vip':
            return VIPMembership(vip_months)
        else:
            raise ValueError(f"Unknown membership type: '{membership_type}'. Choose 'basic', 'premium' or 'vip'.")


    def get_fee(self):
        return self.membership.calculate_fee()


    def can_join_class(self):
        return len(self.classes) < self.membership.max_classes()


    def profile_summary(self):
        base = super().profile_summary()
        return f'{base} — {self.membership.plan_name()} member, {len(self.classes)} class(es)'


    def details(self):
        return f'Member: {self.name} | Age: {self.age} | Phone: {self.phone} | Plan: {self.membership.plan_name()} (N${self.get_fee():.2f}/month) | Classes: {len(self.classes)}/{self.membership.max_classes_display()}'
