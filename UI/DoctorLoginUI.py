from FileHandler.ConfigHandler import ConfigHandler
from UI.CreateUI import CreateUI
from UI.ViewUI import ViewUI


class DoctorLoginUI:

    @staticmethod
    def display():
        reg_no = input('Registration Number: ')
        password = input('Password: ')
        res = ConfigHandler.doctor_validate(reg_no, password)
        DoctorLoginUI.menu(res)

    @staticmethod
    def menu(res):
        if res:
            print("LOGIN SUCCESSFUL")

            print("Select a number from menu\n1- Create New Record\n2- View Patient Record")
            menu_no = input().strip()
            if menu_no == '1':
                CreateUI.create_record()
            elif menu_no == '2':
                patient_nic = input('Enter patient NIC: ')
                ViewUI.view_record(patient_nic)
            else:
                print("INVALID INPUT")
        else:
            print("LOGIN FAILED")
