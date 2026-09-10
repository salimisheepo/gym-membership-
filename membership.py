from abc import ABC, abstractmethod


class Membership(ABC):
    def __init__(self, monthly_fee):
        self.monthly_fee = monthly_fee

    def get_monthly_fee(self):
        return self.monthly_fee

    @abstractmethod
    def calculate_fee(self):
        pass


class BasicMembership(Membership):
    def __init__(self):
        super().__init__(25.00)

    def calculate_fee(self):
        return self.monthly_fee


class PremiumMembership(Membership):
    def __init__(self):
        super().__init__(45.00)
        self.class_access_surcharge = 10.00

    def calculate_fee(self):
        return self.monthly_fee + self.class_access_surcharge


class VIPMembership(Membership):
    def __init__(self, months_active=0):
        super().__init__(80.00)
        self.personal_trainer_fee = 30.00
        self.months_active = months_active

    def calculate_fee(self):
        total = self.monthly_fee + self.personal_trainer_fee
        if self.months_active >= 12:
            total = total * 0.9
        return total
