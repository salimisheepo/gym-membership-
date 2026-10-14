from abc import ABC, abstractmethod


class Membership(ABC):

    @abstractmethod

    def calculate_fee(self):
        pass

    @abstractmethod

    def max_classes(self):
        pass

    @abstractmethod

    def plan_name(self):
        pass


    def max_classes_display(self):
        limit = self.max_classes()
        return 'Unlimited' if limit == float('inf') else str(limit)


    def __str__(self):
        return f'{self.plan_name()} (N${self.calculate_fee():.2f}/month)'


class BasicMembership(Membership):


    def calculate_fee(self):
        return 25.0


    def max_classes(self):
        return 1


    def plan_name(self):
        return 'Basic'


class PremiumMembership(Membership):


    def calculate_fee(self):
        return 55.0


    def max_classes(self):
        return 3


    def plan_name(self):
        return 'Premium'


class VIPMembership(Membership):


    def __init__(self, months=0):
        if not isinstance(months, int) or months < 0:
            raise ValueError(f'VIP months must be a non-negative whole number, got {months}')
        self.months = months


    def calculate_fee(self):
        fee = 110.0
        if self.months >= 12:
            fee = fee * 0.9
        return fee


    def max_classes(self):
        return float('inf')


    def plan_name(self):
        return 'VIP'
