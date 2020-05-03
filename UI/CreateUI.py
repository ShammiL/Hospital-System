from Users.Admin import Admin
from FileHandler.ConfigHandler import ConfigHandler
from FileHandler.DataHandler import DataHandler
from Users.Doctor import Doctor
from Users.Patient import Patient
from Users.Staff import Staff
from records.Record import Record
from Helpers.HashClass import HashClass


class CreateUI:
    @staticmethod
    def create_user(tpe):
        print('creating new user')
        if tpe == '1':
            name = input('Name: ')
            password = input('Password: ')
            age = input('Age: ')
            nic = input('NIC: ')
            hashed = HashClass.hash_password(password)
            admin = Admin(name, hashed, age, nic)
            ConfigHandler.save_data(admin)

        elif tpe == '2':
            name = input('Name: ')
            password = input('Password: ')
            age = input('Age: ')
            nic = input('NIC: ')
            reg_no = input('Registration Number: ')
            hashed = HashClass.hash_password(password)
            doctor = Doctor(name, hashed, age, nic, reg_no)
            ConfigHandler.save_data(doctor)

        elif tpe == '3':
            name = input('Name: ')
            password = input('Password: ')
            age = input('Age: ')
            nic = input('NIC: ')
            hashed = HashClass.hash_password(password)
            staff = Staff(name, hashed, age, nic)
            ConfigHandler.save_data(staff)

        elif tpe == '4':
            name = input('Name: ')
            password = input('Password: ')
            age = input('Age: ')
            nic = input('NIC: ')
            mobile_no = input('Mobile Number: ')
            hashed = HashClass.hash_password(password)
            patient = Patient(name, hashed, age, nic, mobile_no)
            ConfigHandler.save_data(patient)

    @staticmethod
    def create_record():
        print('creating new record')
        name = input('Name: ')
        age = input('age: ')
        nic = input('NIC: ')
        sickness = input('Sickness details: ')
        drug_prescription = input('Drugs prescription: ')
        record = Record(name, age, nic, sickness, drug_prescription)
        DataHandler.save_record(record)

    @staticmethod
    def create_lab_test(patient_nic):
        print('-----fetching lab test prescriptions of patient with nic ' + patient_nic + '-----')
        print('-'*30)
        print(DataHandler.fetch_latest(patient_nic))
        new = input('Enter new lab test prescriptions')
        DataHandler.enter_lab_tests(patient_nic, new)
