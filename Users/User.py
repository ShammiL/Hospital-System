import abc


class User(abc.ABC):
    def __init__(self, name, password, age, nic):
        self.name = name
        self.password = password
        self.age = age
        self.nic = nic



