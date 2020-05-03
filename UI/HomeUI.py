from UI.DoctorLoginUI import DoctorLoginUI
from UI.OtherLoginUI import OtherLoginUI


class HomeUI:
    @staticmethod
    def display():
        print("----------LOG IN----------")

        print('Select a number according to your user type:\n1 - Admin\n2 - Doctor\n3 - Staff\n4 - Patient')

        selected = input().strip()

        if selected == "2":
            DoctorLoginUI().display()
        elif selected == "1" or selected == "3" or selected == "4":
            OtherLoginUI().display(selected)
        else:
            print("INVALID INPUT")
