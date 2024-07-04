import requests

base_url = 'https://httpbin.org'
endpoint = '/patch'
url = base_url + endpoint

data = {'username': 'nitinkr'}
response = requests.patch(url, json=data)

# Print response status code and data
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())
