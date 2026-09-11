
from abc import ABC, abstractmethod

class Membership(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

    @abstractmethod
    def max_classes(self):
        """Maximum number of classes a member on this plan may be enrolled in
        at the same time. Return float('inf') for no limit."""
        pass

class BasicMembership(Membership):
    def calculate_fee(self):
        return 25.0

    def max_classes(self):
        return 1

class PremiumMembership(Membership):
    def calculate_fee(self):
        return 55.0

    def max_classes(self):
        return 3

class VIPMembership(Membership):
    def __init__(self, months=0):
        self.months = months

    def calculate_fee(self):
        fee = 110.0
        if self.months >= 12:
            fee = fee * 0.9
        return fee

    def max_classes(self):
        return float("inf")
