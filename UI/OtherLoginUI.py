from FileHandler.ConfigHandler import ConfigHandler
from UI.CreateUI import CreateUI
from UI.ViewUI import ViewUI


class OtherLoginUI:

    @staticmethod
    def display(selected):
        nic = input('NIC: ')
        password = input('Password: ')
        res = ConfigHandler.other_validate(nic, password)
        OtherLoginUI.menu(res, selected, nic)

    @staticmethod
    def menu(res, selected, nic):
        if res:
            print("LOGIN SUCCESSFUL")
            if selected == '1':

                print("Select a number from menu\n1- Create New User\n2- View All Users")
                menu_no = input().strip()
                if menu_no == "1":
                    print('Select corresponding number to create the user you want\n1- admin\n2- Doctor\n3- Staff')
                    tpe = input().strip()
                    CreateUI.create_user(tpe)
                elif menu_no == "2":
                    ViewUI.view_users()
                else:
                    print("INVALID INPUT")
            if selected == '3':
                print("Select a number from menu\n1- Enter lab prescription\n2- View patient record\n3- Create new patient")
                menu_no = input().strip()
                if menu_no == '1':
                    patient_nic = input('Enter patient NIC: ')
                    CreateUI.create_lab_test(patient_nic)
                elif menu_no == '2':
                    patient_nic = input('Enter patient NIC: ')
                    ViewUI.view_record(patient_nic)
                elif menu_no == '3':
                    CreateUI.create_user('4')
                else:
                    print("INVALID INPUT")
            if selected == '4':
                print('Your Past Records')
                ViewUI.view_record(nic)

        else:
            print("LOGIN FAILED")
