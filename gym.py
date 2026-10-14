import json
from member import Member
from trainer import Trainer
from equipment import Equipment
from gym_class import GymClass
from exceptions import DuplicateEntryError, DataFileError


class Gym:


    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError('Gym name cannot be empty')
        self.name = name.strip()
        self.members = []
        self.trainers = []
        self.classes = []
        self.equipment = []


    def add_member(self, member):
        if not isinstance(member, Member):
            raise TypeError('Only a Member can be added to gym.members')
        if any((m.pid == member.pid for m in self.members)):
            raise DuplicateEntryError(f"A member with ID '{member.pid}' already exists")
        self.members.append(member)


    def add_trainer(self, trainer):
        if not isinstance(trainer, Trainer):
            raise TypeError('Only a Trainer can be added to gym.trainers')
        if any((t.pid == trainer.pid for t in self.trainers)):
            raise DuplicateEntryError(f"A trainer with ID '{trainer.pid}' already exists")
        self.trainers.append(trainer)


    def add_equipment(self, item):
        if not isinstance(item, Equipment):
            raise TypeError('Only Equipment can be added to gym.equipment')
        if item not in self.equipment:
            self.equipment.append(item)


    def add_class(self, gym_class):
        if gym_class not in self.classes:
            if any((c.name == gym_class.name for c in self.classes)):
                raise DuplicateEntryError(f"A class named '{gym_class.name}' already exists")
            self.classes.append(gym_class)


    def total_fee(self, a, b=None):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, Member) and isinstance(b, Member):
            return a.get_fee() + b.get_fee()
        elif isinstance(a, Member) and b is None:
            return a.get_fee()
        else:
            raise TypeError('total_fee() expects either two numbers, two Members, or one Member')


    def register_member_safe(self, member):
        added = False
        try:
            self.add_member(member)
        except DuplicateEntryError as error:
            print(f'Registration failed: {error}')
        except (TypeError, ValueError) as error:
            print(f'Invalid member data: {error}')
        else:
            print(f'Registered {member.name} successfully.')
            added = True
        finally:
            print(f"Finished attempting to register '{member.name}'.")
        return added


    def avg_age(self):
        if len(self.members) == 0:
            return 0
        total = 0
        for m in self.members:
            total += m.age
        return total / len(self.members)


    def find_person(self, name):
        if not name or not name.strip():
            return []
        found = []
        for p in self.members + self.trainers:
            if name.lower() in p.name.lower():
                found.append(p)
        return found


    def find_class(self, class_name):
        for c in self.classes:
            if c.name == class_name:
                return c
        return None


    def to_dict(self):
        return {'gym_name': self.name, 'equipment': [{'name': e.name, 'eq_type': e.eq_type} for e in self.equipment], 'trainers': [{'name': t.name, 'pid': t.pid, 'age': t.age, 'phone': t.phone, 'speciality': t.speciality} for t in self.trainers], 'members': [{'name': m.name, 'pid': m.pid, 'age': m.age, 'phone': m.phone, 'membership_type': m.membership.plan_name().lower(), 'vip_months': getattr(m.membership, 'months', 0)} for m in self.members], 'classes': [{'name': c.name, 'schedule': c.schedule, 'capacity': c.capacity, 'max_waiting': c.max_waiting, 'waiting_pids': [w.pid for w in c.waiting_list.to_list()], 'trainer_pid': c.trainer.pid if c.trainer else None, 'member_pids': [member.pid for member in c.members], 'equipment_names': [eq.name for eq in c.equipment]} for c in self.classes]}


    def save_to_file(self, filepath):
        try:
            with open(filepath, 'w') as file:
                json.dump(self.to_dict(), file, indent=2)
        except OSError as error:
            raise DataFileError(f"Could not save to '{filepath}': {error}") from error

    @classmethod

    def load_from_file(cls, filepath):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
        except FileNotFoundError as error:
            raise DataFileError(f"File '{filepath}' was not found") from error
        except json.JSONDecodeError as error:
            raise DataFileError(f"File '{filepath}' is not valid JSON: {error}") from error
        gym = cls(data.get('gym_name', 'Gym'))
        for e in data.get('equipment', []):
            gym.add_equipment(Equipment(e['name'], e['eq_type']))
        for t in data.get('trainers', []):
            gym.add_trainer(Trainer(t['name'], t['pid'], t['age'], t['phone'], t['speciality']))
        for m in data.get('members', []):
            gym.add_member(Member(m['name'], m['pid'], m['age'], m['phone'], m['membership_type'], vip_months=m.get('vip_months', 0)))
        for c in data.get('classes', []):
            gym_class = GymClass(c['name'], c['schedule'], capacity=c.get('capacity'), max_waiting=c.get('max_waiting', 5))
            trainer_pid = c.get('trainer_pid')
            if trainer_pid:
                trainer = next((t for t in gym.trainers if t.pid == trainer_pid), None)
                if trainer:
                    gym_class.set_trainer(trainer)
            for pid in c.get('member_pids', []):
                member = next((m for m in gym.members if m.pid == pid), None)
                if member:
                    gym_class.add_member(member)
            for pid in c.get('waiting_pids', []):
                member = next((m for m in gym.members if m.pid == pid), None)
                if member:
                    gym_class.waiting_list.enqueue(member)
            for eq_name in c.get('equipment_names', []):
                equipment = next((e for e in gym.equipment if e.name == eq_name), None)
                if equipment:
                    gym_class.add_equipment(equipment)
            gym.add_class(gym_class)
        return gym


    def full_report(self):
        lines = []
        for group_name, group in [('Members', self.members), ('Trainers', self.trainers), ('Classes', self.classes), ('Equipment', self.equipment)]:
            lines.append(f'-- {group_name} --')
            for item in group:
                lines.append(str(item))
        return '\n'.join(lines)
