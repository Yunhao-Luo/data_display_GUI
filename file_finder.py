from textwrap import indent
from configuration import *
import os
import csv

class FileFinder:
    def __init__(self, path):
        self.root_path = path
        self.file_names = []
        os.chdir(path)
        for file in os.listdir():
            self.file_names.append(file)

    def find_id_sessions(self, id_name):
        sessions_list = []
        results_file = ""
        for root, dires, files in os.walk(self.root_path):
            for file in files:
                if id_name in file and "summary" not in file:
                    date = file[file.find('_')+1:file.rfind("_")]
                    if date not in sessions_list:
                        sessions_list.append(date)

        results_file = self.find_all_files_date(id_name, "sessions")[0]
        with open(results_file, 'r', newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
        se_list = []
        for i in data:
            se_list.append(i[0] + "_" + i[1])
        res = []
        for i in sessions_list:
            if i in se_list:
                res.append(i)
        return res

    def find_all_files_date(self, id, date):
        files_same_date = []
        for root, dires, files in os.walk(self.root_path):
            for file in files:
                temp = id + "_" + date
                if temp in file:
                    files_same_date.append(root + "\\" + file)
        return files_same_date
    
    def find_result_file(self, id):
        sessions = self.find_id_sessions(id)
        res = []
        for root, dires, files in os.walk(self.root_path):
            for file in files:
                test = file[file.find("_")+1:file.rfind("_")]
                if id in file and test in sessions and "results" in file:
                    res.append(root + "\\" + file)
        return res


""" if __name__ == "__main__":
    test = FileFinder(DATA_PATH)
    test.read_file_names()

    print(test.find_id_sessions("asdf_06")) """