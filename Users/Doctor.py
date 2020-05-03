from Users.User import User


class Doctor(User):

    def __init__(self, name, password, age, nic, reg_no):
        User.__init__(self, name, password, age, nic)
        self.regNo = reg_no
        self.type = "Doctor"


