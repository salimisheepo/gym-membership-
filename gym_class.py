from member import Member
from trainer import Trainer
from equipment import Equipment
from exceptions import ClassFullError
from queue_adt import Queue


class GymClass:


    def __init__(self, name, schedule, capacity=None, max_waiting=5):
        if not name or not name.strip():
            raise ValueError('Class name cannot be empty')
        if not schedule or not schedule.strip():
            raise ValueError('Schedule cannot be empty')
        if capacity is not None and (not isinstance(capacity, int) or capacity <= 0):
            raise ValueError('Capacity must be a positive whole number, or None for unlimited')
        self.name = name.strip()
        self.schedule = schedule.strip()
        self.members = []
        self.trainer = None
        self.equipment = []
        self.capacity = capacity
        self.max_waiting = max_waiting
        self.waiting_list = Queue()


    def add_member(self, person):
        if not isinstance(person, Member):
            raise TypeError('Only members can join classes')
        if person in self.members:
            return 'already_in'
        if not person.can_join_class():
            raise ValueError(f"{person.name}'s {person.membership.plan_name()} plan only allows {person.membership.max_classes_display()} class(es) at a time")
        if self.capacity is not None and len(self.members) >= self.capacity:
            if person in self.waiting_list.to_list():
                return 'already_waiting'
            if self.waiting_list.size() >= self.max_waiting:
                raise ClassFullError(f'{self.name} is full and its waiting list ({self.max_waiting}) is also full')
            self.waiting_list.enqueue(person)
            return 'waitlisted'
        self.members.append(person)
        person.classes.append(self)
        return 'joined'


    def remove_member(self, person):
        if person in self.members:
            self.members.remove(person)
            if self in person.classes:
                person.classes.remove(self)
            self._promote_from_waiting_list()


    def _promote_from_waiting_list(self):
        has_room = self.capacity is None or len(self.members) < self.capacity
        if has_room and (not self.waiting_list.is_empty()):
            next_person = self.waiting_list.dequeue()
            if next_person.can_join_class():
                self.members.append(next_person)
                next_person.classes.append(self)
            else:
                self._promote_from_waiting_list()


    def set_trainer(self, trainer):
        if not isinstance(trainer, Trainer):
            raise TypeError('Only a Trainer can be assigned to a class')
        self.trainer = trainer


    def add_equipment(self, item):
        if not isinstance(item, Equipment):
            raise TypeError('Only Equipment objects can be added')
        if item not in self.equipment:
            self.equipment.append(item)


    def count_members(self):
        return len(self.members)


    def __str__(self):
        trainer_name = self.trainer.name if self.trainer else 'No trainer assigned'
        cap_display = 'Unlimited' if self.capacity is None else str(self.capacity)
        return f'{self.name} ({self.schedule}) — Trainer: {trainer_name} — {self.count_members()}/{cap_display} member(s), {self.waiting_list.size()} waiting'


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if not isinstance(other, GymClass):
            return NotImplemented
        return self.name == other.name
