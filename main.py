import pickle

from UI.HomeUI import HomeUI
from Helpers.HashClass import HashClass
from FileHandler.ConfigHandler import ConfigHandler


def main():
    # HashClass.hash_password('shammi')
    #
    # records = ConfigHandler.load_current(ConfigHandler.filename)
    # cur_list = []
    #
    # for t in records:
    #     cur_list.append(t)
    #
    # for data in reversed(cur_list):
    #
    #     new_pass = HashClass.hash_password(data.password)
    #     data.password = new_pass
    #
    # with open(ConfigHandler.filename, 'wb') as wf:
    #     for l in cur_list:
    #         pickle.dump(l, wf)

    HomeUI().display()


if __name__ == '__main__':
    main()
