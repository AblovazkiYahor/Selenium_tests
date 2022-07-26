import requests


response = requests.get(url='https://jsonplaceholder.typicode.com/posts/50').json()
print(response['body'])

response_2 = requests.post(url='https://jsonplaceholder.typicode.com/posts')
assert response_2.status_code == 201

if response_2.status_code == 201:
    print('Response is successfully!') 
