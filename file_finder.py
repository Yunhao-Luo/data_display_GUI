from configuration import *
import os

class FileFinder:
    def __init__(self, path):
        self.root_path = path
        self.file_names = []
        os.chdir(path)
        for file in os.listdir():
            self.file_names.append(file)

    def find_id_sessions(self, id_name):
        sessions_list = []
        for root, dires, files in os.walk(self.root_path):
            for file in files:
                if id_name in file:
                    date = file[file.find('_')+1:]
                    date = date[0:date.find("_")]
                    if date not in sessions_list:
                        sessions_list.append(date)
        return sessions_list

    def find_all_files_date(self, id, date):
        files_same_date = []
        for root, dires, files in os.walk(self.root_path):
            for file in files:
                if id and date in file:
                    files_same_date.append(root + "\\" + file)
        return files_same_date


""" if __name__ == "__main__":
    test = FileFinder(DATA_PATH)
    test.read_file_names()

    print(test.find_id_sessions("asdf_06")) """