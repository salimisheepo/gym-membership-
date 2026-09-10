from person import Person


class Trainer(Person):
    def __init__(self, name, id_number, age, phone, specialty):
        super().__init__(name, id_number, age, phone)
        self.specialty = specialty
        self.classes_led = []

    def get_specialty(self):
        return self.specialty

    def print_info(self):
        return "Trainer: " + self.name + " (ID " + self.id_number + "), age " + str(self.age) + ", specialty: " + self.specialty

    def lead_class(self, gym_class):
        gym_class.trainer = self
        if gym_class not in self.classes_led:
            self.classes_led.append(gym_class)
