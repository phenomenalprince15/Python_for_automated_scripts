import requests

# Send a GET request to an API
response = requests.get('https://api.github.com')

if response.status_code == 200:
    print(response.json())


# Send a POST request
data = {'name' : 'test-repo'}
response = requests.post('https://api.github.com/user/repos', json=data,
                        auth=('user', 'token'))
