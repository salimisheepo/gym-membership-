from abc import ABC, abstractmethod


class Person(ABC):


    def __init__(self, name, pid, age, phone):
        if not name or not name.strip():
            raise ValueError('Name cannot be empty')
        if not pid or not pid.strip():
            raise ValueError('ID cannot be empty')
        if not isinstance(age, int) or age <= 0 or age > 120:
            raise ValueError(f'Age must be a realistic whole number, got {age}')
        if not phone or not phone.strip():
            raise ValueError('Phone number cannot be empty')
        self.name = name.strip()
        self.pid = pid.strip()
        self.age = age
        self.phone = phone.strip()

    @abstractmethod

    def details(self):
        pass


    def profile_summary(self):
        return f'{self.name} (ID: {self.pid}, Age: {self.age})'


    def __str__(self):
        return self.details()


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.pid == other.pid


    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
