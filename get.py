import requests

base_url = 'https://httpbin.org'
endpoint = '/get'
url = base_url + endpoint

response = requests.get(url)

# Print response data
print(response.status_code)  # Status code
print(response.json())       # Response data in JSON format
print(response.json()['headers']['Host'])

