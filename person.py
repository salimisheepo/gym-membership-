
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, pid, age, phone):
        self.name = name
        self.pid = pid
        self.age = age
        self.phone = phone

    @abstractmethod
    def details(self):
        pass
