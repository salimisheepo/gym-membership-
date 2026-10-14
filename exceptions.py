class GymError(Exception):
    pass


class DuplicateEntryError(GymError):
    pass


class ClassFullError(GymError):
    pass


class DataFileError(GymError):
    pass
