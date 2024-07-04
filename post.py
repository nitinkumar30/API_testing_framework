import requests

base_url = 'https://httpbin.org'
endpoint = '/post'
url = base_url + endpoint

data = {'username': 'john_doe', 'email': 'john_doe@example.com'}
response = requests.post(url, json=data)

# Print response data
print(response.status_code)  # Status code
print(response.json())       # Response data in JSON format
data = response.json()['data']
print(data)

