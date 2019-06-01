# from django.test import TestCase
import json, requests


BASE_URL = 'http://127.0.0.1:8000'
ENDPOINT = '/task/'
url = BASE_URL + ENDPOINT


# Create your tests here.
def get_resource(id):
    if id is '0':
        data = {
            'id': None
        }
    else:
        data = {
            'id': int(id, 10)
        }
    resp = requests.get(url, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def create_resource(title, check, date):
    data = {
        'title': title,
        'check': check,
        'date_to_do': date
    }
    resp = requests.post(url, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def update_resource(id, title, check, date):
    data = {
    	'id': int(id, 10),
    	'title': title,
        'check': check,
        'date_to_do': date
    }
    resp = requests.put(url, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def delete_resource(id):
    data = {
        'id': int(id, 10)
    }
    resp = requests.delete(url, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def initiate():
    print("")
    print("================================")
    print("This is an API Testing Interface")
    print("================================")
    print("Press: 1 ---- To GET record(s) -")
    print("Press: 2 ---- To POST a record -")
    print("Press: 3 ---- To PUT a record --")
    print("Press: 4 ---- To DELETE data ---")
    print("Press: Any -- To Exit ----------")
    print("================================")
    flag = input("Press: ")
    print("================================")
    if flag is '1':
        id = input("Enter ID [OR] 0 to get all records: ")
        get_resource(id)
        initiate()
    elif flag is '2':
        title = input("Title: ")
        check = input("Done(True/False): ")
        date = input("Date(YYYY-MM-DD): ")
        create_resource(title, check, date)
        initiate()
    elif flag is '3':
        id = input("ID: ")
        title = input("Title: ")
        check = input("Done(True/False): ")
        date = input("Date(YYYY-MM-DD): ")
        update_resource(id, title, check, date)
        initiate()
    elif flag is '4':
        id = input("ID: ")
        if id is not None:
            delete_resource(id)
            initiate()
        else:
            print("Invalid Input! Please try again...")
            initiate()
    else:
        print("---------- TEST ENDED ----------")
        exit()

initiate()
