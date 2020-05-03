from FileHandler.ConfigHandler import ConfigHandler
from FileHandler.DataHandler import DataHandler


class ViewUI:
    @staticmethod
    def view_users():
        print('View all users')
        ConfigHandler.view_data()

    @staticmethod
    def view_record(patient_nic):
        DataHandler.view_records(patient_nic)