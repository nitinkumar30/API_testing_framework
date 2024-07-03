import requests
import json


def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


def send_get_request(endpoint):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    response = requests.get(url)
    return response.json()


def send_post_request(endpoint, data):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()


def send_put_request(endpoint, data):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response.json()


def send_delete_request(endpoint):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    response = requests.delete(url)
    return response.status_code


def send_patch_request(endpoint, data):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    return response.json()


def send_options_request(endpoint):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    response = requests.options(url)
    allowed_methods = response.headers.get('allow', None)
    return allowed_methods.split(",") if allowed_methods else []


def send_head_request(endpoint):
    config = load_config()
    url = f"{config['base_url']}/{endpoint}"
    response = requests.head(url)
    return response.headers
