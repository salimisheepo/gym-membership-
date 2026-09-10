from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, id_number, age, phone):
        self.name = name
        self.id_number = id_number
        self.age = age
        self.phone = phone

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    @abstractmethod
    def print_info(self):
        pass
