import os
import pickle


class DataHandler:
    cur_path = os.path.dirname(__file__)
    filename = '\\'.join(cur_path.split('\\')[0:-1]) + '\\Files\\data.txt'

    @staticmethod
    def load_current(filename):
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    @staticmethod
    def save_record(record):

        items = DataHandler.load_current(DataHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        cur_list.append(record)

        with open(DataHandler.filename, 'wb') as wf:
            for l in cur_list:
                pickle.dump(l, wf)

    @staticmethod
    def view_records(patient_nic):
        items = DataHandler.load_current(DataHandler.filename)
        cur_list = []

        for t in items:
            cur_list.append(t)

        for record in cur_list:
            if record.nic == patient_nic:
                print('-'*30)
                print('Name of Patient: ' + record.name)
                print('Age of Patient: ' + record.age)
                print('Sickness Details: ' + record.sickness)
                print('Drug Prescriptions: ' + record.drug_prescription)
                print('Lab test prescriptions: ' + record.lab_test)
                print('-' * 30)
    @staticmethod
    def enter_lab_tests(patient_nic, new):
        records = DataHandler.load_current(DataHandler.filename)
        cur_list = []

        for t in records:
            cur_list.append(t)

        for record in reversed(cur_list):
            if record.nic == patient_nic:
                record.lab_test = new
                break
        with open(DataHandler.filename, 'wb') as wf:
            for l in cur_list:
                pickle.dump(l, wf)

    @staticmethod
    def fetch_latest(patient_nic):
        records = DataHandler.load_current(DataHandler.filename)
        cur_list = []

        for t in records:
            cur_list.append(t)

        for record in reversed(cur_list):
            if record.nic == patient_nic:
                return record.lab_test