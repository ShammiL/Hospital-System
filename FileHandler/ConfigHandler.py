import os
import pickle
from Helpers.HashClass import HashClass

class ConfigHandler:
    cur_path = os.path.dirname(__file__)
    filename = '\\'.join(cur_path.split('\\')[0:-1]) + '\\Files\\config.txt'

    @staticmethod
    def load_current(filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    @staticmethod
    def save_data(data):

        items = ConfigHandler.load_current(ConfigHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        cur_list.append(data)

        with open(ConfigHandler.filename, 'wb') as wf:
            for l in cur_list:
                pickle.dump(l, wf)

    @staticmethod
    def other_validate(nic, password):
        items = ConfigHandler.load_current(ConfigHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        for obj in cur_list:
            if obj.type == 'Admin' and obj.NIC == nic and obj.password == HashClass.hash_password(password):
                return True
            elif obj.type == 'Patient' and obj.NIC == nic and obj.password == HashClass.hash_password(password):
                return True
            elif obj.type == 'Staff' and obj.nic == nic and obj.password == HashClass.hash_password(password):
                return True
            else:
                continue
        return False

    @staticmethod
    def doctor_validate(reg_no, password):
        items = ConfigHandler.load_current(ConfigHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        for obj in cur_list:
            if obj.type == 'Doctor' and obj.password == HashClass.hash_password(password):
                if obj.regNo == reg_no:
                    return True
            else:
                continue
        return False

    @staticmethod
    def view_data():
        items = ConfigHandler.load_current(ConfigHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        for data in cur_list:
            if data.type == 'Admin':
                print('-' * 30)
                print('Name: ' + data.name)
                print('Age: ' + str(data.age))
                print('Type: ' + data.type)
                print('NIC: ' + data.NIC)
                print('Password: ' + data.password)
                print('-' * 30)
            if data.type == 'Doctor':
                print('-' * 30)
                print('Name: ' + data.name)
                print('Age: ' + str(data.age))
                print('Type: ' + data.type)
                print('NIC: ' + data.nic)
                print('Registration Number: ' + data.regNo)
                print('Password: ' + data.password)
                print('-' * 30)
            if data.type == 'Staff':
                print('-' * 30)
                print('Name: ' + data.name)
                print('Age: ' + str(data.age))
                print('Type: ' + data.type)
                print('NIC: ' + data.nic)
                print('Password: ' + data.password)
                print('-' * 30)
            if data.type == 'Patient':
                print('-' * 30)
                print('Name: ' + data.name)
                print('Age: ' + str(data.age))
                print('Type: ' + data.type)
                print('NIC: ' + data.NIC)
                print('Password: ' + data.password)
                print('-' * 30)