import csv
import json
import os
os.chdir(os.path.dirname(__file__))

'''
Здесь мы считываем и сохраняем, в нашу базу, записи из файла, 
который указал пользователь
'''


def copy_cont(n, nn):
    path = n

    def import_csv(path_to_import_csv_file):
        data = []
        with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:

            file_reader = csv.reader(file, delimiter=";", lineterminator="\n")
            for row in file_reader:
                data.append(row)
        return data
    d = import_csv(path)
    f = nn
    arr = []
    for i in range(len(d)):
        if f in d[i]:
            arr.append(d[i])
    return arr


def copy_cont_json(n, nn):
    path = n

    def import_json(path):
        data = []
        with open(path, "r", encoding='utf-8') as file:
            file_reader = json.load(file)
            for i in range(0, len(file_reader)):
                g = list(file_reader[i])
                data.append(g)
        return data

    d = import_json(path)
    new = nn
    arr = []
    for i in range(len(d)):
        if new in d[i]:
            arr.append(d[i])

    for i in range(len(arr)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(arr[i])


def copy_cont1(n):
    path = n

    def import_csv(path_to_import_csv_file):
        data = []
        with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:

            file_reader = csv.reader(file, delimiter=";", lineterminator="\n")
            for row in file_reader:
                data.append(row)
        return data
    d = import_csv(path)
    
    arr = []
    for i in range(len(d)):
        
        arr.append(d[i])
    return arr


def copy_cont_json1(n):
    path = n

    def import_json(path):
        data = []
        with open(path, "r", encoding='utf-8') as file:
            file_reader = json.load(file)
            for i in range(0, len(file_reader)):
                g = list(file_reader[i])
                data.append(g)
        return data

    d = import_json(path)
    
    arr = []
    for i in range(len(d)):
        arr.append(d[i])

    for i in range(len(arr)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';', lineterminator="\n")
            csv_fil.writerow(arr[i])




def write_csv(data):
    for i in range(len(data)):
        with open('phonebook.csv', "a", newline='', encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';', lineterminator="\n")
            csv_fil.writerow(data[i])
            print('Данные успешно записаны')