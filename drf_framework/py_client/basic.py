import requests

endpoint = 'http://localhost:8000/api/get_product/'

response = requests.get(endpoint, params={'param1':'abc'}, json={'query':'test'})

# print(response.text)
print(response.status_code)
print(response.json())
