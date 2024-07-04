import requests

base_url = 'https://httpbin.org'
endpoint = '/delete'
url = base_url + endpoint

response = requests.delete(url)

# Print response status code
print("Status Code:", response.status_code)
