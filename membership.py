
from abc import ABC, abstractmethod

class Membership(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

class BasicMembership(Membership):
    def calculate_fee(self):
        return 25.0

class PremiumMembership(Membership):
    def calculate_fee(self):
        return 55.0

class VIPMembership(Membership):
    def __init__(self, months=0):
        self.months = months

    def calculate_fee(self):
        fee = 110.0
        if self.months >= 12:
            fee = fee * 0.9
        return fee
