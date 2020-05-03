from Users.User import User


class Admin(User):

    def __init__(self, name, password, age, nic):
        User.__init__(self, name, password, age, nic)
        self.type = "Admin"


