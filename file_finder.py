from configuration import *
import os

class FileFinder:
    def __init__(self, path):
        self.file_names = []
        os.chdir(path)
        for file in os.listdir():
            if file.endswith(".txt") or file.endswith(".csv"):
                self.file_names.append(file)

    def find_id_sessions(self, id_name):
        sessions_list = []
        for file in self.file_names:
            date = file[file.find('_')+1:]
            date = date[0:date.find("_")]
            if id_name in file and date not in sessions_list:
                sessions_list.append(date)
        return sessions_list

    def find_all_files_date(self, id, date):
        files_same_date = []
        for file in self.file_names:
            if id in file and date in file:
                files_same_date.append(file)
        return files_same_date

""" if __name__ == "__main__":
    test = FileFinder(DATA_PATH)
    test.read_file_names()

    print(test.find_id_sessions("asdf_06")) """