# from django.test import TestCase
import json, requests, time


BASE_URL = 'http://127.0.0.1:8000'    # Local Server
# BASE_URL = 'http://tadpol.herokuapp.com'    # Golobal Server
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
    print('Status Code: ' + str(str(resp.status_code)))
    print('data: ', resp.json())


def create_resource(title, check, date):
    data = {
        'title': title,
        'check': check,
        'date_to_do': date
    }
    resp = requests.post(url, data=json.dumps(data))
    print('Status Code: ' + str(resp.status_code))
    print('data: ', resp.json())


def update_resource(id, title, check, date):
    data = {
    	'id': int(id, 10),
    	'title': title,
        'check': check,
        'date_to_do': date
    }
    resp = requests.put(url, data=json.dumps(data))
    print('Status Code: ' + str(resp.status_code))
    print('data: ', resp.json())

def delete_resource(id):
    data = {
        'id': int(id, 10)
    }
    resp = requests.delete(url, data=json.dumps(data))
    print('Status Code: ' + str(resp.status_code))
    print('data: ', resp.json())


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
        time.sleep(1)

initiate()
