class Equipment:


    def __init__(self, name, eq_type):
        if not name or not name.strip():
            raise ValueError('Equipment name cannot be empty')
        if not eq_type or not eq_type.strip():
            raise ValueError('Equipment type cannot be empty')
        self.name = name.strip()
        self.eq_type = eq_type.strip()


    def __str__(self):
        return f'{self.name} ({self.eq_type})'


    def __repr__(self):
        return self.__str__()


    def __eq__(self, other):
        if not isinstance(other, Equipment):
            return NotImplemented
        return self.name == other.name and self.eq_type == other.eq_type
