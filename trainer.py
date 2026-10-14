from person import Person


class Trainer(Person):


    def __init__(self, name, pid, age, phone, speciality):
        super().__init__(name, pid, age, phone)
        if not speciality or not speciality.strip():
            raise ValueError('Speciality cannot be empty')
        self.speciality = speciality.strip()


    def profile_summary(self):
        base = super().profile_summary()
        return f'{base} — Trainer specializing in {self.speciality}'


    def details(self):
        return f'Trainer: {self.name} | Age: {self.age} | Phone: {self.phone} | Speciality: {self.speciality}'
