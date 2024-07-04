import requests

base_url = 'https://dummy.restapiexample.com/api/v1'
endpoint = 'employees'

url = f'{base_url}/{endpoint}'  # You can also use f-strings for string formatting
print(url)

try:
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception for HTTP errors
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
