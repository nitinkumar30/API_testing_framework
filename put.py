import requests

base_url = 'https://httpbin.org'
endpoint = '/put'
url = base_url + endpoint

data = {'username': 'nitinkumar'}
response = requests.put(url, json=data)

# Print response status code and data
print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())
