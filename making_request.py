import requests

# making a request to another server

response = requests.get('https://api.github.com/eventjjefs')

print(response.status_code)
print(response.json())
print(response.content)