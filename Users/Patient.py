from Users.User import User


class Patient(User):

    def __init__(self, name, password, age, nic, mobile_no):
        User.__init__(self, name, password, age, nic)
        self.mobileNo = mobile_no
        self.type = "Patient"


