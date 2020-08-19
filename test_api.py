import requests

server_ip = "http://127.0.0.1:8000/api/v1"


def registration(email, password):
    url = f'{server_ip}/rest-auth/registration/'
    data = {'email': email, 'password1': password, 'password2': password}
    resp = requests.post(url, json=data)
    print(resp.json())


def login(username, password):
    url = f'{server_ip}/rest-auth/login/'
    login_data = {'username': username, 'password': password}
    token = requests.post(url, json=login_data).json()
    print(token)
    return token['key']


def logout(token):
    headers = {"Authorization": "token {}".format(token)}
    url = f'{server_ip}/rest-auth/logout/'
    resp = requests.post(url, headers=headers)
    print(resp.text)


def upload_metadata(user_token):
    url = f'{server_ip}/metadata/'
    headers = {"Authorization": "token {}".format(user_token)}
    data = {'name': 'custom_data1', 'value': 'custom_value1'}
    resp = requests.post(url, data=data, headers=headers)
    print(resp.status_code, resp.text, sep='\n')


def get_metadata(user_token):
    url = f'{server_ip}/metadata/'
    headers = {"Authorization": "token {}".format(user_token)}
    resp = requests.get(url, headers=headers)
    print(resp.json())


def get_metadata_by_name(user_token, name):
    url = f'{server_ip}/metadata/{name}'
    headers = {"Authorization": "token {}".format(user_token)}
    resp = requests.get(url, headers=headers)
    print(resp.json())


def upload_doc(user_token, file_name):
    url = f'{server_ip}/docs/'
    headers = {"Authorization": "token {}".format(user_token)}
    files = {'file': open(file_name, 'rb')}
    resp = requests.post(url, files=files, headers=headers)
    print(resp.json())


def get_docs(user_token):
    url = f'{server_ip}/docs/'
    headers = {"Authorization": "token {}".format(user_token)}
    resp = requests.get(url, headers=headers)
    print(resp.json())


def get_doc_by_name(user_token, filename):
    url = f'{server_ip}/docs/{filename}'
    headers = {"Authorization": "token {}".format(user_token)}
    resp = requests.get(url, headers=headers)
    print(resp.json())


# registration('email@gmail.com', 'opensource')

# login('mohamed', 'opensource')

# get_metadata('1dad19f63f4f784f0aa5af6d991d867b8fe67776')

# get_metadata_by_name('1dad19f63f4f784f0aa5af6d991d867b8fe67776', 'custom_data1')

# upload_metadata('1dad19f63f4f784f0aa5af6d991d867b8fe67776')

# upload_doc('1dad19f63f4f784f0aa5af6d991d867b8fe67776', 'manage.py')

get_doc_by_name('1dad19f63f4f784f0aa5af6d991d867b8fe67776', 'manage.py')

# get_docs('1dad19f63f4f784f0aa5af6d991d867b8fe67776')
